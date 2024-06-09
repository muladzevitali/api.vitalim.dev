import enum

import environ


class DeploymentEnvironment(enum.Enum):
    DEV = 'dev'
    PROD = 'prod'

    def __eq__(self, other):
        return self.value == other.value

    @classmethod
    def from_value(cls, value):
        if value.lower() == cls.DEV.value.lower():
            return DeploymentEnvironment.DEV

        if value.lower() == cls.PROD.value.lower():
            return DeploymentEnvironment.PROD

        raise ValueError('incorrect environment value provided, should be one of: dev|prod')


class APIVersionUrlEnum(str, enum.Enum):
    VERSION_1 = 'api/v1'
    VERSION_2 = 'api/v2'


env = environ.Env(
    ENV_PATH=(str, None),
    DJANGO_DEBUG=(bool, False),
    DJANGO_SECRET_KEY=(str, ''),
    DJANGO_ALLOWED_HOSTS=(list, []),
    DEPLOYMENT_ENV=(str, 'dev'),
    CSRF_TRUSTED_ORIGINS=(list, []),
    AUTHENTICATION_TOKEN_EXPIRES_AFTER_SECONDS=(int, 60 * 60 * 24 * 365),
    POSTGRES_HOST=(str, 'localhost'),
    POSTGRES_DB=(str, 'db'),
    POSTGRES_USER=(str, 'user'),
    POSTGRES_PASSWORD=(str, 'password'),
)

if env('ENV_PATH'):
    environ.Env.read_env(env('ENV_PATH'))
