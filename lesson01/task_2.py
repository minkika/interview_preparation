"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    заполните далее

Пример:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]
"""

import os

def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    for item in os.listdir(sPath):
        full_name = os.path.join(os.path.abspath(sPath), item)
        if os.path.isfile(full_name):
            print(os.path.abspath(sPath), item)
        else:
            print_directory_contents(full_name)


print_directory_contents('/home/minkika/Learning/interview_preparation')

# Не знаю, как это работает для Windows. Мой листинг:
# minkika@minkika:~/Learning/interview_preparation/lesson01$ python3 task_2.py
# /home/minkika/Learning/interview_preparation README.md
# /home/minkika/Learning/interview_preparation/.git/logs/refs/remotes/origin HEAD
# /home/minkika/Learning/interview_preparation/.git/logs/refs/heads lesson01
# /home/minkika/Learning/interview_preparation/.git/logs/refs/heads master
# /home/minkika/Learning/interview_preparation/.git/logs HEAD
# /home/minkika/Learning/interview_preparation/.git/refs/remotes/origin HEAD
# /home/minkika/Learning/interview_preparation/.git/refs/heads lesson01
# /home/minkika/Learning/interview_preparation/.git/refs/heads master
# /home/minkika/Learning/interview_preparation/.git/info exclude
# /home/minkika/Learning/interview_preparation/.git packed-refs
# /home/minkika/Learning/interview_preparation/.git COMMIT_EDITMSG
# /home/minkika/Learning/interview_preparation/.git/objects/d8 8ca4160b8b135ac7f8982960b508881f788917
# /home/minkika/Learning/interview_preparation/.git/objects/5e cc132f4afae090120664119116751eb5d812fb
# /home/minkika/Learning/interview_preparation/.git/objects/90 ffb115ac30a72e7bb1efe1aa8c988f68a90fc8
# /home/minkika/Learning/interview_preparation/.git/objects/a4 abd12c9ca0f0464c9d4f4983ec80d3a101dedf
# /home/minkika/Learning/interview_preparation/.git/objects/d9 e7b0b5569de0d105d8c7e3213d95b39636d52e
# /home/minkika/Learning/interview_preparation/.git/objects/d9 a52422c7a2e81827259a816c06023fd78cefd1
# /home/minkika/Learning/interview_preparation/.git/objects/48 5dee64bcfb48793379b200a1afd14e85a8aaf4
# /home/minkika/Learning/interview_preparation/.git/objects/a5 f83a5ae88a02ec3eafce3ee83eccbab6ffd0bb
# /home/minkika/Learning/interview_preparation/.git/objects/15 fcf245b5b66dc0d95ec58236122810c851099b
# /home/minkika/Learning/interview_preparation/.git/objects/22 8aeba8ef60ef9573841835764e2013748f97b3
# /home/minkika/Learning/interview_preparation/.git/objects/pack pack-52848ff9d43be801d8e1ed9c07750eb0b78ef447.pack
# /home/minkika/Learning/interview_preparation/.git/objects/pack pack-52848ff9d43be801d8e1ed9c07750eb0b78ef447.idx
# /home/minkika/Learning/interview_preparation/.git/objects/16 0d7d775799533c4f468da05188b5683416ecd4
# /home/minkika/Learning/interview_preparation/.git/objects/ce effd16b7cd30e8cb0cd6d7b7325cd4717e8a7d
# /home/minkika/Learning/interview_preparation/.git/hooks pre-applypatch.sample
# /home/minkika/Learning/interview_preparation/.git/hooks pre-push.sample
# /home/minkika/Learning/interview_preparation/.git/hooks pre-merge-commit.sample
# /home/minkika/Learning/interview_preparation/.git/hooks prepare-commit-msg.sample
# /home/minkika/Learning/interview_preparation/.git/hooks pre-receive.sample
# /home/minkika/Learning/interview_preparation/.git/hooks fsmonitor-watchman.sample
# /home/minkika/Learning/interview_preparation/.git/hooks applypatch-msg.sample
# /home/minkika/Learning/interview_preparation/.git/hooks update.sample
# /home/minkika/Learning/interview_preparation/.git/hooks commit-msg.sample
# /home/minkika/Learning/interview_preparation/.git/hooks post-update.sample
# /home/minkika/Learning/interview_preparation/.git/hooks pre-rebase.sample
# /home/minkika/Learning/interview_preparation/.git/hooks pre-commit.sample
# /home/minkika/Learning/interview_preparation/.git index
# /home/minkika/Learning/interview_preparation/.git config
# /home/minkika/Learning/interview_preparation/.git description
# /home/minkika/Learning/interview_preparation/.git HEAD
# /home/minkika/Learning/interview_preparation/.idea vcs.xml
# /home/minkika/Learning/interview_preparation/.idea/inspectionProfiles profiles_settings.xml
# /home/minkika/Learning/interview_preparation/.idea .gitignore
# /home/minkika/Learning/interview_preparation/.idea interview_preparation.iml
# /home/minkika/Learning/interview_preparation/.idea workspace.xml
# /home/minkika/Learning/interview_preparation/.idea modules.xml
# /home/minkika/Learning/interview_preparation/.idea misc.xml
# /home/minkika/Learning/interview_preparation .gitignore
# /home/minkika/Learning/interview_preparation/lesson01 task_2.py
# /home/minkika/Learning/interview_preparation/lesson01 task_4.py
# /home/minkika/Learning/interview_preparation/lesson01 task_5.py
# /home/minkika/Learning/interview_preparation/lesson01 task_3.py
# /home/minkika/Learning/interview_preparation/lesson01 task_1.py
