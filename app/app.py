from flask import Flask, request, render_template
import os
from classifier import get_model, make_prediction


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

server = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@server.route("/")
def home():
	return render_template('index.html')


@server.route("/upload", methods=['POST'])
def upload():
	if 'file' not in request.files:
		msg = {"message": "no file part"}
		return {"message": msg}
	
	file = request.files['file']
	if file.filename == '':
		msg = {"message": "no selected file"}

	if file and allowed_file(file.filename):
		file_obj = file.read()
		model = get_model()
		(class_name, class_score) = make_prediction(model, file_obj)
		msg = {
			"class_name": class_name,
			"class_score": class_score
		}
	return {"message": msg}

if __name__ == "__main__":
	server.run(debug=True)