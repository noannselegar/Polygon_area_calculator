class Rectangle():
    def __init__(self, width=10, height=3):
        self.width = width
        self.height = height
        self.area = self.width * self.height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h

    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = 2*self.width + 2*self.height
        return self.perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return self.diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return '\nRectangle too big for picture'
        else:
            picture = str()
            for i in range(self.height):
                picture += f"{'*'.center(self.width, '*')}\n"
            return picture
        
    def get_amount_inside(self, shape):
        res = (self.width // shape.width)*(self.height // shape.height)
        return res
        
class Square(Rectangle):
    def __init__(self, side=5):
        self.width = side
        self.height = side
        self.area = self.width**2
    
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, w):
        self.width = w
        self.height = w
    
    def set_height(self, h):
        self.height = h
        self.width = h