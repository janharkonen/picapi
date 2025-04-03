import os
from werkzeug.datastructures.file_storage import FileStorage

class ImageTransformer:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pics_path = os.path.join(base_dir, '..', 'Pics')
        self.pics_path = os.path.join(pics_path)
    
    def extend_background(self, pics_dir: str, filename: str, extension_percentage: int):
        # Manipulate image such that it puts a "extension_percentage"% bigger grey background with the "filename" picture
        extension_percentage = int(extension_percentage)
        assert type(extension_percentage) is int, 'XBG is not int'

        return 1