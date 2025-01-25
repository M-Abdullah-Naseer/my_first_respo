from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def pageFirst():
 return render_template('ITC-Home.html')

@app.route('/home')
def home():
 return render_template('ITC-Home.html')

@app.route('/about')
def about():
 return render_template('ITC-About.html')

@app.route('/login')
def login():
 return render_template('myapp_login.html')

@app.route('/signup')
def signup():
 return render_template('myapp_signup.html')

@app.route('/memb')
def memb():
 return render_template('ITC-Membership.html')



if __name__ == '__main__':
 app.run(debug=True)
