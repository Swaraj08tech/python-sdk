# generated by datamodel-codegen:
#   filename:  openai_task_text_embeddings_output.json

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Optional

UpstreamValue = str


InstillTypes = Any


@dataclass
class ImageUrl:
    url: str


class Type(Enum):
    text = 'text'
    image_url = 'image_url'


@dataclass
class MultiModalContentItem:
    type: Type
    image_url: Optional[ImageUrl] = None
    text: Optional[str] = None


@dataclass
class Output:
    embedding: List[float]


@dataclass
class ChatMessage:
    content: List[MultiModalContentItem]
    role: str