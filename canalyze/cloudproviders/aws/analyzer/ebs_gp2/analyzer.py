import boto3

from ..warning import Warning

class EBSGP2Analyzer:
    warning: list = []
    def __init__(self, region: str):
        self.client = boto3.client('ec2', region_name=region)
        self.region = region

    def name(self):
        return "EBSGP2"

    def fix_level(self):
        return "easy"

    def analyze(self):
        volumes = self.client.describe_volumes()
        for volume in volumes['Volumes']:
            if volume['VolumeType'] == 'gp2' and volume['State'] == 'in-use':
                self.warning.append(Warning(volume['VolumeId'], self.region))

    def recommendations(self) -> list:
        ret: list = []
        for warning in self.warning:
            ret.append(f"EBS Volume {warning.resource_name} in region {warning.region} is gp2 type, upgrade it to gp3 to reduce the Cloud costs")
        return ret
