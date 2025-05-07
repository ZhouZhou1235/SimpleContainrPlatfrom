import core.machine as Machine
import core.config as Config
import core.DataModels as DataModels
import sys

try:
    machine = Machine.createFlask()
    machine.config.from_object(Config.SystemConfig)
    DataModels.db.init_app(machine)
    Machine.initDatabase(machine)

except Exception as e: print(e)
sys.exit()
