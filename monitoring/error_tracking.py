import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

class ErrorTracker:
    def __init__(self, dsn: str):
        sentry_sdk.init(
            dsn=dsn,
            integrations=[
                FastApiIntegration(),
            ],
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
        )

    def capture_exception(self, error: Exception, context: dict = None):
        with sentry_sdk.push_scope() as scope:
            if context:
                scope.set_context("additional", context)
            sentry_sdk.capture_exception(error)

    def capture_message(self, message: str, level="error"):
        sentry_sdk.capture_message(message, level=level)