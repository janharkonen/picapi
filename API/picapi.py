from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from werkzeug.utils import secure_filename
from SQLiteInterface import SQLiteInterface
from ImageBucket import ImageBucket

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)
sqlite_interface = SQLiteInterface()
image_bucket = ImageBucket()
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
            sqlite_interface.save(unique_filename, file.filename)
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)