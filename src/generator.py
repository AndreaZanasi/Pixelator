import numpy as np
from PIL import Image

class SpriteGenerator:
    def __init__(self):
        self.resolution = (32, 32)

    def set_resolution(self, width, height):
        self.resolution = (width, height)

    def generate_sprite(self, clustered_data, algorithm, palette=None):
        color_map = algorithm.centroids.astype(np.uint8)
        
        if palette is not None:
            color_map = self._map_to_palette(color_map, palette)
        
        n_channels = color_map.shape[1]
        
        height, width = clustered_data.shape
        sprite_array = np.zeros((height, width, n_channels), dtype=np.uint8)
        
        for i in range(height):
            for j in range(width):
                cluster_id = clustered_data[i, j]
                sprite_array[i, j] = color_map[cluster_id]
        
        mode = 'RGBA' if n_channels == 4 else 'RGB'
        sprite = Image.fromarray(sprite_array, mode)
        return sprite
    
    def _map_to_palette(self, colors, palette):
        palette_array = np.array(palette)
        mapped_colors = []
        
        for color in colors:
            distances = np.linalg.norm(palette_array - color[:3], axis=1)
            closest_idx = np.argmin(distances)
            mapped_colors.append(palette_array[closest_idx])
        
        return np.array(mapped_colors)