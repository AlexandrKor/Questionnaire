from flask_script import Manager

from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from qs.app import app
from qs.extensions import db


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
