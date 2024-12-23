import boto3

from ..warning import Warning

class EKSELBDuplicateAnalyzer:
    warning: list = []
    def __init__(self, region: str):
        self.client = boto3.client('elb', region_name=region)
        self.region = region

    def name(self):
        return "EKSELBDuplicate"

    def fix_level(self):
        return "middle"

    def analyze(self):
        lbs =self.client.describe_load_balancers()
        lb_names = []
        for lb in lbs['LoadBalancerDescriptions']:
            lb_name = lb['LoadBalancerName']
            lb_names.append(lb_name)
        
        if len(lb_names) <= 0:
            return

        clusters = {}
        resp = self.client.describe_tags(LoadBalancerNames=lb_names)
        for lb_info in resp['TagDescriptions']:
            lb_name = lb_info['LoadBalancerName']
            for tag in lb_info['Tags']:
                if not tag['Key'].startswith('kubernetes.io/cluster/'):
                    continue

                cluster_name = tag['Key'].replace('kubernetes.io/cluster/','')
                if cluster_name not in clusters:
                    clusters[cluster_name] = []
                clusters[cluster_name].append(lb_name)
        
        for cluster in clusters:
            if len(clusters[cluster]) > 1:
                self.warning.append(Warning(cluster, self.region))

    def recommendations(self) -> list:
        ret: list = []
        for warning in self.warning:
            ret.append(f"EKS cluster {warning.resource_name} in region {warning.region} has multiple ELBs(It cost extra money), you can only use one ELB per cluster if you don't have high throughput, and the routing could be done in the cluster, through the service load balancer")
        return ret
