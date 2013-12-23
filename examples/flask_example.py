from flask import Flask
from datetime import datetime
from flint import Flint

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
	today = datetime.today()

	todo_list = ["Be awesome",
				 "Make a website",
				 "Take over the world"]

	flint = Flint("flask_example.md")
	flint.add_dict({"year": today.year,
					"month": today.month,
					"day": today.day,
					"hour": today.hour,
					"minute": today.minute})
	flint.add("visitor_name", name)
	flint.add("todo_list", todo_list)
	flint.render()
	return flint.getHTML()

# Handle the case when no name is supplied
@app.route('/')
def root():
	return hello("Visitor")

if __name__ == '__main__':
	app.run()