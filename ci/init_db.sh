#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


DATABASE_NAME="cabal_test_$USER"

mysql -uroot -hlocalhost -e "DROP DATABASE IF EXISTS $DATABASE_NAME;"
mysql -uroot -hlocalhost -e "CREATE DATABASE $DATABASE_NAME CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
mysql -uroot -hlocalhost -e "GRANT ALL PRIVILEGES ON $DATABASE_NAME.* to super@'%' IDENTIFIED BY 'super@gzxultra.xyz';"
mysql -uroot -hlocalhost $DATABASE_NAME < $DIR/tables.sql
