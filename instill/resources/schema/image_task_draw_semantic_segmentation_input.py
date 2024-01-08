# generated by datamodel-codegen:
#   filename:  image_task_draw_semantic_segmentation_input.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class Object:
    category: str
    rle: str


InstillTypes = Any


@dataclass
class Input:
    image: str
    stuffs: List[Object]
    showScore: Optional[bool] = None
