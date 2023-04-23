from flask import Flask, render_template

app = Flask(__name__)

COURSES = [
  {
    'id': 1,
    'title': '8th std',
    'location': 'calicut',
    'fee': '10000'
  }
  {
    'id': 2,
    'title': '9th std',
    'location': 'calicut',
    'fee': '12000'
  }
  {
    'id': 3,
    'title': '10th std',
    'location': 'calicut',
    'fee': '13000'
  }
  {
    'id': 4,
    'title': '11th std',
    'location': 'calicut',
    'fee': '14000'
  }
]

@app.route("/") # "/"here stands for routing to home page of the url
def hello_world():
  return render_template('home.html', jobs=JOBS)

print(__name__)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  print("im inside if")#this is work arund to run the application instead of invoking the flask command and setting the environmental variable to run the web application
  
  
