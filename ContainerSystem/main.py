import core.machine as Machine
import core.router as Router
import core.DataModels as DataModels
from core.config import SystemConfig

# 初始化
machine = Machine.createFlask()
machine.config.from_object(SystemConfig)
Router.setMachineRoutes(machine)
Machine.setFlaskErrorHander(machine)
DataModels.db.init_app(machine)
print('PINKCANDY: init done')

# 开始
print('PINKCANDY: machine ready')
machine.run(host=SystemConfig.LISTEN_HOST,port=SystemConfig.RUNNING_PORT)
