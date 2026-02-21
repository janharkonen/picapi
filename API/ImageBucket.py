import os
from werkzeug.datastructures.file_storage import FileStorage
from PIL import Image

class ImageBucket:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.pics_dir = os.path.join('/app', 'app', 'storage', 'storage', 'Pics')
        os.makedirs(self.pics_dir, exist_ok=True)
    
    def save(self, unique_filename: str, file: FileStorage):
        # Save the file
        file_path = os.path.join(self.pics_dir, unique_filename)
        file.save(file_path)

    def delete(self, filename: str):
        # Delete the file
        file_path = os.path.join(self.pics_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)

    def get_dir(self) -> str:
        return self.pics_dir
    
    def get_image(self, filename: str) -> Image:
        img_path = os.path.join(self.pics_dir, filename)
        with Image.open(img_path) as img:
            return img.copy()