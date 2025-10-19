class Dog:
    spices = 'husky' #attribute
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self): #class method, always takes first param as self. self is like Hey you do this action
        print('woof')
        
#instatiation

# my_dog = Dog()
# my_dog.bark()

miko = Dog('Miko',1)

print(miko.age)

class Book: 
    def __init__(self, book, author):
        self.book = book
        self.author = author
        
    def __str__(self):
        return (f"The book's name is {self.book}, written by {self.author}")
        
book1 = Book('Deep work', 'Cal Newport')
print(book1)