
# Lukas Spencer

# 10/22/2022

# The "class shark" is the blueprint created by a programmer for an object

class Shark:
    def __init__(self, name):
        self.name = name
        
# here we are telling our progam what we want our "sharks" to do (so for an example "def swim" is telling an object what it is doing)

    def be_wild(self):
        print(self.name + " is being wild.")
        
    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")
        
        
# Here we are telling our progam which shark is doing what, (example: sammy is being awesome is for Sammy and not Stevie)

def main():
    Lukas = Shark("Lukas")
    Lukas.be_wild()
    sammy = Shark("Sammy")
    sammy.be_awesome()
    stevie = Shark("Stevie")
    stevie.swim()
    
# this code is like the finishing touch, this code tells our progam to read the code and spit out an answer for us 

if __name__ == "__main__":
  main()
