from rich.console import Console
from rich.table import Table

from .. import interface
from .analyzer.eks_observability.analyzer import EKSObservabilityAnalyzer
from .analyzer.ebs_idle.analyzer import EBSIdleAnalyzer

class AWSCloudProviders(interface.CloudProvider):
    def __init__(self, region: str):
        self.analyzers = {
            EKSObservabilityAnalyzer(region),
            EBSIdleAnalyzer(region)
        }

    def analyze(self):
        ret = []
        for analyzer in self.analyzers:
            analyzer.analyze()
            Warnings = analyzer.warning
            if len(Warnings) == 0:
                continue
            ret.extend(analyzer.recommendations())
        
        console = Console()
        console.print("Canalyze finished the analysis, please check the following:", style="bold green")

        table = Table(show_header=True, header_style="bold magenta", title_justify="center")
        table.add_column("Index", justify="center", style="dim")
        table.add_column("Recommendation", justify="left", style="bold yellow")
        for recommendation in ret:
            table.add_row(str(ret.index(recommendation)), str(recommendation))
        console.print(table)