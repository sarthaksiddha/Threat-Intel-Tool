from fastapi import FastAPI
from core.logging_config import setup_logging
from core.error_handler import error_handler, ThreatIntelException
from monitoring.metrics import monitor_endpoint
from prometheus_client import make_asgi_app

app = FastAPI()
logger = setup_logging()
metrics_app = make_asgi_app()

app.mount("/metrics", metrics_app)
app.add_exception_handler(Exception, error_handler)

@app.get("/threats")
@monitor_endpoint
async def get_threats():
    try:
        threats = await collector.collect_feeds()
        logger.info(f"Retrieved {len(threats)} threats")
        return {"threats": threats}
    except Exception as e:
        logger.error(f"Error retrieving threats: {str(e)}")
        raise ThreatIntelException(message="Failed to retrieve threats")
