
# Create A Basic Class
class Book():
    
    def __init__(self, title):
        self.title = title


# Create an instance of the class
b1 = Book("Brave New World")
b2 = Book("War & Peace")

print(b1)
print(b1.title)