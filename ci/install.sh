#!/usr/bin/env bash

set -e  # 若指令传回值不等于 0，则立即退出 shell

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


export PATH="$HOME/miniconda/bin:$PATH"
# Update environment if cache is available
if [[ -e $HOME/miniconda/bin/conda ]]; then
    conda env update -f $DIR/../environment.yml

# Otherwise, install conda and create environment
else
    wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -f -p $HOME/miniconda
    conda env create -f $DIR/../environment.yml
fi
