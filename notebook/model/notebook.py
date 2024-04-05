from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Note:
    code: int
    title: str
    text: str
    importance: str
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    tags: list[str] = field(default_factory=list)
    creation_date: datetime = field(default_factory=datetime.now)

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"Code: {self.code}\n" \
               f"Creation date: {self.creation_date}\n" \
               f"{self.title}: {self.text}"


class Notebook:
    def __init__(self):
        self.notes: dict[int, Note] = {}
        self._last_code = 0

    def add_note(self, title: str, text: str, importance: str) -> int:
        self._last_code += 1
        new_note = Note(self._last_code, title, text, importance)
        self.notes[self._last_code] = new_note
        return self._last_code

    def list_notes(self) -> list[Note]:
        return list(self.notes.values())

    def add_tags_to_note(self, code: int, tags: list[str]) -> None:
        if code in self.notes:
            note = self.notes[code]
            for tag in tags:
                note.add_tag(tag)

    def important_notes(self) -> list[Note]:
        return [note for note in self.notes.values() if note.importance in ("HIGH", "MEDIUM")]

    def delete_note(self, code: int) -> None:
        if code in self.notes:
            del self.notes[code]

    def get_notes(self) -> list[Note]:
        return list(self.notes.values())

    def tags_note_count(self) -> dict[str, int]:
        tags_count: dict[str, int] = {}
        for note in self.notes.values():
            for tag in note.tags:
                tags_count[tag] = tags_count.get(tag, 0) + 1
        return tags_count
