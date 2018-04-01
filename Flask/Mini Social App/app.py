from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_login import current_user
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jeangene@localhost/flasksocial'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = '$2a$16$PnnIgfMwk0jGX4SkHqSOPO'
# app.debug = True

db = SQLAlchemy(app)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/posting')
@login_required
def posting():
    now_user = User.query.filter_by(email=current_user.email).first()
    this_user = UserDetails.query.filter_by(user_id=current_user.id).first()
    return render_template('add_post.html', now_user=now_user, this_user=this_user)


@app.route('/user_list')
@login_required
def get_user_list():
    users = User.query.all()
    user_d = UserDetails.query.order_by(UserDetails.username).all()
    return render_template('user_list.html', users=users, user_d=user_d)


@app.route('/add_post', methods=['POST'])
def add_post():
    post = Post(request.form['pcontent'], request.form['pemail'])
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/editprofile')
@login_required
def edit_profile():
    now_user = User.query.filter_by(email=current_user.email).first()
    return render_template('user_detail.html', now_user=now_user)


@app.route('/add_user_details', methods={'POST'})
@login_required
def add_user_details():
    user_details = UserDetails(request.form['pid'], request.form['username'],
                               request.form['profile_pic'], request.form['location'])
    db.session.add(user_details)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/feed')
def get_post():
    singlepost = Post.query.all()
    return render_template('post_feed.html', singlepost=singlepost)


@app.route('/profile/<id>')
def user_profile(id):
    oneuser = UserDetails.query.filter_by(id=id).first()
    suser = User.query.filter_by(id=oneuser.user_id).first()
    user_post = Post.query.filter_by(posted_by=suser.email)
    return render_template('user_profile.html', oneuser=oneuser, suser=suser, user_post=user_post)


#  models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    username = db.Column(db.String(100))
    profile_pic = db.Column(db.String(300))
    location = db.Column(db.String(100))

    def __init__(self, user_id, username, profile_pic, location):
        self.user_id = user_id
        self.username = username
        self.profile_pic = profile_pic
        self.location = location

    def __repr__(self):
        return 'UserDetails %r>' % self.username


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_content = db.Column(db.String(200))
    posted_by = db.Column(db.String(100))
    created_on = db.Column(db.DateTime)

    def __init__(self, post_content, posted_by, created_on=None):
        self.post_content = post_content
        self.posted_by = posted_by
        self.created_on = time.strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<Post %r>' % self.post_content


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with  (** only need this code on first run **)
# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='abc@xyz.com', password='test123')
#     db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
