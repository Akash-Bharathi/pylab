#9(a) Create a fully funtional blogging platform where users register, create blog posts, add comments and browse through published ports

#9(a) Create a fully funtional blogging platform where users register, create blog posts, add comments and browse through published ports
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))

# Routes
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        comment_text = request.form['comment']
        comment = Comment(text=comment_text, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = 1  # Default user for testing
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

# Initialize DB and run app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
