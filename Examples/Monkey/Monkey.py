import os, random

def Main() -> None:
    running: bool = True

    while running:
        print("Le Grange")

        if random.randrange(0, 100) == 1:
            with open("Monkey.py", "r+") as file:
                toUse = file.read().replace('''Grange")''', '''Grange"); print('Le strange')''', 1)
            print("done")
            with open("Monkey.py", "w") as file:
                file.write(toUse)
        elif random.randrange(0, 1000) == 1:
            running = False

if __name__ == "__main__":
    Main()