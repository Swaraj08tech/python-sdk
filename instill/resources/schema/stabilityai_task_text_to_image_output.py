# generated by datamodel-codegen:
#   filename:  stabilityai_task_text_to_image_output.json

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Output:
    images: List[str]
    seeds: List[float]
