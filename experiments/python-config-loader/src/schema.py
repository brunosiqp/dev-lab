from .exceptions import ValidationError


def validate_schema(config: dict, schema: dict) -> None:
    for key, expected_type in schema.items():
        value = config.get(key)

        if value is None:
            raise ValidationError(f"Missing required config: {key}")

        try:
            config[key] = expected_type(value)
        except (TypeError, ValueError):
            raise ValidationError(
                f"Invalid type for {key}. Expected {expected_type.__name__}"
            )
