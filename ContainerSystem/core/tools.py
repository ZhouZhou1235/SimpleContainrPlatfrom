# 工具

from flask import session

def getFromFile(path):
    with open(path,'r',encoding='UTF-8') as f: s=f.read()
    return s

def haveLogin():
    if session.get('username')!=None: return 1
    else: return 0
