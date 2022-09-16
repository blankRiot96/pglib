import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Tuple

import pygame

logger = logging.getLogger()


def get_images_from_spritesheet(
    sheet: pygame.Surface,
    size: Tuple[int],
    bound=False,
):
    """
    Converts a sprite sheet to a list of surfaces
    Parameters:
        sheet: A pygame.Surface that contains the sprite sheet
        rows: Amount of rows in the sprite sheet
        columns: Amount of columds in the sprite sheet
        size: Size of a sprite in the sprite sheet
    """
    images = []

    width, height = size

    # loop through all sprites in the sprite sheet
    rows = int(sheet.get_height() / height)
    columns = int(sheet.get_width() / width)

    for row in range(rows):
        for col in range(columns):
            image = sheet.subsurface(pygame.Rect((col * width), (row * height), *size))

            if bound:
                r = image.get_bounding_rect()
                image = image.subsurface(r)

            images.append(image)

    return images


def load_images(state: str) -> Iterator:
    path = Path("assets/images/")

    json_files = path.rglob("*.json")
    json_files = tuple(json_files)
    yield len(json_files)
    for metadata_f in json_files:
        metadata = json.loads(metadata_f.read_text())
        assets = {}
        for file, data in metadata.items():
            if state not in data["states"] and data["states"] != ["*"]:
                continue

            complete_path = metadata_f.parent / file
            logger.info(f"Loaded {complete_path}")
            if data["convert_alpha"]:
                image = pygame.image.load(complete_path).convert_alpha()
            else:
                image = pygame.image.load(complete_path).convert()

            if data["sprite_sheet"] is None:
                asset = image
            else:
                asset = get_images_from_spritesheet(
                    image, *data["sprite_sheet"].values()
                )

            file_extension = file[file.find(".") :]
            assets[file.replace(file_extension, "")] = asset
        yield assets
