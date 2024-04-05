from datetime import datetime
from dataclasses import dataclass


@dataclass
class Note:

    def __init__(self, code: int, title: str, text: str, importance: str):
        self.code: int = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance

    def add_tag(self, tag: str):
        pass

    def __str__(self) -> str:
        pass


class Notebook:

    def __init__(self):
        pass

    def add_note(self, title: str, text: str, importance: str):
        pass

    def important_notes(self) -> list[Note]:
        pass

    def tags_notes_count(self) -> dict[str, int]:
        pass
