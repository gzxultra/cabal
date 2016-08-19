# cabal

cabal is a system that enables every one to use my shadowsocks service.

## Installation

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

3) run app
```bash
cd cabal/site
python runserver.py [port]
```
