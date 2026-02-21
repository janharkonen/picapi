import os
from PIL import Image
from rembg import remove

class ImageTransformer:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pics_path = os.path.join('app', 'app', 'storage', 'storage', 'Pics')
        self.pics_path = os.path.join(pics_path)
    
    def extend_background(self, img: Image, 
                          left: int = 100, 
                          right: int = 100, 
                          top: int = 100,
                          bottom: int = 100,
                          background_color: tuple = (200, 200, 200)) -> Image:
        orig_width, orig_height = img.size
        new_width = int(orig_width + orig_width*(left/100 - 1) + orig_width*(right/100-1))
        new_height = int(orig_height + orig_height*(top/100 - 1) + orig_height*(bottom/100-1))
        
        if len(background_color) == 4 and background_color[3] == 0:
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            mode = 'RGBA'
        else:
            mode = img.mode
            
        new_img = Image.new(mode, (new_width, new_height), background_color)
        
        paste_x = int(new_width - orig_width*(right/100))
        paste_y = int(new_height - orig_height*(bottom/100))
        new_img.paste(img, (paste_x, paste_y))
        
        return new_img
    
    def remove_background(self, img: Image) -> Image:
        new_img = remove(img)
        return new_img