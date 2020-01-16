# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
$script = <<-SCRIPT
sudo apt update
sudo apt install software-properties-common -y
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y

sudo su -c "useradd ansibleuser -m -s /bin/bash"
sudo su -c "usermod -aG sudo ansibleuser"
sudo echo 'ansibleuser ALL=(ALL) NOPASSWD:ALL' | sudo EDITOR='tee -a' visudo
sudo -u ansibleuser bash -c "cat /dev/zero | ssh-keygen -q -N ''"

sudo su - ansibleuser
cd /vagrant/
cp /home/ansibleuser/.ssh/id_rsa.pub .
sudo apt install python-pip --yes


cat << EOF > pyscript.py
#!/usr/bin/pip
pip install boto boto3 botocore  --upgrade
pip install awscli --upgrade --user
EOF
chmod 755 pyscript.py
sudo -u ansibleuser bash -c "./pyscript.py"

rm /etc/ansible/hosts
mkdir /etc/ansible/hosts
cp /vagrant/ec2.py /etc/ansible/hosts
cp /vagrant/ec2.ini /etc/ansible/hosts
sudo chmod +x /etc/ansible/hosts/ec2.py

SCRIPT

Vagrant.configure("2") do |config|

  config.vm.define "control" do |control|
    config.vm.box = "ubuntu/xenial64"
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
    end
    config.vm.hostname = "test"
    config.vm.network "forwarded_port", guest: 80, host: 8080
    config.vm.network "public_network", ip: "192.168.86.99", bridge: "en0: Wi-Fi (Wireless)"
    config.vm.network "private_network", ip: "192.168.33.10"
    config.vm.synced_folder ".", "/vagrant"
    config.vm.provision "shell", inline: $script
    #config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/my.pub"
  end 
end   


