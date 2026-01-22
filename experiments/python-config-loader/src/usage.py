from src.config_loader import load_and_validate

schema = {
    "DB_HOST": str,
    "DB_PORT": int,
}

config = load_and_validate(
    required_keys=schema.keys(),
    schema=schema,
    defaults={"DB_PORT": "5432"}
)

print(config)
