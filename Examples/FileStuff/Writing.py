import random
CONSONANTS: str = "bcdfghjklmnpqrstvwxz"
VOWELS: str = "aeiouy"

def RandomString(a_length: int = 5) -> str:
    vowel: bool = random.random() > 0.5
    toReturn: str = ""
    for _ in range(a_length):
        toReturn += random.choice(VOWELS) if vowel else random.choice(CONSONANTS)
        vowel = not vowel
    return toReturn

def main() -> None:
    with open("./temp.txt", "w+") as file:
        file.writelines([f"{" ".join([RandomString(random.randint(3, 16)) for _ in range(random.randint(3, 16))])}.\n".capitalize() for _ in range(random.randint(3, 100))])

if __name__ == "__main__":
    main()