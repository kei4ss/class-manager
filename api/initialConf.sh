#!/bin/bash

echo '***********************'
echo '--- ATUALIZANDO APT ---'
echo '***********************'
sudo apt update && sudo apt upgrade

echo '****************************************'
echo '--- ATUALIZANDO / INSTALANDO PYTHON3 ---'
echo '****************************************'
sudo upgrade python3 || sudo apt install python3 
sudo apt autoremove

echo '*************************'
echo '--- ADICIONANDO .VENV ---'
echo '*************************'
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt




