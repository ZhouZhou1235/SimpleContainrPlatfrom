# 机器路由

from flask import Flask,request
import core.tools as Tools
import core.config as Config
import core.machine as Machine

def setMachineRoutes(machine:Flask):
    # 页面
    @machine.route('/')
    def home(): return Tools.getFromFile(Config.statichtmlUrl+'home.html')
    @machine.route('/register')
    def register(): return Tools.getFromFile(Config.statichtmlUrl+'register.html')
    @machine.route('/login')
    def login(): return Tools.getFromFile(Config.statichtmlUrl+'login.html')
    @machine.route('/adminLogin')
    def adminLogin(): return Tools.getFromFile(Config.statichtmlUrl+'adminLogin.html')
    # 动作
    # === POST
    @machine.route('/doRegister',methods=['post'])
    def doRegister(): return str(Machine.work_register())
    @machine.route('/dologin',methods=['post'])
    def dologin(): return str(Machine.work_login())
    @machine.route('/adminDologin',methods=['post'])
    def adminDologin(): return str(Machine.work_adminLogin())
    @machine.route('/logout',methods=['post'])
    def logout():
        Machine.work_logout()
        return "logout done"
    @machine.route('/checkLogin',methods=['post'])
    def checkLogin(): return str(Tools.haveLogin())
    @machine.route('/addContainer',methods=['post'])
    def addContainer(): return str(Machine.work_addContainer())
    @machine.route('/addCompany',methods=['post'])
    def addCompany(): return str(Machine.work_addCompany())
    @machine.route('/containerExit',methods=['post'])
    def containerExit(): return str(Machine.work_containerExit())
    @machine.route('/updateContainer',methods=['post'])
    def updateContainer(): return str(Machine.work_updateContainer())
    @machine.route('/updateCompany',methods=['post'])
    def updateCompany(): return str(Machine.work_updateCompany())
    @machine.route('/updateUser',methods=['post'])
    def updateUser(): return str(Machine.work_updateUser())
    @machine.route('/deleteContainer',methods=['post'])
    def deleteContainer(): return str(Machine.work_deleteContainer())
    @machine.route('/deleteCompany',methods=['post'])
    def deleteCompany(): return str(Machine.work_deleteCompany())
    @machine.route('/deleteUser',methods=['post'])
    def deleteUser(): return str(Machine.work_deleteUser())
    # === GET
    @machine.route('/getUser',methods=['get'])
    def getUser():
        res = Machine.work_getUser()
        if res!=None: return res
        return "no data"
    @machine.route('/getUsers',methods=['get'])
    def getUsers():
        res = Machine.work_getUsers()
        if res!=None: return res
        return "no data"
    @machine.route('/getContainers',methods=['get'])
    def getContainers():
        res = Machine.work_getContainers()
        if res!=None: return res
        return "no data"
    @machine.route('/getContainerByUsername',methods=['get'])
    def getContainerByUsername():
        res = Machine.work_getContainerByUsername()
        if res!=None: return res
        return "no data"
    @machine.route('/getAdmin',methods=['get'])
    def getAdmin():
        res = Machine.work_getAdmin()
        if res!=None: return res
        return "no data"
    @machine.route('/getContainerFull',methods=['get'])
    def getContainerFull():
        containerid = request.args.get('containerid')
        res = Machine.work_getContainerFull(containerid)
        if res!=None: return res
        return "no data"
    @machine.route('/getCompanys',methods=['get'])
    def getCompanys():
        res = Machine.work_getCompanys()
        if res!=None: return res
        return "no data"
