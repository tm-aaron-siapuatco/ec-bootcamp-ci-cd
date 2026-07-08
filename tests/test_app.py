import pytest

from src.app import format_deploy_message, is_production, validate_environment


@pytest.mark.parametrize("env", ["dev", "staging", "production"])
def test_validate_environment_accepts_valid_names(env):
    assert validate_environment(env) == env


@pytest.mark.parametrize("env", ["", "prod", "local", "PRODUCTION"])
def test_validate_environment_rejects_invalid_names(env):
    with pytest.raises(ValueError, match="Invalid environment"):
        validate_environment(env)


@pytest.mark.parametrize(
    ("env", "version", "expected"),
    [
        ("dev", "1.0.0", "Deploying 1.0.0 to dev"),
        ("staging", "2.3.4", "Deploying 2.3.4 to staging"),
        ("production", "9.9.9", "Deploying 9.9.9 to production"),
    ],
)
def test_format_deploy_message(env, version, expected):
    assert format_deploy_message(env, version) == expected


def test_format_deploy_message_rejects_invalid_environment():
    with pytest.raises(ValueError, match="Invalid environment"):
        format_deploy_message("qa", "1.0.0")


@pytest.mark.parametrize(
    ("env", "expected"),
    [
        ("dev", False),
        ("staging", False),
        ("production", True),
    ],
)
def test_is_production(env, expected):
    assert is_production(env) is expected


def test_is_production_rejects_invalid_environment():
    with pytest.raises(ValueError, match="Invalid environment"):
        is_production("qa")
