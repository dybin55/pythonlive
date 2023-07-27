class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):    
    def bark(self): 
        """
        왜 self가 꼭 들어가야하지? 밑의 함수에는 안들어가도 되는데?
        """
        print('멍멍!')



class Cat(Animal):
    pass


class Pet(Dog, Cat):
   def access_num_of_animal():
       return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'


dog1 = Dog()
dog1.bark()
