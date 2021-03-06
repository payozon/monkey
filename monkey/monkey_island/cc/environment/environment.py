import json
import logging

from cc.environment import standard
from cc.environment import aws
from cc.environment import password

__author__ = 'itay.mizeretz'

logger = logging.getLogger(__name__)

AWS = 'aws'
STANDARD = 'standard'
PASSWORD = 'password'

ENV_DICT = {
    STANDARD: standard.StandardEnvironment,
    AWS: aws.AwsEnvironment,
    PASSWORD: password.PasswordEnvironment,
}


def load_server_configuration_from_file():
    with open('monkey_island/cc/server_config.json', 'r') as f:
        config_content = f.read()
    return json.loads(config_content)


def load_env_from_file():
    config_json = load_server_configuration_from_file()
    return config_json['server_config']

try:
    config_json = load_server_configuration_from_file()
    __env_type = config_json['server_config']
    env = ENV_DICT[__env_type]()
    env.set_config(config_json)
    logger.info('Monkey\'s env is: {0}'.format(env.__class__.__name__))
except Exception:
    logger.error('Failed initializing environment', exc_info=True)
    raise
