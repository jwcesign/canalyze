from .aws import aws
from . import interface

def NewCloudProvider(name: str, region: str) -> interface.CloudProvider:
    if name == "aws":
        return aws.AWSCloudProviders(region)
    else:
        return None
