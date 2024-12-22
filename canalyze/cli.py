from opts import opts
from cloudproviders import provider

def main():
    parser = opts.new_optsp_arser()
    args = parser.parse_args()
    cloud_provider = provider.NewCloudProvider(args.provider, args.region)
    cloud_provider.analyze()

if __name__ == "__main__":
    main()