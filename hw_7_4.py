class Person:
   count = 0

   def __init__(self, name, age):
      self.name = name
      self.age = age
      Person.count += 1

   def introduce(self):
      print(f'제 이름은 {self.name}이고, 저는 {self.age}살 입니다')

   @classmethod
   def number_of_people(clr):
      print(clr.count)
    

person1 = Person("Alice", 25)
person1.introduce()
Person.number_of_people()


# print(Person.number_of_people())
# print(Person.count)
