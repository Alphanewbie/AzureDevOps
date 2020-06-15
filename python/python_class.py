# class Dog :
#     kind = 'canine'
#     def __init__(self,name) :
#         self.name = name

# my_dog = Dog('namu')
# your_dog = Dog('gazi')
# print(my_dog.kind)
# print(your_dog.kind)
# print(my_dog.name)
# print(your_dog.name)


# class Dog:
#     # 모든 클래스가 공유하는 값이다. - 그래서 이름이 클래스 변수
#     tricks = []

#     def __init__(self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)


# my_dog = Dog('namu')
# your_dog = Dog('gazi')

# my_dog.add_trick('hello')
# your_dog.add_trick('byebye')

# print(my_dog.tricks)
# print(your_dog.tricks)


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


my_dog = Dog('namu')
your_dog = Dog('gazi')

my_dog.add_trick('hello')
your_dog.add_trick('byebye')

print(my_dog.tricks)
print(your_dog.tricks)

# print(help(str))
print(help(str.capitalize))

# 우리가 사용할땐 이런 형태지만
# 단축형
'apple'.capitalize()

# 실제로는 작동되는 방식
str.capitalize('apple')

# 절차 지향 vs 객체 지향
# 데이터가 흘러 다니는 것으로 보는 시각 ->  데이터가 중심이 되는 시각

# 절차 지향
# 데이터가 변수에 들어가고
def greeting(name) :
    return f'hello, {name}'

print(greeting('harry'))

# 객체 지향
# 데이터가 중심이 되는 시각
class Person :
    def __init__(self,name):
        self.name = name

    def greeting(self) :
        return f'hello, {self.name}'

my_var = Person('harry')
print(my_var.greeting())