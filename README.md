# Cabal

Cabal is a system that enables every one to use my shadowsocks service.

## Continuous Integration
[![Build Status](https://travis-ci.org/gzxultra/cabal.svg?branch=master)](https://travis-ci.org/gzxultra/cabal)
[![Join the chat at https://gitter.im/the-cabal/Lobby](https://badges.gitter.im/the-cabal/Lobby.svg)](https://gitter.im/the-cabal/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Prerequisition
git ruby foreman python-2.7 pre-commit npm mysql

## Deloyment

1) install conda
```bash
for OS X:
wget https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
bash Miniconda2-latest-MacOSX-x86_64.sh

for Linux:
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh
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

**npm 3+ is recommended for a more efficient dependency tree.**

```bash
cd cabal/site
npm install
npm run dev
```


## Licese

Copyright 2016 夏天的风铃_ MechanicianW

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
