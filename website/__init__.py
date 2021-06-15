from flask import Flask
import mysql.connector

db = mysql.connector.connect(host="127.0.0.1", user="root", password="Hanumann@1",
                             auth_plugin='mysql_native_password',database='testdatabase')

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='ninad'
    from .views import views
    app.register_blueprint(views,url_prefix='/')
    return app