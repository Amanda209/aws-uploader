import os
from application    import app
from flask          import Flask, request, redirect, url_for, render_template, \
    send_from_directory, current_app, send_file
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')

            return redirect(request.url)

        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')

            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('index', filename=filename))

    base_dir = app.config['UPLOAD_FOLDER']
    files = ({'name': file, 'size': os.stat(os.path.join(base_dir,file))[6]} for file in os.listdir(base_dir))

    return render_template('index.html', files=files)

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    base_dir = app.config['UPLOAD_FOLDER']

    return send_file(base_dir, attachment_filename=filename)
