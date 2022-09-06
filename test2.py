import sentry_sdk
from loguru import logger

sentry_sdk.init(
    dsn="dsn",
    debug=True,

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

def main():
    1/0

if __name__ == "__main__":
    with logger.catch():
        main()