# generated by datamodel-codegen:
#   filename:  huggingface_task_table_question_answering_input.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Inputs:
    query: str
    table: Dict[str, Any]


Model = str


@dataclass
class Options:
    use_cache: Optional[bool]
    wait_for_model: Optional[bool]


StringInput = str


@dataclass
class Input:
    inputs: Inputs
    model: Optional[Model]
    options: Optional[Options]
