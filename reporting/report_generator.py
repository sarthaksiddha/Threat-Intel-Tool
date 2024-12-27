import jinja2
from datetime import datetime
from typing import Dict, List
import matplotlib.pyplot as plt
import pandas as pd

class ReportGenerator:
    def __init__(self):
        self.template_loader = jinja2.FileSystemLoader('templates')
        self.template_env = jinja2.Environment(loader=self.template_loader)

    async def generate_report(self, data: Dict, report_type: str) -> str:
        template = self.template_env.get_template(f'{report_type}.html')
        plots = self._generate_plots(data)
        stats = self._calculate_statistics(data)
        
        return template.render(
            timestamp=datetime.now(),
            data=data,
            plots=plots,
            statistics=stats
        )

    def _generate_plots(self, data: Dict) -> Dict:
        plots = {}
        if 'threats_over_time' in data:
            plots['trend'] = self._create_trend_plot(data['threats_over_time'])
        if 'severity_distribution' in data:
            plots['severity'] = self._create_severity_plot(data['severity_distribution'])
        return plots