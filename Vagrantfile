# -*- mode: ruby -*-
# vi: set ft=ruby :
# VAGRANTFILE_API_VERSION = "2"
REQUIRED_PLUGINS        = %w(ansible_local)

Vagrant.configure(2) do |config|
  config.vm.provider :virtualbox do |vb|
    vb.gui = true
  end
  config.vm.box = "mrvantage/centos7-minikube"
  config.vm.synced_folder ".", "/vagrant"
  config.vm.provision 'shell', keep_color: true, inline: <<-SHELL
    which kubectl
    which docker
    yum install -y python3 python3-pip
    mv /usr/bin/python /usr/bin/python-old
    ln -s /usr/bin/python3 /usr/bin/python
    python -V
  SHELL
  # Ansible provisioner.
  config.vm.provision "ansible_local" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.playbook = "provisioning/playbook.yml"
    ansible.become = true
  end

  #config.vm.hostname = "rails"
  config.vm.define "servicea" do |service_a|
    service_a.vm.network :forwarded_port, guest: 8000, host: 8000, auto_correct: true
    service_a.vm.hostname = "ServiceA"
  end
end
