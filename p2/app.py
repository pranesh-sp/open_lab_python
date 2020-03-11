from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/UserLogin', methods=['GET', 'POST'])
def UserLogin():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'pranesh' or request.form['password'] != 'user':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            return redirect(url_for('success'))

    return render_template('UserLogin.html', error=error)


@app.route('/success',methods = ['GET', 'POST'])
def success():
    if request.method == "POST":
        session['username']=request.form['username']
    return render_template('success.html')


@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return  render_template('profile.html', username=username)
    else:
        return '<p>Please login first</p>'


@app.route('/AdminLogin', methods=['GET', 'POST'])
def AdminLogin():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('AdminLogin.html', error=error)


@app.route('/viewBook',methods = ['GET', 'POST'])
def viewBook():
    return render_template('bookDetails.html')

@app.route('/contact',methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/libdetails',methods = ['GET', 'POST'])
def libdetails():
    return render_template('libdetails.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username',None)
        return render_template('logout.html');
    else:
        return '<p>user already logged out</p>'


if __name__ == '__main__':    app.run(debug=True)
