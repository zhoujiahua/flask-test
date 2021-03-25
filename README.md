# Test Python

> 官方文档 [https://pipenv.pypa.io/en/latest/](https://pipenv.pypa.io/en/latest/)

> 基本使用 [https://www.cnblogs.com/blueberry-mint/p/13362737.html](https://www.cnblogs.com/blueberry-mint/p/13362737.html)

## Introduction

```
The current project is built using Python3 and flask frameworks.
Python.
The project virtual environment is managed using Pipenv.
Pipenv install.
```

## Pipenv install

```
pipenv --where
pipenv --venv
pipenv install
pipenv shell
pipenv graph
```

## Python反向生成requirements.txt

`pip freeze > requirements.txt`

## Pipenv Commands

```
check      Checks for security vulnerabilities and against PEP 508 markers
         provided in Pipfile.
clean      Uninstalls all packages not specified in Pipfile.lock.
graph      Displays currently–installed dependency graph information.
install    Installs provided packages and adds them to Pipfile, or (if no
         packages are given), installs all packages from Pipfile.
lock       Generates Pipfile.lock.
open       View a given module in your editor.
run        Spawns a command installed into the virtualenv.
scripts    Displays the shortcuts in the (optional) [scripts] section of
         Pipfile.
shell      Spawns a shell within the virtualenv.
sync       Installs all packages specified in Pipfile.lock.
uninstall  Un-installs a provided package and removes it from Pipfile.
```

> 虚拟环境

虚拟环境是用于依赖项管理和项目隔离的python工具，它可以将python程序和pip包管理工具安装在本地的隔离目录中（非全局安装）。

> Pipenv简介

pipenv发布于2017年1月，它是一种Python依赖管理工具，你可以把它看做是pip和virtualenv的组合体，它基于Pipfile的依赖记录方式，用于替代旧的记录方式requirements.txt。
pipenv会自动帮你管理虚拟环境和依赖文件，并且提供一系列命令和选项来帮助你实现各种依赖和环境管理相关的操作。简而言之，它更方便、完善和安全。

> 安装

`pip3 install pipenv`或`python3 -m pip install pipenv`
安装完成可以通过命令pipenv --version检测安装是否成功

> 创建环境

`pipenv install`

上述命令会生成Pipfile和Pipfile.lock，使用pipenv创建虚拟环境，自动生成一个随机的虚拟环境目录名。

如果在windows系统下执行命令，生成的虚拟环境在C:\Users\用户名\.virtualenvs文件夹下。

一般虚拟环境目录名的前缀是你创建环境时所在的项目目录名，如在myblog目录下执行命令，虚拟环境的目录名称就是myblog-Gtn4e1q9，后半部分为随机字符串。

> 激活虚拟环境

`pipenv shell`

创建环境后会自动进入到虚拟环境中，当退出虚拟环境重新进入到虚拟环境则需要执行以上命令。

> 安装依赖包到虚拟环境

`pipenv install requests`

不管是否激活虚拟环境，都可以执行pipenv install 库名来安装。

> 查看已安装的模块

`pipenv graph`

> 卸载已经安装的模块

`pipenv uninstall requests`

> 获取当前虚拟环境位置

`pipenv --venv`

> 寻找当前项目的根目录

`pipenv --where`

> 通过requirements.txt文件安装模块

`pipenv install -r requirements.txt`

> 总结

以上就是pipenv的简单说明和一些命令的基本使用，如果想了解更多pipenv的用法可以去pipenv官方文档中查阅。

