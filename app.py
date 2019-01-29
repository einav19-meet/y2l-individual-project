from flask import Flask, render_template, request, redirect, url_for
from database import get_all_opinions, create_opinion, get_id, change_url, touch
from werkzeug.utils import secure_filename
import os 

ON_COMPUTER = True

app = Flask(__name__)

FULL_PATH = "/home/meet/Desktop/y2l-individual-project"

DEFAULT_IMAGE_URL = "/static/img/logo.png"
UPLOAD_FOLDER = "/static/img"
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
	opinions = get_all_opinions()
	opinions.reverse()
	if len(opinions) > 9:
		opinions = opinions[0:8]
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
	identity = get_id(name, title, opinion)


	if "file" in request.files:
		image_file = request.files["file"]

		img_type = image_file.filename.split(".")[-1]
		if img_type in ALLOWED_EXTENSIONS:
			filename = secure_filename("saved_image_" + str(identity) + "." + img_type)
			saved_filename = os.path.join(app.config["UPLOAD_FOLDER"], filename)
			if ON_COMPUTER:
				touch(FULL_PATH + saved_filename)
				image_file.save(FULL_PATH + saved_filename)
			else:
				touch(saved_filename)
				image_file.save(saved_filename)
		else:
			raise AssertionError("Invalid Image type")
		img_url = saved_filename
	else:
		img_url = DEFAULT_IMAGE_URL


	change_url(identity, img_url)
	

	return redirect(url_for("hello_world"))


if __name__ == "__main__":
    app.run(debug=True)

