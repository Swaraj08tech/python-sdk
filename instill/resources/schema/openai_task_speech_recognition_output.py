# generated by datamodel-codegen:
#   filename:  openai_task_speech_recognition_output.json

from __future__ import annotations

from dataclasses import dataclass

Text = str


@dataclass
class ChatMessage:
    content: str
    role: str


@dataclass
class Output:
    text: Text
