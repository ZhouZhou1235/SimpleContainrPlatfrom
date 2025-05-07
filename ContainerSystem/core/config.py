# 配置

from datetime import timedelta

statichtmlUrl = 'static/html/'
initDatabaseSQL = 'static/sql/container_system_init.sql'
queryPageLimit = 1000

# SQLALCHEMY_DATABASE_URI = 'sqlite:///dbname.db' 使用SQLite
# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/dbname' 使用MySQL
class SystemConfig:
    # 数据库
    dbUsrname = 'container_system'
    dbPassword = '123456'
    host = 'localhost'
    dbname = 'container_system'
    SQLALCHEMY_DATABASE_URI = f'mysql://{dbUsrname}:{dbPassword}@{host}/{dbname}' # 数据库连接
    # SQLAlchemy 功能开关
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 追踪修改
    # SESSION设置
    SECRET_KEY = 'pinkcandy in flask' # 储存密钥
    PERMANENT_SESSION_LIFETIME = timedelta(days=7) # 有效时间
    # 启动
    LISTEN_HOST = '0.0.0.0'
    RUNNING_PORT = 8000
