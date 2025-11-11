from __future__ import annotations

#

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Callable, Iterator

class Registry[T]:
    def __init__(self) -> None:
        self.entries: list[T] = []
    
    def Register(self, a_registerable: T) -> int:
        self.entries.append(a_registerable)
        return len(self.entries) - 1
    
    def FindFirst(self, a_predicate: Callable[[T], bool]) -> int:
        gen = (i for i in range(len(self.entries)) if a_predicate(self.entries[i]))
        print(next(gen))
        for i in range(len(self.entries)):
            if a_predicate(self.entries[i]):
                print(i)
                return i
        return -1
    
    def FindAll(self, a_predicate: Callable[[T], bool]) -> list[int]:
        return [i for i in range(len(self.entries)) if a_predicate(self.entries[i])]
    
    def FindLast(self, a_predicate: Callable[[T], bool]) -> int:
        for i in range(len(self.entries) - 1, -1, -1):
            if a_predicate(self.entries[i]):
                return i
        return -1
    
    def EntriesIterator(self) -> Iterator[T]:
        return iter(self.entries)