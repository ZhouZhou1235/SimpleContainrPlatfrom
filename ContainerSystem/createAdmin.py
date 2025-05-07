import core.machine as Machine
import core.machine as Machine
import core.config as Config
import core.DataModels as DataModels
import sys

try:
    machine = Machine.createFlask()
    machine.config.from_object(Config.SystemConfig)
    DataModels.db.init_app(machine)
    with machine.app_context():
        print('PINKCANDY: creating an admin...')
        admin = input('admin:')
        password = input('password:')
        name = input('name:')
        info = input('info:')
        x = Machine.work_adminRegister(admin,password,name,info)
        print(f'admin {admin} password {password} x {x}')
except Exception as e: print(e)
sys.exit()
