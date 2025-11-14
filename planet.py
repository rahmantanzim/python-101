class Planet:
    # Class attributes, shared by all planets
    star = "Sun"
    
    def __init__(self,name,radius):
        # Instance attributes, unique for each planet
        self.name = name
        self.radius = radius
        
# Creating objects

earth = Planet("Earth", 6371)
jupiter = Planet("Jupiter", 69911)

# Output class attribute
print(Planet.star)
print(earth.star)

# Output instance attribute
print(earth.name)
print(jupiter.radius)



 
        