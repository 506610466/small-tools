# pip install  python-gitlab
# pip3 install gitpython
# 首先要安装以上的库
import shutil
import stat

import gitlab
from git.repo import Repo
import os
import time

server_url = 'http://git.jshcbd.com.cn/'
project_name = 'liuyu/gitflow'  # 项目
branch = 'develop'  # 分支
private_token = 'qdkcao-58zwoDCup6sYn'  # 在这里获取  https://git.jshcbd.com.cn/-/profile/personal_access_tokens

s = 10  # 监听间隔时间  单位 秒
local_path = 'E:/git/source'  # 本地路径
target_path = 'E:/git/target'  # 目标路径
# ---------------------------------------------以上内容可以自定义-------------------------------------------------------
git_url = server_url + project_name + '.git'
# 创建客户端
client = gitlab.Gitlab(server_url, timeout=2, private_token=private_token)
# 发起认证
client.auth()
# 然后获取到project：
project = client.projects.get(project_name)


def remove_tree(path):
    while 1:
        try:
            shutil.rmtree(path)
        except PermissionError as e:
            err_file_path = str(e).split("\'", 2)[1]
            if os.path.exists(err_file_path):
                os.chmod(err_file_path, stat.S_IWUSR)
        except FileNotFoundError as e2:
            break


def move(local_dir, target_dir):
    remove_tree(target_dir)  # 先删除B目录下的所有内容
    shutil.copytree(local_dir, target_dir)
    remove_tree(target_dir + '/.git')


i = 0
while True:
    # 监听commits
    commits = project.commits.list(ref_name=branch)
    # for c in commits[:3]:
    #     print(c.id, c.committer_name, c.created_at, c.message)
    # 只在首次写入
    i = i + 1
    if i == 1:
        with open(os.path.dirname(local_path) + '/commit_id.txt', 'w', encoding='utf8') as f:
            f.write(commits[0].id)
            if not os.listdir(local_path):  # 如果目录为空，则进行 clone操作
                repo = Repo.clone_from(git_url, to_path=local_path, branch=branch)

    with open(os.path.dirname(local_path) + '/commit_id.txt', 'r', encoding='utf8') as f:
        old_id = f.read()
    print('持续监听中.....')
    if commits[0].id != old_id:
        print(f'监听到远程仓库改变！内容----->  Name：{commits[0].committer_name}  Message：{commits[0].message}')
        if not os.listdir(local_path):  # 如果目录为空，则进行 clone操作
            repo = Repo.clone_from(git_url, to_path=local_path, branch=branch)
        else:
            repo = Repo(local_path)
        # pull最新代码
        repo.git.pull()
        print("代码已更新到最新！")
        move(local_dir=local_path, target_dir=target_path)
        with open(os.path.dirname(local_path) + '/commit_id.txt', 'w', encoding='utf8') as f:
            f.write(commits[0].id)
    time.sleep(s)
