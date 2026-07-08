"""Small client-config helpers for the Lecture 5 CI/CD demo."""

VALID_ENVIRONMENTS = frozenset({"dev", "staging", "production"})


def validate_environment(name: str) -> str:
    """Return the environment name if valid, otherwise raise ValueError."""
    if name not in VALID_ENVIRONMENTS:
        raise ValueError(f"Invalid environment: {name}")
    return name


def format_deploy_message(env: str, version: str) -> str:
    """Return a deploy log line for the given environment and version."""
    validate_environment(env)
    return f"Deploying {version} to {env}"


def is_production(env: str) -> bool:
    """Return True when the environment is production."""
    validate_environment(env)
    return env == "production"
