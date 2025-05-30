class Dog:
    species = "animal"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

jolly = Dog("jolly", "Russian Chow-Chow")
gabrial = Dog("gabrial", "German Shepherd")
print("jolly is a", jolly.species)
print("gabrial is a", gabrial.species)
print("jolly is a {} ".format(jolly.species))
print("gabrial is also a {} ".format(gabrial.species))

print("{} breed {} ".format(jolly.name, jolly.breed))
print("{} breed {} ".format(gabrial.name, gabrial.breed))