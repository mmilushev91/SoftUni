class_animals = {
    "dog": "mammal",
    "snake": "reptile",
    "crocodile": "reptile",
    "tortoise": "reptile",
}

animal = input()

if animal not in class_animals.keys():
    print("unknown")
    quit()

print(class_animals[animal])
