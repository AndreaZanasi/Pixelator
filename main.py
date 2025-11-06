import argparse
import numpy as np
from src.loader import ImageLoader
from src.preprocessor import ImagePreprocessor
from src.generator import SpriteGenerator
from src.algorithms import KMeans
from src.config import DEFAULT_RESOLUTION, COLOR_PALETTES, COLOR_PALETTE_OPTIONS, MAX_CLUSTERS

def main():
    parser = argparse.ArgumentParser(description='Generate pixel art sprites from images')
    parser.add_argument('image_path', help='Path to the input image')
    parser.add_argument('-W', '--width', type=int, default=DEFAULT_RESOLUTION[0], 
                        help=f'Output width in pixels (default: {DEFAULT_RESOLUTION[0]})')
    parser.add_argument('-H', '--height', type=int, default=DEFAULT_RESOLUTION[1], 
                        help=f'Output height in pixels (default: {DEFAULT_RESOLUTION[1]})')
    parser.add_argument('-P', '--palette', type=str, default='none', 
                        choices=COLOR_PALETTE_OPTIONS,
                        help=f'Color palette to apply (default: none)')
    
    args = parser.parse_args()
    
    image_path = args.image_path
    resolution = (args.width, args.height)
    palette = COLOR_PALETTES[args.palette]

    loader = ImageLoader()
    image = loader.load_image(image_path)

    preprocessor = ImagePreprocessor()
    processed_image = preprocessor.resize_image(image, resolution)

    image_array = np.array(processed_image)
    
    original_shape = image_array.shape
    pixel_data = image_array.reshape(-1, image_array.shape[-1])

    # Use palette length if palette is specified, otherwise use MAX_CLUSTERS
    n_clusters = len(palette) if palette is not None else MAX_CLUSTERS
    algorithm = KMeans(n_clusters=n_clusters)
    algorithm.fit(pixel_data)
    cluster_labels = algorithm.predict(pixel_data)
    
    clusters = cluster_labels.reshape(original_shape[:2])

    sprite_generator = SpriteGenerator()
    sprite_generator.set_resolution(resolution[0], resolution[1])
    sprite = sprite_generator.generate_sprite(clusters, algorithm, palette)

    file_name = image_path.split("/")[-1].split(".")[0]
    output_path = f"gen_images/{file_name}_sprite.png"
    loader.save_image(sprite, output_path)
    print(f"Sprite generated and saved to {output_path}")

if __name__ == "__main__":
    main()