from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
import uuid
import os
from io import BytesIO
from PIL import Image
from werkzeug.utils import secure_filename
from SQLiteInterface import SQLiteInterface
from ImageBucket import ImageBucket
from ImageTransformer import ImageTransformer


app = Flask(__name__)
# Enable CORS for all routes
CORS(app)
db_interface = SQLiteInterface()
image_bucket = ImageBucket()
image_transformer = ImageTransformer()
# Configuration
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Flask: No image part in the request'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Flask: No image selected for uploading'}), 400
    
    if file and allowed_file(file.filename):
        try:    
            # Generate a unique filename to prevent overwriting
            unique_id = uuid.uuid4().hex
            original_filename = secure_filename(file.filename)
            file_extension = original_filename.rsplit('.', 1)[1].lower()
            unique_filename = f"{unique_id}.{file_extension}"
            
            image_bucket.save(unique_filename, file)
            db_interface.save(unique_filename, file.filename)
            ## Return success response
            return jsonify({
                'message': 'Image uploaded successfully',
                #'filename': unique_filename,
                #'original_filename': original_filename
            }), 200
        except:
            return jsonify({'error': 'Flask: unknown error occured'}), 400
    else:
        return jsonify({'error': 'Flask: File type not allowed'}), 400

@app.route('/api/getallpicmetadata', methods=['GET'])
def get_all_pic_metadata():
    pic_metadata = db_interface.get_metadata()
    return jsonify(pic_metadata), 200

@app.route('/api/pics/<filename>', methods=['GET'])
def get_picture(filename: str):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pics_dir = os.path.join(base_dir, '..', 'Pics')
    if request.args:
        extend_background_percentage = request.args.get('XBG')
        if extend_background_percentage is not None:
            #edit this
            new_img = image_transformer.extend_background(pics_dir, filename, extend_background_percentage)
            img_io = BytesIO()
            img_format = filename.rsplit('.', 1)[1].upper()
            if img_format == 'JPG':
                img_format = 'JPEG'  # PIL uses 'JPEG' instead of 'JPG'

            assert type(new_img is Image), 'Image is not type PIL/Image' 
            new_img.save(img_io, format=img_format)
            img_io.seek(0)
            return send_file(img_io, mimetype=f'image/{img_format.lower()}')
    
    image = send_from_directory(pics_dir, filename)
    return image

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)