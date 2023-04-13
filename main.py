from jinja2 import Template

"""Использование {{}} в шаблонах. Сравнение f'{}' с шаблонизатором. Простейший функционал.

{{}} — принимает в себя  любые  конструкции Python / переменные, экземпляры классов, ключи словарей...
{% %} — спецификатор шаблона
{# #} — блок комментариев
# ## — строковый комментарий"""


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def give_regards(self):
        message = f'{self.name} gives you regards!'
        return message


p1 = Person(name='Antonio', age=47)

tm = Template('My name is {{p.name}} and I am {{p.age}}. {{p.give_regards()}}')
jinja_msg = tm.render(p=p1)
print('[RESULT 1]:', jinja_msg)

f_msg = f'My name is {p1.name} and I am {p1.age}. {p1.give_regards()}'
print('[RESULT 2]:', f_msg)

"""К ключу словаря в jinja можно обращаться через точку, как к атрибуту класса"""
