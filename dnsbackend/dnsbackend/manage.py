# import os
# from flask import Flask
from flask_script import Manager # , Shell
from app import create_app, db
# from app.models import IP_Table, Users, FT_Domain_Top_Daily, FT_Domain_Top_Weelkly, Domain_IP, Dm_Domain_IP

# from app import app

# app = Flask(__name__)
app = create_app()
manager = Manager(app)

# manager.add_command("server", Server())

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


# @manager.shell
# def make_shell_context():
#    return dict(app=app, db=db)
# manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
	from werkzeug.contrib.fixers import ProxyFix
	app.wsgi_app = ProxyFix(app.wsgi_app)
	# manager.run()
	app.run(threaded=True)