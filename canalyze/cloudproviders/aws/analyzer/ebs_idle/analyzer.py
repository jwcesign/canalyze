import boto3

from ..warning import Warning

class EBSIdleAnalyzer:
    warning: list = []
    def __init__(self, region: str):
        self.client = boto3.client('ec2', region_name=region)
        self.region = region

    def name(self):
        return "EBSIdle"

    def fix_level(self):
        return "easy"

    def analyze(self):
        volumes = self.client.describe_volumes()
        for volume in volumes['Volumes']:
            if volume['State'] == 'available':
                self.warning.append(Warning(volume['VolumeId'], self.region))

    def recommendations(self) -> list:
        ret: list = []
        for warning in self.warning:
            ret.append(f"EBS Volume {warning.resource_name} in region {warning.region} is idle, delete it to reduce the Cloud costs")
        return ret
