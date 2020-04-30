from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role
from  flask_migrate import Migrate, MigrateCommand#import imgrate class and migrate command class

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


migrate = Migrate(app,db)#initialize migrate class
manager.add_command('db',MigrateCommand)#create new manager command 'db'

# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

#to create the shell context
@manager.shell
def make_shell_context():
    '''
    To allow us to pass properties into our shell
    '''
    return dict(app = app,db = db,User = User ,Role = Role )


if __name__ == '__main__':
    manager.run()