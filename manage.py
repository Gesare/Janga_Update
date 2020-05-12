import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

app = create_app(os.environ.get('CONFIG_OPTION'))

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()