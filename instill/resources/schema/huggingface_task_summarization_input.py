# generated by datamodel-codegen:
#   filename:  huggingface_task_summarization_input.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Parameters:
    max_length: Optional[int]
    max_time: Optional[float]
    min_length: Optional[int]
    repetition_penalty: Optional[float]
    top_k: Optional[int]
    top_p: Optional[float]
    temperature: Optional[float] = 1


Model = str


@dataclass
class Options:
    use_cache: Optional[bool]
    wait_for_model: Optional[bool]


StringInput = str


@dataclass
class Input:
    inputs: StringInput
    model: Optional[Model]
    options: Optional[Options]
    parameters: Optional[Parameters]
