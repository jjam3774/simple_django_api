# -*- mode: ruby -*-
# vi: set ft=ruby :
# VAGRANTFILE_API_VERSION = "2"
REQUIRED_PLUGINS        = %w(ansible_local)

Vagrant.configure(2) do |config|
  config.vm.box = "alphaegg/minikube"
  config.vm.synced_folder ".", "/vagrant"
  config.vm.provision 'shell', keep_color: true, inline: <<-SHELL
    apt-get clean
    apt-get update
  SHELL
  # Ansible provisioner.
  config.vm.provision "ansible_local" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.playbook = "provisioning/playbook.yml"
    ansible.become = true
  end
  
  config.vm.define "servicea" do |service_a|
    service_a.vm.network :forwarded_port, guest: 8000, host: 8000, auto_correct: true
    service_a.vm.hostname = "ServiceA"
  end
end