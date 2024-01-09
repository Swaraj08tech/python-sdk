# generated by datamodel-codegen:
#   filename:  huggingface_task_conversational_input.json

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Inputs:
    text: str
    generated_responses: Optional[List[str]] = None
    past_user_inputs: Optional[List[str]] = None


@dataclass
class Parameters:
    max_length: Optional[int] = None
    max_time: Optional[float] = None
    min_length: Optional[int] = None
    repetition_penalty: Optional[float] = None
    temperature: Optional[float] = 1
    top_k: Optional[int] = None
    top_p: Optional[float] = None


@dataclass
class Options:
    use_cache: Optional[bool] = None
    wait_for_model: Optional[bool] = None


StringInput = str


@dataclass
class Input:
    inputs: Inputs
    model: Optional[str] = None
    options: Optional[Options] = None
    parameters: Optional[Parameters] = None