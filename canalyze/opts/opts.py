import argparse

def new_optsp_arser():
    parser = argparse.ArgumentParser(description="A cloud analysis tool designed to identify opportunities for cost savings in your cloud infrastructure.")
    parser.add_argument('--provider', type=str, default='aws', help='cloud provider to scan', required=True)
    parser.add_argument('--region', type=str, default='us-east-2', help='cloud provider region to scan', required=False)
    return parser
    