import os
from PIL import Image


class ImageTransformer:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pics_path = os.path.join(base_dir, '..', 'Pics')
        self.pics_path = os.path.join(pics_path)
    
    def extend_background(self, img: Image, width: int, height: int) -> Image:
        orig_width, orig_height = img.size
        new_width = int(orig_width * (width / 100))
        new_height = int(orig_height * (height / 100))
        
        #grey
        background_color = (200, 200, 200)
        new_img = Image.new('RGB', (new_width, new_height), background_color)
        
        paste_x = (new_width - orig_width) // 2
        paste_y = (new_height - orig_height) // 2
        new_img.paste(img, (paste_x, paste_y))
        
        return new_img