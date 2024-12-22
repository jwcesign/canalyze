from rich.console import Console
from rich.table import Table
from rich.progress import track

from .. import interface
from .analyzer.eks_observability.analyzer import EKSObservabilityAnalyzer
from .analyzer.ebs_idle.analyzer import EBSIdleAnalyzer
from .analyzer.eip_idle.analyzer import EIPIdleAnalyzer
from .analyzer.eks_elb_duplicate.analyzer import EKSELBDuplicateAnalyzer

class AWSCloudProviders(interface.CloudProvider):
    def __init__(self, region: str):
        self.analyzers = {
            EKSObservabilityAnalyzer(region),
            EBSIdleAnalyzer(region),
            EIPIdleAnalyzer(region),
            EKSELBDuplicateAnalyzer(region),
        }

    def analyze(self):
        ret = {}

        # add progress bar
        for analyzer in track(self.analyzers, description="Analyzing..."):
            analyzer.analyze()
            Warnings = analyzer.recommendations()
            if len(Warnings) == 0:
                continue
            ret[analyzer] = Warnings
        
        console = Console()
        console.print("Canalyze finished the analysis, please check the following:", style="bold green")

        table = Table(show_header=True, header_style="bold magenta", title_justify="center")
        table.add_column("Index", justify="center", style="dim")
        table.add_column("Analyzer", justify="left", style="dim")
        table.add_column("Fix Level", justify="left", style="bold yellow")
        table.add_column("Recommendation", justify="left", style="bold yellow")

        cnt = 0
        for ana in ret:
            for warning in ret[ana]:
                table.add_row(str(cnt), ana.name(), ana.fix_level(), warning)
        console.print(table)
