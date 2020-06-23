
# Create A Basic Class
class Book():
    
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    def get_price(self):
        return self.price


# Create an instance of the class
b1 = Book("Brave New World","Leo Tolstoy", 1225, 39.95)
b2 = Book("War & Peace","JD Salinger",234,12.95)

print(b1.get_price())
print(b1.title)