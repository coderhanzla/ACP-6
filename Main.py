class square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Square : " ,self.side*4)

class rectangle:
       def __init__(self, height , width):
        self.height = height
        self.width = width

       def area(self):
          print("rectangle : ", self.height* self.width)

sq = square(7)
re = rectangle(10 , 17)

for shape in (sq , re):
    shape.area()