class Shape:
   
   def __init__(self, width, height):
      self.width = width
      self.height = height

   def calculate_perimeter(self):
      return 2 * self.width + 2 * self.height

      
shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)