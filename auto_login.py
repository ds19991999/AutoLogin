#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import os
from rich import print
from rich.markdown import Markdown


CLEAR = "cls" if os.name == "nt" else "clear"
SERVER_PWD = ""
SERVER_USER = ["root"]
IP_PRE = ["115.13.74.213", "153.86.118.134"]


DEPLOY_DOC = Markdown("""
# 📝部署教程

> 直接运行 `server` 即可启动工具

* 安装 `JupyterLab`: https://github.com/mesondzh/internet-memory-backup/blob/main/post/jekyll/2018-11-03-build-jupyterlab-server.md

```shell
jupyter lab --generate-config
jupyter lab password
from notebook.auth import passwd
passwd()
```

* 配置 `JupyterLab` 终端 `Shell`: https://github.com/jupyter/notebook/blob/d145301b5583366fc0c5e938ded80f07a0bc1bbf/notebook/terminal/__init__.py#L21-L23

* 检查 `Jupyter` 内核

```shell
jupyter kernelspec list
jupyter kernelspec remove <kernel_name> 
```

* `WSL` 安装 `sshpass` 并配置脚本环境变量

```shell
sudo apt-get install sshpass
vi /etc/profile
export PATH="/home/debian/app:$PATH"
source /etc/profile
sudo mv auto_login.py ~/app/server & chmod +x -R ~/app/server
```

* 常用命令

```shell
/etc/init.d/ssh restart
```
""")

CMD_HELP = """
[bold yellow]🎉🎉🎉欢迎进入 [bold green]AutoLogin[/bold green] v0.01[/bold yellow]

[bold green]help)[/bold green] 查看帮助 | h
[bold green]ssh)[/bold green] 登录节点 | login
[bold green]list)[/bold green] 节点列表
[bold green]deploy)[/bold green] 部署教程
[bold green]exit)[/bold green] 退出系统 | q | Ctrc+C

----------------------------------------------------------------
"""


def print_menu():
    print(CMD_HELP)


class AutoLogin(object):
    def __init__(self):
        self.SERVER_PWD = SERVER_PWD
        self.SERVER_USER = SERVER_USER
        self.IP_PRE = list(map(lambda x: ".".join(x.split(".")[:-1]) + ".", IP_PRE))

    def __login(self, ip, user, password):
        hidden = "*"*6
        print("--------------------------------------------------------------------------")
        print("[bold yellow]>>> 尝试登录节点：IP={} USER={} PASSWORD={}[/bold yellow]".format(ip, hidden, hidden))
        cmd = "sshpass -p {} ssh {}@{} -q -o StrictHostKeyChecking=no".format(password, user, ip)
        result = os.system(cmd)
        return result

    def _pre_login(self, ip):
        for user in self.SERVER_USER:
            result = result = self.__login(ip, user, self.SERVER_PWD)
            if result == 0:
                return result
        return result

    def login(self, input_ip):
        self.dot_count = input_ip.count(".")
        if (self.dot_count == 0):
            for _ip in self.IP_PRE:
                ip = _ip + input_ip
                result = self._pre_login(ip)
                if result == 0:
                    return
        if (self.dot_count == 1):
            for _ip in self.IP_PRE:
                if input_ip.split(".")[0] in _ip:
                    index = self.IP_PRE.index(_ip)
                    ip = self.IP_PRE[index] + input_ip.split(".")[-1]
                    result = self._pre_login(ip)
                    if result == 0:
                        return
        elif (self.dot_count == 3):
            result = self._pre_login(input_ip)
            if result == 0:
                return


def main():
    server = AutoLogin()
    os.system(CLEAR)
    print_menu()
    while True:
        try:
            print("[bold cyan]>>> [/bold cyan]", end="")
            i = input().lower().strip()
            if i == "help" or i == "h":
                os.system(CLEAR)
                print_menu()
            elif i == "exit" or i == "q":
                os.system(CLEAR)
                os.system(exit())
            elif i == "deploy":
                os.system(CLEAR)
                print(DEPLOY_DOC)
            elif i == "list":
                print(IP_PRE) 
            elif i.startswith("ssh")or i.startswith("login"):
                ip = i.split(" ")[-1]
                print(ip)
                server.login(ip)
            else:
                os.system(i)
        except KeyboardInterrupt:
            os.system(CLEAR)
            os.system(exit())
        except Exception:
            print_menu()
            print("[bold red]❌内部错误![/bold red]")


if __name__ == "__main__":
    main()
