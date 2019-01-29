from flask import Flask, render_template, request, redirect, url_for
from database import get_all_opinions, create_opinion
app = Flask(__name__)

@app.route('/')
def hello_world():
	opinions = get_all_opinions()
	print(opinions)
	return render_template('index.html', opinions = opinions)


@app.route('/form')
def forming():
	return render_template('finalForm.html')

@app.route("/opinion-form", methods=["POST"])
def opinion_post():
	name = request.form["name"]
	title = request.form["title"]
	opinion= request.form["opinion"]

	create_opinion(name,title,opinion)

	return redirect(url_for("hello_world"))


if __name__ == "__main__":
    app.run(debug=True)

