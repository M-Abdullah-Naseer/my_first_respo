from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def pageFirst():
 return "Welcome to the First Page!"

@app.route('/home')
def home():
 return render_template('ITC-Home.html')

@app.route('/about')
def about():
 return render_template('ITC-About.html')

@app.route('/memb')
def memb():
 return render_template('ITC-Membership.html')



if __name__ == '__main__':
 app.run(debug=True)
