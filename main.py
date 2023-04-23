from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # "/"here stands for routing to home page of the url
def hello_world():
  return render_template('home.html')

print(__name__)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  print("im inside if")#this is work arund to run the application instead of invoking the flask command and setting the environmental variable to run the web application
  
  
