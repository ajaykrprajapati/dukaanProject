import enum


class AppEnvironment(enum.Enum):
    PRODUCTION = "Production"
    STAGING = "Staging"
    DEVELOPMENT = "Development"
    TESTING = "Testing"
    LOCAL = "Local"
