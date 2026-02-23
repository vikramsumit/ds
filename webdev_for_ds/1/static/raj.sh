#!/usr/bin/env bash
set -e

echo "1️⃣  Blacklisting nouveau..."
sudo tee /etc/modprobe.d/blacklist-nouveau.conf <<EOL
blacklist nouveau
options nouveau modeset=0
EOL

echo "2️⃣  Updating initramfs..."
sudo update-initramfs -u

echo "3️⃣  Installing build dependencies..."
sudo apt update
sudo apt install -y linux-headers-$(uname -r) build-essential dkms

echo "4️⃣  Installing NVIDIA driver..."
sudo apt install -y nvidia-driver

echo "5️⃣  All set—rebooting now..."
sudo reboot
