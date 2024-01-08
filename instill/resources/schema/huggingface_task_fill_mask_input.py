# generated by datamodel-codegen:
#   filename:  huggingface_task_fill_mask_input.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Options:
    use_cache: Optional[bool] = None
    wait_for_model: Optional[bool] = None


@dataclass
class Input:
    inputs: str
    model: Optional[str] = None
    options: Optional[Options] = None
