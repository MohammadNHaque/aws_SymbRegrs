#!/bin/sh

# --- Update Ubuntu Distro and Install Python
sudo apt-get update
sudo apt-get -y install python3
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo apt-get -y install python3-pip

#--- Install symreg
pip install symreg

#--- install gplearn
pip install gplearn

#--- install pysr

# Step 1 — Downloading and Installing Julia
cd ~/
wget https://julialang-s3.julialang.org/bin/linux/x64/1.8/julia-1.8.5-linux-x86_64.tar.gz
tar -xvzf julia-1.8.5-linux-x86_64.tar.gz
sudo mv julia-1.8.5/ /opt/
sudo ln -s /opt/julia-1.8.5/bin/julia /usr/local/bin/julia


# Install PySR
pip install -U pysr
python -c 'import pysr; pysr.install()'

