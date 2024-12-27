from fastapi import APIRouter, BackgroundTasks
from core.threat_hunter import ThreatHunter
from integrations.siem import SIEMIntegration

router = APIRouter()
hunter = ThreatHunter()
siem = SIEMIntegration(config={})

@router.post("/hunt/{workflow}")
async def start_hunt(workflow: str, background_tasks: BackgroundTasks):
    results = await hunter.run_hunt(workflow)
    background_tasks.add_task(siem.push_alerts, results['alerts'])
    return {"status": "Hunt completed", "findings": results}

@router.get("/hunt/results/{hunt_id}")
async def get_hunt_results(hunt_id: str):
    return await siem.fetch_correlated_events(hunt_id)