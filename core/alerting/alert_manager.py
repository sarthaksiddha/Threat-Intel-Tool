from typing import List, Dict
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from slack_sdk import WebClient

class AlertManager:
    def __init__(self, config: Dict):
        self.email_config = config.get('email')
        self.slack_config = config.get('slack')
        self.slack = WebClient(token=self.slack_config['token']) if self.slack_config else None

    async def send_alert(self, alert: Dict):
        if self.email_config and alert['severity'] >= self.email_config['threshold']:
            await self._send_email_alert(alert)
        
        if self.slack_config:
            await self._send_slack_alert(alert)

    async def _send_email_alert(self, alert: Dict):
        msg = MIMEText(self._format_alert(alert))
        msg['Subject'] = f"[{alert['severity']}] New Security Alert"
        msg['From'] = self.email_config['from']
        msg['To'] = self.email_config['to']

        with smtplib.SMTP(self.email_config['smtp_host']) as server:
            server.send_message(msg)

    async def _send_slack_alert(self, alert: Dict):
        self.slack.chat_postMessage(
            channel=self.slack_config['channel'],
            text=self._format_alert(alert),
            blocks=self._format_slack_blocks(alert)
        )