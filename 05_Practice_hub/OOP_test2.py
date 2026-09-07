class Animal():
    zoo_name = "Madagaskar"
    def __init__(self , name , species , age , sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        print(f"The sound of animal is : {self.sound}")

    def info(self):
        print(f"Zoo: {Animal.zoo_name}")  # Access class attribute
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Sound: {self.sound}")
        
class Bird(Animal):
    def __init__(self, name, species, age, sound , wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span


sample1 = Animal("Lion" , 1 , 30 , "HP")

# print(f"The information is : \nname: {sample1.name} \nspecies: {sample1.species} \nage: {sample1.age} \nsound: {sample1.sound}")


sample1.make_sound()
sample1.info()

sample2 = Bird("Sparrow" , 2 , 2 , "VHP" , 10)

sample2.info()