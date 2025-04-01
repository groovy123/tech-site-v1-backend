import os
import uvicorn

# uvicornログ設定
custom_logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s %(levelprefix)s %(message)s",
            "use_colors": True,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
        },
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
        # Additional handlers for file logging, etc.
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.access": {"handlers": ["default"], "level": "INFO", "propagate": False},
    },
}

def main():
    env = os.environ.get("ENV", "development")
    if (env == "development"):
        uvicorn.run(
                "app.main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                log_level="info",
                log_config=custom_logging_config,
            )
    else:
        raise Exception("not set environment.")
    pass

if __name__ == "__main__":
    main()
