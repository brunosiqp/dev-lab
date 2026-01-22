from src.config_loader import load_config

config = load_config(
    required_keys=["DB_HOST", "DB_USER"],
    defaults={"DB_HOST": "localhost"}
)

print(config)
