# coding: utf-8
import os

__all__ = ['AppConfig', 'DBConfig']

# for app config
app_config_module_path = os.environ.get('CABAL_APP_CONFIG', '')
if not app_config_module_path:
    raise Exception('No CABAL_APP_CONFIG in os environ')
app_config_module = __import__(app_config_module_path, fromlist=['Config'])

AppConfig = app_config_module.Config

# for db config
db_config_module_path = os.environ.get('CABAL_DB_CONFIG', '')
if not db_config_module_path:
    raise Exception('No CABAL_DB_CONFIG in os environ')
db_config_module = __import__(db_config_module_path, fromlist=['Config'])

DBConfig = db_config_module.Config
