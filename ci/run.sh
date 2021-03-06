#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export PATH="$HOME/miniconda/bin:$PATH"
export PYTHONPATH="$HOME/miniconda/envs/cabal"

export CABAL_APP_CONFIG="config.test_app_config"
export CABAL_DB_CONFIG="config.test_db_config"



# Activate Python environment
echo 'activate cabal'
source activate cabal
echo 'activate cabal done!'


# Init DB

echo 'init db...'

$DIR/init_db.sh

echo 'init db...done'


# Run tests
# export PYTHONPATH="${PYTHONPATH}:$HOME/cabal/"
# echo $PYTHONPATH
py.test -x -vv -s $DIR/../site/tests/


# Clean up DB

echo 'clean up...'

mysql -uroot -hlocalhost -e "DROP DATABASE IF EXISTS cabal_test_$USER;"

echo 'clean up...done'
