# 服务机器

import datetime,bcrypt,re,random
import core.tools as Tools
import core.config as Config
from flask import Flask,request,session,jsonify
from sqlalchemy import text
from core.DataModels import Admin, Cargo, Company, Container, ContainerRegister, User,db

def createFlask(): return Flask(__name__)

def setFlaskErrorHander(machine:Flask):
    errorList = [
        {
            'code':403,
            'content':'服务器拒绝响应'
        },
        {
            'code':404,
            'content':'资源未找到'
        },
        {
            'code':500,
            'content':'服务器出错'
        }
    ]
    for i in errorList:
        code = i['code']
        content = i['content']
        @machine.errorhandler(code)
        def f(error): return f'PINKCANDY: {content} <br> \n Flask: {error}'

def initDatabase(machine:Flask):
    with machine.app_context():
        db.session.execute(text(Tools.getFromFile(Config.initDatabaseSQL)))
        db.session.commit()

def work_register():
    username :str = request.form.get('username')
    password :str = request.form.get('password')
    name = request.form.get('name')
    info = request.form.get('info')
    type = request.form.get('type')
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    result = User.query.filter_by(username=username).all()
    passwordhash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
    user = User(
        username = username,
        passwordhash = passwordhash,
        name = name,
        info = info,
        type = type
    )
    if username==None or password==None: return 0
    if len(username)>20 or len(password)>20: return 0
    if re.match(pattern,username)==None or re.match(pattern,password)==None: return 0
    if len(result)>0: return 0
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    session['username'] = username
    return 1

def work_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username==None or password==None: return 0
    result = User.query.filter_by(username=username).all()
    if len(result)==0: return 0
    passwordhash :str = result[0].passwordhash
    if bcrypt.checkpw(password.encode(),passwordhash.encode())==False: return 0
    session['username'] = username
    return 1

def work_adminRegister(admin,password,name,info):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    result = Admin.query.filter_by(admin=admin).all()
    passwordhash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
    theAdmin = Admin(
        admin = admin,
        passwordhash = passwordhash,
        name = name,
        info = info,
    )
    if admin==None or password==None: return 0
    if len(admin)>20 or len(password)>20: return 0
    if re.match(pattern,admin)==None or re.match(pattern,password)==None: return 0
    if len(result)>0: return 0
    try:
        db.session.add(theAdmin)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_adminLogin():
    admin = request.form.get('admin')
    password = request.form.get('password')
    if admin=='' or password=='': return 0
    result = Admin.query.filter_by(admin=admin).all()
    if len(result)==0: return 0
    passwordhash :str = result[0].passwordhash
    if bcrypt.checkpw(password.encode(),passwordhash.encode())==False: return 0
    session['admin'] = admin
    return 1

def work_logout(): session.clear()

def work_getUser():
    username = request.args.get('username')
    if username=='': username=session['username']
    result = User.query.filter_by(username=username).all()
    if len(result)==0: return None
    res = jsonify({'data':[i.getData() for i in result],'info':'work_getUser'})
    return res

def work_getUsers():
    result = User.query.order_by(User.id).paginate(page=1,per_page=Config.queryPageLimit).items
    if len(result)==0: return None
    res = jsonify({'data':[i.getData() for i in result],'info':'work_getUsers'})
    return res

def work_getAdmin():
    if session.get('admin')==None: return None
    admin = session.get('admin')
    result = Admin.query.filter_by(admin=admin).all()
    if len(result)==0: return None
    res = jsonify({'data':[i.getData() for i in result],'info':'work_getAdmin'})
    return res

def work_getAdmins():
    result = Admin.query.order_by(Admin.id).paginate(page=1,per_page=Config.queryPageLimit).items
    if len(result)==0: return None
    res = jsonify({'data':[i.getData() for i in result],'info':'work_getAdmins'})
    return res

def work_getCargos():
    result = Cargo.query.order_by(Cargo.id).paginate(page=1,per_page=Config.queryPageLimit).items
    if len(result)==0: return None
    res = jsonify({'data':[i.getDict for i in result],'info':'work_getCargos'})
    return res

def work_getCompanys():
    result = Company.query.order_by(Company.id).paginate(page=1,per_page=Config.queryPageLimit).items
    if len(result)==0: return None
    res = jsonify({'data':[i.getDict for i in result],'info':'work_getCompanys'})
    return res

def work_getContainerRegister(containerid):
    return ContainerRegister.query.filter_by(containerid=containerid).all()[0]

def work_getContainerByUsername():
    username = request.args.get('username')
    if not username:
        if Tools.haveLogin(): username=session['username']
    if not username: return None
    result = Container.query.filter_by(username=username).all()
    if len(result)==0: return None
    dataList = [i.getDict for i in result]
    for i in dataList:
        cr = work_getContainerRegister(i['containerid'])
        i['entertime'] = cr.entertime
        i['exittime'] = cr.exittime
    res = jsonify({'data':dataList,'info':'work_getContainerByUsername'})
    return res

def work_getContainers():
    result = Container.query.order_by(Container.id).paginate(page=1,per_page=Config.queryPageLimit).items
    if len(result)==0: return None
    dataList = [i.getDict for i in result]
    for i in dataList:
        cr = work_getContainerRegister(i['containerid'])
        i['entertime'] = cr.entertime
        i['exittime'] = cr.exittime
    res = jsonify({'data':dataList,'info':'work_getContainers'})
    return res

def work_getContainerRegisters():
    result = ContainerRegister.query.order_by(ContainerRegister.id).paginate(page=1,per_page=Config.queryPageLimit).items
    if len(result)==0: return None
    res = jsonify({'data':[i.getDict for i in result],'info':'work_getContainerRegisters'})
    return res

def work_addCargo(containerid='',title='',content='',num=0):
    cargoid = random.randint(100000000,1000000000)
    cargo = Cargo(
        cargoid=cargoid,
        containerid=containerid,
        title=title,
        content=content,
        num=num,
    )
    try:
        db.session.add(cargo)
    except Exception as e:
        print(e)
        return 0
    return 1

def work_addContainer():
    companyid = request.form.get('companyid')
    title = request.form.get('title')
    info = request.form.get('info')
    cargoText = request.form.get('cargoText')
    if title=='': return 0
    if Tools.haveLogin()==0: return 0
    containerid = str(random.randint(100000000,1000000000))
    try:
        db.session.add(Container(
            containerid=containerid,
            companyid=companyid,
            username=session['username'],
            title=title,
            info=info,
        ))
        print('db.session.add(Container(')
    except Exception as e:
        print(e)
        return 0
    try:
        db.session.add(ContainerRegister(
            containerid=containerid,
        ))
    except Exception as e:
        print(e)
        return 0
    cargoList = cargoText.split('\n')
    for i in cargoList:
        try:
            tmpList = i.split(' ')
            title :str = tmpList[0]
            num :int = int(tmpList[1])
            print('tmpList = i.split(' ')')
        except Exception as e:
            print(e)
            continue
        work_addCargo(containerid,title,'',num)
    try:
        db.session.commit()
        print('commit')
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_addCompany():
    name = request.form.get('name')
    info = request.form.get('info')
    companyid = random.randint(10000,100000)
    try:
        db.session.add(Company(
            companyid=companyid,
            name=name,
            info=info,
        ))
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_containerExit():
    if Tools.haveLogin()==0: return 0
    containerid = request.form.get('containerid')
    if not containerid: return 0
    username = session['username']
    result = Container.query.filter_by(containerid=containerid,username=username).all()
    if len(result)==0: return 0
    record = ContainerRegister.query.get(result[0].id)
    record.exittime = datetime.datetime.now()
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_getContainerFull(containerid):
    try:
        containerList = Container.query.filter_by(containerid=containerid).all()
        containerRegisterList = ContainerRegister.query.filter_by(containerid=containerid).all()
        cargoList = Cargo.query.filter_by(containerid=containerid).all()
        userList = User.query.filter_by(username=containerList[0].username).all()
        companyid = containerList[0].companyid
        theCompany = None
        if companyid:
            companyList = Company.query.filter_by(companyid=companyid).all()
            theCompany = [i.getDict for i in companyList][0]
        resultDict = {
            'container':[i.getDict for i in containerList][0],
            'containerRegister':[i.getDict for i in containerRegisterList][0],
            'cargo':[i.getDict for i in cargoList],
            'user':[i.getData() for i in userList][0],
            'company': theCompany,
        }
        return jsonify(resultDict)
    except Exception as e:
        print(e)
        return None

def work_updateContainer():
    containerid = request.form.get('containerid')
    title = request.form.get('title')
    info = request.form.get('info')
    if not containerid or not title: return 0
    if not session.get('admin'): return 0
    try:
        key = Container.query.filter_by(containerid=containerid).all()[0].id
        record = Container.query.get(key)
        record.title = title
        record.info = info
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_updateCompany():
    companyid = request.form.get('companyid')
    name = request.form.get('name')
    info = request.form.get('info')
    if not companyid or not name: return 0
    if not session.get('admin'): return 0
    try:
        key = Company.query.filter_by(companyid=companyid).all()[0].id
        record = Company.query.get(key)
        record.name = name
        record.info = info
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_updateUser():
    username = request.form.get('username')
    name = request.form.get('name')
    info = request.form.get('info')
    type = request.form.get('type')
    if not username or not name: return 0
    if not session.get('admin'): return 0
    try:
        key = User.query.filter_by(username=username).all()[0].id
        record = User.query.get(key)
        record.name = name
        record.info = info
        record.type = type
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_deleteContainer():
    containerid = request.form.get('containerid')
    if not containerid: return 0
    if not session.get('admin'): return 0
    try:
        key = Container.query.filter_by(containerid=containerid).all()[0].id
        record = Container.query.get(key)
        db.session.delete(record)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_deleteCompany():
    companyid = request.form.get('companyid')
    if not companyid: return 0
    if not session.get('admin'): return 0
    try:
        key = Company.query.filter_by(companyid=companyid).all()[0].id
        record = Company.query.get(key)
        db.session.delete(record)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1

def work_deleteUser():
    username = request.form.get('username')
    if not username: return 0
    if not session.get('admin'): return 0
    try:
        key = User.query.filter_by(username=username).all()[0].id
        record = User.query.get(key)
        db.session.delete(record)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 0
    return 1
