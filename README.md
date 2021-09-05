# AutoLogin 自动登录服务器

[![GitHub stars](https://img.shields.io/github/stars/mesondzh/AutoLogin.svg?style=popout&label=Stars)](https://github.com/mesondzh/AutoLogin/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mesondzh/AutoLogin.svg?style=popout&label=Fork)](https://github.com/mesondzh/AutoLogin/fork)
[![GitHub issues](https://img.shields.io/github/issues/mesondzh/AutoLogin.svg)](https://github.com/mesondzh/AutoLogin/issues)
[![DUB](https://img.shields.io/dub/l/vibe-d.svg)](https://github.com/mesondzh/AutoLogin/blob/master/LICENSE)

* 无需输入一大串的 `ip` 和密码，交互式自动登录服务器节点，适用于开发测试环境，不易用于实际生产环境.

![](https://cdn.jsdelivr.net/gh/ds19991999/image/picgo/20210905121239.gif)

## 脚本部署

```shell
git clone -b main https://github.com/mesondzh/AutoLogin.git
cd AutoLogin
sudo apt-get install sshpass
python3 -m pip install rich

# 修改 auto_login.py 中的SERVER_PWD、SERVER_USER、IP_PRE
# 添加环境变量，以/home/$USER/app为例
vi /etc/profile
export PATH="/home/$USER/app:$PATH"                                                   
source /etc/profile

sudo mv auto_login.py ~/app/server & chmod +x -R ~/app/server
```

## 菜单帮助

```shell
help) 查看帮助 | h
ssh) 登录节点 | login
list) 节点列表
deploy) 部署教程
exit) 退出系统 | q | Ctrc+C
```

## 配合 JupyterLab使用效果更佳

查看部署教程：`deploy`

![](https://cdn.jsdelivr.net/gh/ds19991999/image/picgo/20210905122020.png)

## Stargazers over time 

[![Stargazers over time](https://starchart.cc/mesondzh/AutoLogin.svg)](https://starchart.cc/mesondzh/AutoLogin) 

## LICENSE

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

