class ConfigError(Exception):
    """Base configuration error."""


class ValidationError(ConfigError):
    """Raised when configuration validation fails."""
