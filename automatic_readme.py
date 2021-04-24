#!/usr/bin/python3
""" script that creates a readme
port via hipporead and uploads it
to the repo passing it a txt with
the urls and the path to the repository
"""
from fabric.api import local
hipporead='python2 /home/klich1984/Klich84/klich/README_AUTOMATICO/hipposcraper/hipporead.py'

def Readme():

    with open('readme_file.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            url = line.split(' ')[0]
            path = line.split(' ')[1]
            local("{} {}".format(hipporead, url))
            local("cp README.md /home/klich1984/holbeton/{}".format(path))
            path2 = line.split(' ')[1].split('/')
            local("cd /home/klich1984/holbeton/{}/{} && \
                    git add README.md &&\
                    git commit -m hola &&\
                    git push \
                    ".format(path2[0], path2[1]))
