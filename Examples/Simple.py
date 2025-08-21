import random

nums: list[int] = sorted([random.randrange(1, 1000) for _ in range(100)])
print(f"Num | Square ")
print(f"----|--------")
for num in nums:
    print(f"{num:>3.0f} | {(num ** 2):>7,}")

print()

names: dict[str, int] = {name: random.randint(0, 100) for name in sorted(["George", "Carl", "Berreta", "Megan", "Elizabeth", "Elizer"])}
print(f"Name         | Grade ")
print(f"-------------|--------")
for name, grade in names.items():
    print(f"{name:<12} | {grade:<3}")