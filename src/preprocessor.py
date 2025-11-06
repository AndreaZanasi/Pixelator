import numpy as np
from PIL import Image

class ImagePreprocessor:
    def __init__(self):
        pass

    def resize_image(self, image, new_size):
        return image.resize(new_size, Image.LANCZOS)

    def normalize_colors(self, image):
        image_array = np.array(image)
        normalized_image = (image_array - image_array.min()) / (image_array.max() - image_array.min()) * 255
        return Image.fromarray(normalized_image.astype('uint8'))