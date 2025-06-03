# 9(b) Develop a social media platform where users can create profiles, post updates, connect with friends, and engage with content through likes and comments

from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    bio = db.Column(db.String(300))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    content = db.Column(db.String(300))
    likes = db.Column(db.Integer, default=0)

# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            session['user_id'] = user.id
            return redirect('/feed')
    return render_template('login.html')

@app.route('/feed')
def feed():
    if 'user_id' not in session:
        return redirect('/')
    posts = Post.query.all()
    user = User.query.get(session['user_id'])
    return render_template('feed.html', posts=posts, user=user)

@app.route('/post', methods=['POST'])
def post():
    if 'user_id' in session:
        new_post = Post(user_id=session['user_id'], content=request.form['content'])
        db.session.add(new_post)
        db.session.commit()
    return redirect('/feed')

@app.route('/like/<int:post_id>')
def like(post_id):
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    db.session.commit()
    return redirect('/feed')

# Initialize DB and run app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
