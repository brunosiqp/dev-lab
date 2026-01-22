import sys
from .env_file_loader import load_env_file
from .config_loader import load_and_validate
from .logger import setup_logger


def main():
    logger = setup_logger()

    load_env_file()

    schema = {
        "APP_PORT": int,
        "DEBUG": bool,
    }

    try:
        config = load_and_validate(
            required_keys=schema.keys(),
            schema=schema,
            defaults={"DEBUG": "false"}
        )
        logger.info("Configuration loaded successfully")
        logger.info(config)
    except Exception as exc:
        logger.error(str(exc))
        sys.exit(1)


if __name__ == "__main__":
    main()
