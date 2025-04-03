import os
from PIL import Image

class ImageTransformer:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pics_path = os.path.join(base_dir, '..', 'Pics')
        self.pics_path = os.path.join(pics_path)
    
    def extend_background(self, pics_dir: str, filename: str, extension_percentage: int):
        # Manipulate image such that it puts a "extension_percentage"% bigger grey background with the "filename" picture
        extension_percentage = int(extension_percentage)
        assert type(extension_percentage) is int, 'XBG is not int'

        img_path = os.path.join(pics_dir, filename)
        
        # Open the original image
        with Image.open(img_path) as img:
            orig_width, orig_height = img.size
            new_width = int(orig_width * (extension_percentage / 100))
            new_height = int(orig_height * (extension_percentage / 100))
            
            #grey
            background_color = (200, 200, 200)
            new_img = Image.new('RGB', (new_width, new_height), background_color)
            
            # Calculate position to paste the original image (centered)
            paste_x = (new_width - orig_width) // 2
            paste_y = (new_height - orig_height) // 2
            
            # Paste the original image onto the new background
            new_img.paste(img, (paste_x, paste_y))
            
            return new_img