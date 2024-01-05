# generated by datamodel-codegen:
#   filename:  huggingface_task_conversational_output.json

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Conversation:
    """
    A facility dictionnary to send back for the next input (with the new user input addition).
    """

    generated_responses: List[str]
    past_user_inputs: List[str]


@dataclass
class Output:
    conversation: Optional[Conversation]
    generated_text: str


Model = str


@dataclass
class Options:
    use_cache: Optional[bool]
    wait_for_model: Optional[bool]


StringInput = str
