import boto3

from ..warning import Warning

class EKSObservabilityAnalyzer:
    warning: list = []
    def __init__(self, region: str):
        self.client = boto3.client('eks', region_name=region)
        self.region = region

    def analyze(self):
        clusters =self.client.list_clusters()
        cluster_info = []
        for cluster in clusters['clusters']:
            response = self.client.describe_cluster(name=cluster)
            cluster_info.append(response.get('cluster', {}))

        for cluster in cluster_info:
            for logging in cluster.get('logging', {}).get('clusterLogging'):
                if logging.get('enabled'):
                    self.warning.append(Warning(cluster.get('name'), self.region))

    def recommendations(self) -> list:
        ret: list = []
        for warning in self.warning:
            ret.append(f"Cluster {warning.resource_name} in region {warning.region} has logging enabled, if it's dev only, disable it to reduce the EBS costs")
        return ret
