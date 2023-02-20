# by Kami Bigdely
# Extract superclass.
class Circle:
    
    def __init__(self, x, y, r, visible = True):
      self.center_x = x
      self.center_y = y
      self.r = r
      self.visible = visible
      
    def display(self):
        print('drew the circle.')
        
    def set_visible(self,is_visible):
        self.visible = is_visible
        
    def get_center(self):
        return self.center_x, self.center_y

# create a class rectangle that is a superclass of circle

class Rectangle(Circle):
    def __init__(self, x, y, width, height, visible = True):
        super().__init__(x, y, width, visible)
        self.height = height
        
    def display(self):
        print('drew the rectangle.')
        
    def get_center(self):
        return self.center_x + self.r/2, \
               self.center_y + self.height/2




if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visible(True)
    circle.display()
    print('center point',circle.get_center())


    rect = Rectangle(10, 10, 20, 5)
    rect.set_visible(False)
    rect.display() # does not display because it's hidden.
    rect.set_visible(True)
    rect.display()

    print('center point',rect.get_center())