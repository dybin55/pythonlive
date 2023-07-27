# ws_7_4.py

# 아래 클래스를 수정하시오.

class Shape:
   
    def __init__(self, width, height):
      self.width = width
      self.height = height
      # self.area = self.width * self.height
      self.area = self.calculate_area()
      self.perimeter = self.calculate_perimeter() 

    def calculate_area(self):
      area = self.width * self.height
      return area
   
    def calculate_perimeter(self):
      perimeter = 2 * self.width + 2 * self.height   
      return perimeter

    def print_info(self):
#       print(f'''Width : {self.width}
# Height : {self.height}''')
      print(f'Width : {self.width}\n'
            f'Height : {self.height}\n'
            f'Area : {self.area}\n'
            f'Width : {self.perimeter}')

      # print(f'Width : {self.width} \n
      #       Height : {self.height} \n
      #       Area : {self.area} \n
      #       Width : {self.perimeter}')

shape1 = Shape(5, 3)
shape1.print_info()