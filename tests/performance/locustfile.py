from locust import HttpUser, task, between
import json

class ThreatAPIUser(HttpUser):
    wait_time = between(1, 2.5)

    def on_start(self):
        response = self.client.post("/token", {
            "username": "test_user",
            "password": "test_pass"
        })
        self.token = response.json()["access_token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    @task(3)
    def view_threats(self):
        self.client.get("/threats", headers=self.headers)

    @task(2)
    def analyze_threat(self):
        self.client.get("/analyze/random_id", headers=self.headers)

    @task(1)
    def predict_threats(self):
        self.client.post("/predict", headers=self.headers)
