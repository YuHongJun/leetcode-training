Type vagrant status
This command will show you the current status of the virtual machine. It should currently read “default running (virtualbox)” along with some other information.
Type vagrant suspend
This command suspends your virtual machine. All of your work is saved and the machine is put into a “sleep mode” of sorts. The machines state is saved and it’s very quick to stop and start your work. You should use this command if you plan to just take a short break from your work but don’t want to leave the virtual machine running.
Type vagrant up
This gets your virtual machine up and running again. Notice we didn’t have to redownload the virtual machine image, since it’s already been downloaded.
Type vagrant ssh
This command will actually connect to and log you into your virtual machine. Once done you will see a few lines of text showing various performance statistics of the virtual machine along with a new command line prompt that reads vagrant@vagrant-ubuntu-trusty-64:~$
Here are a few other important commands that we’ll discuss but you do not need to practice at this time:

vagrant halt
This command halts your virtual machine. All of your work is saved and the machine is turned off - think of this as “turning the power off”. It’s much slower to stop and start your virtual machine using this command, but it does free up all of your RAM once the machine has been stopped. You should use this command if you plan to take an extended break from your work, like when you are done for the day. The command vagrant up will turn your machine back on and you can continue your work.
vagrant destroy
This command destroys your virtual machine. Your work is not saved, the machine is turned off and forgotten about for the most part. Think of this as formatting the hard drive of a computer. You can always use vagrant up to relaunch the machine but you’ll be left with the baseline Linux installation from the beginning of this course. You should not have to use this command at any time during this course unless, at some point in time, you perform a task on the virtual machine that makes it completely inoperable.

```
pwd
ls -al

ls -al /home/ubuntu/.ssh

cat /etc/apt/sources.list 资源ubuntu列表

sudo apt-get update  检查是否最新软件

sudo apt-get upgrade  可更新软件列表

man apt-get   可执行命令列表

sudo apt-get autoremove  自动删除

sudo apt-get install finger

packages.ubuntu.com 安装包名字搜索

Apache Http Server=> apache2

PostgreSQL=> postgresql

Memcache=> memcached

finger

finger vagrant

cat /etc/passwd

sudo adduser student  创建用户

ssh student@127.0.0.1 -p 2222 新命令行 用新用户连接ssh。会提示没有权限

去root账号 vagrant 添加权限

vagrant$: sudo cat /etc/sudoers
vagrant$: sudo ls /etc/sudoers.d
vagrant$: sudo cp /etc/sudoers.d/vagrant /etc/sudoers.d/student
vagrant$: sudo nano /etc/sudoers.d/student

vagrant$: sudo passwd -e student 强制学士在下次登录时 重置自己的密码


```


