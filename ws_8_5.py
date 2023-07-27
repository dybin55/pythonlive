class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):    
    sound = '멍멍'

    def bark(self): 
        """
        왜 self가 꼭 들어가야하지? 밑의 함수에는 안들어가도 되는데?
        """
        print('멍멍!')



class Cat(Animal):
    sound = '야옹'
    # def __init__(self, sound):
    #     self.sound = sound

    def meow(self):
        print('야옹!')


class Pet(Dog, Cat):
    def access_num_of_animal():
       return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'
    
    def __str__(self):
        return f'애완동물은 {super().sound}소리를 냅니다.'

    # def make_sound(self):
    #     print(self.sound)

    # def play(self):
    #     print('애완동물과 놀기')

pet_1 = Pet()
pet_2 = Pet()
print(pet_1)
print(pet_2)