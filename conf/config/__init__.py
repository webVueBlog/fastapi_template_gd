

# @File    : __init__.py.py
# @Desc    : 配置载入


import os

from utils import Config

# 配置文件映射
CONF_NAME_MAPPER = {
    'base': 'conf.config.base',
    'local': 'conf.config.local',
    'test': 'conf.config.test',
    'prod': 'conf.config.prod',
    'ci': 'conf.config.ci',
}
# 读取.env文件
CONF_ENV = os.environ.get('CONF_MODULE')

config = Config()

# 载入配置
if not CONF_ENV:
    try:
        config.from_object(CONF_NAME_MAPPER['local'])
    except ModuleNotFoundError as e:
        exit(e)
else:
    try:
        config_name = CONF_NAME_MAPPER[CONF_ENV]
        config.from_object(config_name)
    except ModuleNotFoundError as e:
        exit(e)

__all__ = ['config']
