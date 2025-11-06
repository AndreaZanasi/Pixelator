class SpriteExporter:
    def export_to_png(self, sprite_data, file_path):
        from PIL import Image
        image = Image.new('RGBA', (sprite_data.width, sprite_data.height))
        image.putdata(sprite_data.pixels)
        image.save(file_path)

    def export_to_json(self, sprite_data, file_path):
        import json
        sprite_dict = {
            'width': sprite_data.width,
            'height': sprite_data.height,
            'pixels': sprite_data.pixels
        }
        with open(file_path, 'w') as json_file:
            json.dump(sprite_dict, json_file)