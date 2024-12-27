import asyncio
import aiohttp
import time
from locust import HttpUser, task, between

class ThreatIntelUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def get_threats(self):
        self.client.get("/threats", headers=self.auth_headers)
    
    @task(2)
    def analyze_threat(self):
        self.client.get(f"/analyze/{self.threat_id}", headers=self.auth_headers)

    def on_start(self):
        self.auth_headers = {"Authorization": f"Bearer {self.get_token()}"}
        self.threat_id = "test-threat-id"