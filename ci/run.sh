#!/usr/bin/env bash

set -e
set -x

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


export PATH="$HOME/miniconda/bin:$PATH"
echo "$HOME/miniconda/bin:$PATH"
export PYTHONPATH="$DIR/..:$PYTHONPATH"
export CABAL_APP_CONFIG="site.config.ci_test_app_config"
export CABEL_DB_CONFIG="site.config.ci_test_db_config"

# Skip tests if no .py file changed
# If git repo doesn't exist, then run tests anyway

# if [[ -e $DIR/../.git ]]; then
#     COUNT_PY_FILES=`git diff --name-status master | grep -E '^(A|M).+\.py$' | wc -l`
#     if [[ $COUNT_PY_FILES -eq 0 ]]; then
#         echo 'no py file changed, skip tests'
#         exit 0
#     fi
# else
#     echo 'no git repo, run tests anyway'
# fi


# Activate Python environment

source activate cabal


# Init DB

echo 'init db...'

$DIR/init_db.sh

echo 'init db...done'


# Run tests

py.test $DIR/../site/tests/
