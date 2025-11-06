DEFAULT_RESOLUTION = (128, 128)

COLOR_PALETTES = {
    "none": None,
    "gameboy": [
        (15, 56, 15),
        (48, 98, 48),
        (139, 172, 15),
        (155, 188, 15)
    ],
    "pastel": [
        (255, 179, 186),
        (255, 223, 186),
        (255, 255, 186),
        (186, 255, 201),
        (186, 225, 255)
    ],
    "monochrome": [
        (0, 0, 0),
        (64, 64, 64),
        (128, 128, 128),
        (192, 192, 192),
        (255, 255, 255)
    ]
}

COLOR_PALETTE_OPTIONS = list(COLOR_PALETTES.keys())

MAX_CLUSTERS = 16
MIN_CLUSTER_SIZE = 5

IMAGE_FORMAT = "PNG"
