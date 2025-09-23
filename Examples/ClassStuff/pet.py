from dataclasses import dataclass

@dataclass(frozen=True)
class PetBreed:
    name: str

@dataclass
class PetType:
    name: str
    breeds: set[PetBreed]

@dataclass(repr=False)
class PetInstance:
    petType: str
    name: str
    age: int
    breed: set[tuple[str, int]]
    
    def __repr__(self) -> str:
        total: float = sum([weight for _, weight in self.breed]) / 100
        return f"{self.name}: {self.petType} ({self.age}) {", ".join([f"{weight/total:.2f}% {breed}" for breed, weight in self.breed])}"

