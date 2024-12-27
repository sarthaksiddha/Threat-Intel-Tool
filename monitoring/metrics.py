from prometheus_client import Counter, Histogram, Gauge

class MetricsCollector:
    def __init__(self):
        self.threat_counter = Counter(
            'threats_total',
            'Total number of threats detected',
            ['severity']
        )
        
        self.analysis_time = Histogram(
            'threat_analysis_seconds',
            'Time spent analyzing threats',
            buckets=(1, 5, 10, 30, 60, 120)
        )
        
        self.active_hunts = Gauge(
            'active_threat_hunts',
            'Number of active threat hunting operations'
        )

    def track_threat(self, severity: str):
        self.threat_counter.labels(severity=severity).inc()

    def track_analysis_time(self, duration: float):
        self.analysis_time.observe(duration)

    def set_active_hunts(self, count: int):
        self.active_hunts.set(count)