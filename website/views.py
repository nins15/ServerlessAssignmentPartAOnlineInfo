from flask import render_template, Blueprint

from website import db

views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def your_view():
    mycursor=db.cursor()
    mycursor.execute("SELECT email FROM LoginInfo where status='online';")

    your_list = mycursor.fetchall()
    print(your_list)
    return render_template('List.html', your_list=your_list)

