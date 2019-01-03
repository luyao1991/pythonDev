# coding:utf-8


class Person:
    persition = 'teacher'
    def __new__(cls, *args, **kwargs):
        print('__new__方法被执行了')
        return object.__new__(cls)

    def __init__(self, age, sex):
        self.age = age
        self.sex = sex


person = Person(26, 'male')
print(person.persition)
print(person.sex)
person.age = 27
print(person.age)
person.sex = 'fmale'
print(person.sex)
