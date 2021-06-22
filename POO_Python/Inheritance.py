class Rectangle:
    def __init__(self, width , length ) :
        self.width= width
        self.length = length
    def area (self):
        return self.width*self.length
class Square(Rectangle):
    def __init__(self,width ) -> None:
        super().__init__(width,width)

if __name__=='__main__':
    rectangle=Rectangle(3,4)
    print(rectangle.area())
    square=Square(5)
    print(square.area())

