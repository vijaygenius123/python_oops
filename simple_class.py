
# Create A Basic Class
class Book():
    
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    def get_price(self):
        if hasattr(self,'_discount'):
            return self.price - (self.price * self._discount)
        return self.price

    def set_discount(self,amount):
        self._discount = amount 

# Create an instance of the class
b1 = Book("Brave New World","Leo Tolstoy", 1225, 39.95)
b2 = Book("War & Peace","JD Salinger",234,12.95)

print(b1.get_price())
print(b1.title)
b1.set_discount(0.25)
print(b1.get_price())