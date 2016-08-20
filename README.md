# Cabal
Cabal is a system that enables every one to use my shadowsocks service.

## Continuous Integration
[![Build Status](https://travis-ci.org/gzxultra/cabal.svg?branch=master)](https://travis-ci.org/gzxultra/cabal)

## Prerequisition
git ruby foreman python-2.7 pre-commit

## Deloyment

1) install conda
```bash
for OS X:
brew install conda
wget https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
bash Miniconda2-latest-MacOSX-x86_64.sh

for Linux:
apt-get install conda
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-MacOSX-x86_64.sh
```

2) clone source
```bash
git clone https://github.com/gzxultra/cabal.git
conda env create -f cabal/environment.yml
source activate cabal
```

3) run app via foreman Procfile
```bash
cd cabal
forman s
```
