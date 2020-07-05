# library imports
import os, json
from flask import Flask, request, redirect, url_for, flash
from flask import render_template
from werkzeug.utils import secure_filename
import cell_culture

# global variable initialisations
PORT = 6923
cwd = os.getcwd()
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
ALLOWED_EXTENSIONS = {'jpg'}
IMAGE_FOLDER = cwd + r'\static\images'
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
# flaskKwargs = {'debug': False, 'host': '0.0.0.0'}
print("this is image folder")
print(IMAGE_FOLDER)


# utility functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# routing
@app.route('/')
def homepage_upload():
    return render_template('upload.html', title="Cell Confluency App")


@app.route("/image_upload", methods=["POST"])
def upload_image():
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file in request"

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        abs_path_to_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(abs_path_to_file)
        flash("Upload Successfull")

    else:
        flash("No or invalid File")
    return redirect(url_for("homepage_upload"))


@app.route('/calculate_confluency', methods=['GET', 'POST'])
def calculate_confluency():
    outDict = {}
    if request.method == 'GET':
        return render_template("calculate_confluency.html",
                               title="Cell Confluency App",
                               confluency="X", cell_type="X",
                               overgrow_estim="X")
    else:
        requestDict = request.get_json()
        fileName = requestDict['fileName']
        confluency_value, cell_type = \
            cell_culture.calculate_confluency(fileName)
        outDict['confluency_value'] = round(confluency_value, 2)
        outDict['cell_type'] = cell_type

        print("outDict: ", outDict)
        return json.dumps(outDict)


@app.route('/estimate_overgrow', methods=['POST'])
def estimate_overgrow():
    outDict = {}
    requestDict = request.get_json()
    proliferationHour = requestDict['proliferationHour']

    if not proliferationHour:
        outDict['overgrow_estim_text'] = "Overgrow Estimation = " \
                                         "Please enter valid Hour value"
        return json.dumps(outDict)

    overgrow_estimation = cell_culture.estimate_overgrow(proliferationHour)
    outDict['overgrow_estim_text'] = f"Overgrow Estimation " \
                                     f"= {overgrow_estimation}"

    print("outDict: ", outDict)
    return json.dumps(outDict)


@app.route('/populate_select_list')
def populate_select_list():
    files = os.listdir(IMAGE_FOLDER)
    image_files = []

    for file in files:
        if file[-3:] in ['jpg', 'JPG']:
            image_files.append(file)

    return json.dumps(image_files)


# server spawn
if __name__ == '__main__':
    # print(f"Visit: http://localhost:{PORT}")
    app.run(debug=False)
