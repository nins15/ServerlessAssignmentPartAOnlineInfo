from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
import mysql.connector

from website import create_app

app=create_app()
if __name__ =='__main__':
    app.run(debug=True)

