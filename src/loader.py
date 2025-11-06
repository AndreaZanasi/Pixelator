class ImageLoader:
    def load_image(self, file_path):
        from PIL import Image
        try:
            image = Image.open(file_path)
            return image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def save_image(self, image, file_path):
        try:
            image.save(file_path, format='PNG')
        except Exception as e:
            print(f"Error saving image: {e}")