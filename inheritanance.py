class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return"animal speaks"
class dog(animal):
    def __init__(self,name,bread):
        super().__init__(name)
        self.bread=bread
    def speak(self):
        return f"{self.name} the {self.bread} barks"
dog1=dog("appu","rot")
print(dog1.speak())