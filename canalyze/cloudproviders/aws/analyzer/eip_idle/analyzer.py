import boto3

from ..warning import Warning

class EIPIdleAnalyzer:
    warning: list = []
    def __init__(self, region: str):
        self.client = boto3.client('ec2', region_name=region)
        self.region = region

    def name(self):
        return "EIPIdle"

    def fix_level(self):
        return "easy"

    def analyze(self):
        eips = self.client.describe_addresses()
        for eip in eips['Addresses']:
            if eip.get('AssociationId') is not None:
                continue
            self.warning.append(Warning(eip['PublicIp'], self.region))

    def recommendations(self) -> list:
        ret: list = []
        for warning in self.warning:
            ret.append(f"EIP {warning.resource_name} in region {warning.region} is idle, delete it to reduce the Cloud costs")
        return ret
       