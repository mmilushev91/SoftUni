class Zoo:
  __animals = 0
  
  def __init__(self, name):
    self.name = name
    self.mammals = []
    self.fishes = []
    self.birds = []
  
  def add_animal(self, species, name):
    
    match species:
      case "mammal":
        self.mammals.append(name)
      case "fish":
        self.fishes.append(name)
      case "bird":
        self.birds.append(name)
    
    Zoo.__animals += 1
  
  def get_info(self, species):
    output_species = None
    
    match species:
      case "mammal":
        return f"Mammals in {self.name}: {', '.join(self.mammals)}\n\
                Total animals: {Zoo.__animals}" 
      case "fish":
        return f"Fishes in {self.name}: {', '.join(self.fishes)}\n\
                Total animals: {Zoo.__animals}"
      case "bird":
        return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"

zoo_name = input() 
animal_count = int(input())

zoo = Zoo(zoo_name)

for _ in range(animal_count):
  species, name = input().split()
  
  zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))
