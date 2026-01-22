from dotenv import load_dotenv


def load_env_file(path: str = ".env") -> None:
    """
    Load environment variables from a .env file without
    overriding existing variables.
    """
    load_dotenv(dotenv_path=path, override=False)
