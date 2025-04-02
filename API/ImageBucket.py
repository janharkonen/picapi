import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures.file_storage import FileStorage

class ImageBucket:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pics_path = os.path.join(base_dir, '..', 'Pics')
        self.pics_path = os.path.join(pics_path)
        os.makedirs(self.pics_path, exist_ok=True)
    
    def save(self, uuid: str, file: FileStorage):
        # Generate a unique filename to prevent overwriting
        original_filename = secure_filename(file.filename)
        file_extension = original_filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid}.{file_extension}"

        # Save the file
        file_path = os.path.join(self.pics_path, unique_filename)
        file.save(file_path)