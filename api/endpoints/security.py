from fastapi import APIRouter, BackgroundTasks
from security.vulnerability_scanner import VulnerabilityScanner

router = APIRouter()
scanner = VulnerabilityScanner()

@router.post("/scan")
async def run_security_scan(background_tasks: BackgroundTasks):
    background_tasks.add_task(scanner.run_scan)
    return {"message": "Scan initiated"}

@router.get("/scan/results")
async def get_scan_results():
    return await scanner.get_latest_results()