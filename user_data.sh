#!/bin/bash
sudo -u ubuntu bash -c "cat /dev/zero | ssh-keygen -q -N ''"
sudo su -c "useradd ansibleuser -m -s /bin/bash"
sudo su -c "usermod -aG sudo ansibleuser"
sudo echo 'ansibleuser ALL=(ALL) NOPASSWD:ALL' | sudo EDITOR='tee -a' visudo
sudo su - ansibleuser
sudo cp -r home/ubuntu/.ssh/ /home/ansibleuser/
sudo chown -R ansibleuser /home/ansibleuser/.ssh
sudo apt update --yes
sudo apt install python --yes