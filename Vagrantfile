
Vagrant.configure("2") do |config|

    config.vm.box = "debian/bullseye64"
    config.vm.provision "shell", path: "provision.sh" 
    config.vm.hostname = "VM-Delivery"
  
    config.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
  
    config.vm.network "forwarded_port", guest: 80, host: 80
    config.vm.network "forwarded_port", guest: 443, host: 443
    config.vm.network "forwarded_port", guest: 8080, host: 8080
  
    config.vm.synced_folder "./sources", "/projeto"
  
  
  end
  