from .base import *

env_name = os.getenv('ENV_NAME', 'local')

if env_name == 'pro':
    from .pro import *
else:
    from .local import *