# Cabal

Cabal is a system that enables every one to use my shadowsocks service.

## Continuous Integration
[![Build Status](https://travis-ci.org/gzxultra/cabal.svg?branch=master)](https://travis-ci.org/gzxultra/cabal)
[![Join the chat at https://gitter.im/the-cabal/Lobby](https://badges.gitter.im/the-cabal/Lobby.svg)](https://gitter.im/the-cabal/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Prerequisition
git ruby foreman python-2.7 pre-commit npm

## Deloyment

1) install conda
```bash
for OS X:
wget https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
bash Miniconda2-latest-MacOSX-x86_64.sh

for Linux:
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-MacOSX-x86_64.sh
```

2) clone source
```bash
git clone https://github.com/gzxultra/cabal.git
cd cabal
conda env create -f environment.yml
source activate cabal
```

3) run app via honcho Procfile
```bash
cd cabal
honcho start
```

## Static Files Compiled

**It is recommended to use npm 3+ for a more efficient dependency tree.**

```bash
cd cabal/site
npm install
npm run dev
```
