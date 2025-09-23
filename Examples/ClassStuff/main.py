from pet import PetBreed, PetInstance, PetType

DOG: PetType = PetType("Dog", {
    PetBreed("German"), PetBreed("Italian"), PetBreed("Albanian")
})

a: PetInstance = PetInstance("Dog", "Max", 12, {("German", 2), ("Albanian", 1)})

print(a)