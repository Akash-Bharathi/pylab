#10(B) Develop a ticket booking platform where users can browse available events, select seats, and purchase tickets securely.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from models import db, User, Event, Ticket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking.db'

db.init_app(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=request.form['username'], password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('index'))
        flash('Login failed.')
    return render_template('login.html')

@app.route('/event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == 'POST':
        seat = int(request.form['seat'])
        if seat in event.seats_booked or seat > event.seats_total:
            flash('Seat already booked or invalid.')
        else:
            event.seats_booked.append(seat)
            ticket = Ticket(user_id=current_user.id, event_id=event.id, seat_number=seat)
            db.session.add(ticket)
            db.session.commit()
            flash('Ticket booked!')
    return render_template('event_detail.html', event=event)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.cli.command('initdb')
def initdb():
    db.create_all()
    print("Database initialized.")

if __name__ == '__main__':
    app.run(debug=True)
