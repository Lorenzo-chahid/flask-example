#/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import datetime
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_socketio import SocketIO, join_room



app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = "the random string"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///" + os.path.join(basedir, "database.db")
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
db.init_app(app)
db.app = app
db.create_all()




class Users(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    email = db.Column(db.Text(), nullable=True)
    posts = db.relationship('Posts', backref="users")


    def __repr__(self):
        return '<User {}>'.format(self.username)
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Posts(db.Model):
    __tablename__= "posts"
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.Text(),nullable=False )
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    users_id = db.Column(db.Text(), db.ForeignKey('users.username'))


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/login/", methods=["GET", "POST"])
def login():
    home = Users.query.all()
    if request.method == "POST":
        session.pop("user_id", None)
        password_check = request.form["password"]
        username = request.form["username"]
        password = Users.query.filter_by(password_hash=password_check).first()
        user = Users.query.filter_by(username=request.form["username"]).first()
        for el in home:
            if check_password_hash(user.password_hash, password_check)and user:
                error = False
                session["user_id"] = user.id
                return redirect(url_for("chat"))
            return render_template(("form.html"),error="Password or username invalid")
    return render_template("form.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    room = 1
    users = Users.query.all()
    posts = Posts.query.all()
    return render_template("chat.html", users=users,posts=posts, room=room)
 

@app.route("/profile/")
def profile():
    users = Users.query.all()
    posts = Posts.query.all()
    return render_template("profile.html", users=users, posts=posts)

@app.route("/testo")
def testoo():
    return render_template("testo.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = Users(username = uname, email = mail, password_hash = passw)
        register.set_password(passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("signup.html")





@socketio.on("send_message")
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {} : {}".format(data["username"], data["room"], data["message"]))
    socketio.emit("receive_message", data, room=data["room"])

@socketio.on("join_room")
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data["username"], data["room"]))
    join_room(data["room"])
    socketio.emit("join_room_announcement", data)


admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Posts, db.session))

if __name__ == '__main__':
    socketio.run(app, debug=True)
#/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import datetime
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_socketio import SocketIO, join_room



app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = "the random string"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///" + os.path.join(basedir, "database.db")
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
db.init_app(app)
db.app = app
db.create_all()




class Users(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    email = db.Column(db.Text(), nullable=True)
    posts = db.relationship('Posts', backref="users")


    def __repr__(self):
        return '<User {}>'.format(self.username)
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Posts(db.Model):
    __tablename__= "posts"
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.Text(),nullable=False )
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    users_id = db.Column(db.Text(), db.ForeignKey('users.username'))


@app.route("/")
def index():
    return render_template("index.html")




@app.route("/login/", methods=["GET", "POST"])
def login():
    home = Users.query.all()
    if request.method == "POST":
        session.pop("user_id", None)
        password_check = request.form["password"]
        username = request.form["username"]
        password = Users.query.filter_by(password_hash=password_check).first()
        user = Users.query.filter_by(username=request.form["username"]).first()
        for el in home:
            if check_password_hash(user.password_hash, password_check)and user:
                error = False
                session["user_id"] = user.id
                return redirect(url_for("chat"))
            return render_template(("form.html"),error="Password or username invalid")
    return render_template("form.html")


@app.route("/chat", methods=["GET"])
def chat(user):
    room = 1
    users = Users.query.all()
    posts = Posts.query.all()
    user_this = Users.query.filter_by(id="user")
    return render_template("chat.html", users=users,posts=posts, room=room)
 

@app.route("/profile/")
def profile():
    users = Users.query.all()
    posts = Posts.query.all()
    return render_template("profile.html", users=users, posts=posts)

@app.route("/testo")
def testoo():
    return render_template("testo.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = Users(username = uname, email = mail, password_hash = passw)
        register.set_password(passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("signup.html")





@socketio.on("send_message")
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {} : {}".format(data["username"], data["room"], data["message"]))
    socketio.emit("receive_message", data, room=data["room"])

@socketio.on("join_room")
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data["username"], data["room"]))
    join_room(data["room"])
    socketio.emit("join_room_announcement", data)


admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Posts, db.session))

if __name__ == '__main__':
    socketio.run(app, debug=True)
