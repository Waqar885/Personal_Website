from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from secret_key import key

app = Flask(__name__)
app.secret_key = key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(10000), nullable=False)
    parent_sno = db.Column(db.Integer, db.ForeignKey('data.sno'), nullable=True)  # Link to parent message
    replies = db.relationship('Data', backref=db.backref('parent', remote_side=[sno]), lazy='select')

    def __repr__(self):
        return f'{self.sno} : {self.title}'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        name = request.form['Name']
        email = request.form['Email']
        city = request.form['City']
        title = request.form['Title']
        message = request.form['Message']
        data = Data(name=name, email=email, city=city, title=title, message=message)
        db.session.add(data)
        db.session.commit()
    all_data= Data.query.all()
    
    return render_template('contact.html', all_data=all_data)

@app.route('/message/<int:sno>')
def message(sno):
    data = Data.query.get_or_404(sno)
    return render_template('message.html', data=data)

@app.route('/delete/<int:sno>')
def delete(sno):
    data = Data.query.filter_by(sno=sno).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

@app.route('/message/<int:sno>/reply', methods=['POST', 'GET'])
def reply(sno):
    message = Data.query.get_or_404(sno)

    if request.method == "POST":
        print(request.form)  # Debugging: Check if form data is received
        try:
            reply_content = request.form.get('Reply')
            if not reply_content:
                flash("Reply cannot be empty!", "error")
                return redirect(f'/message/{sno}/reply')
            
            # Add new reply
            reply = Data(
                name=request.form.get('Name'),
                email=request.form.get('Email'),
                city=request.form.get('City'),
                message=request.form.get('Reply'),
                parent_sno=message.sno,
                title="Replyed"  # Set a default title for replies
)

            db.session.add(reply)
            db.session.commit()
            flash("Reply sent successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {e}", "error")
            return redirect(f'/message/{sno}/reply')

    replies = Data.query.filter_by(parent_sno=message.sno).all()
    return render_template('reply.html', data=message, replies=replies)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)