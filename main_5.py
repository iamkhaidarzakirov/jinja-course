from jinja2 import Environment, FileSystemLoader

'''Загрузчики. Конструкции include / import'''

'''Синтаксис:
{% include <template path> %}'''

'''Позволяет подключать к шаблону другие шаблоны. Например, header и footer сайта обычно неизменны.
Их удобно подключать, чем прописывать один и тот же код в каждом шаблоне'''

'''import мало чем отличается от одноименной инструкции в Python. Выполняет те же функции импорта
функционала из указанного шаблона. Если в Python импортируешь модуль, здесь шаблон'''

'''Синтаксис:
{% import 'test.html' as test %} 
{% from 'test.html' import some_macro as macro %}'''

some_list = [1, 2, 3, 4, 5]
file_loader = FileSystemLoader(searchpath='templates')
env = Environment(loader=file_loader)
tm = env.get_template(name='content.html')
result = tm.render(list_table=some_list)

print(result)

