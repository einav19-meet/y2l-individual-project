from flask import Flask, render_template
from database import get_all_opinions
app = Flask(__name__)

@app.route('/')
def hello_world():
	opinions = get_all_opinions()
	return render_template('index.html', opinions = opinions)


@app.route('/form')
def forming():
	return render_template('finalForm.html')



if __name__ == "__main__":
    app.run(debug=True)

