from test import cars, title
from jinja2 import Environment, FileSystemLoader

"""Загрузчики шаблонов. FileSystemLoader"""

"""Как применяется FileSystemLoader?  Допустим, есть готовый шаблон / HTML страница, в котором при помощи 
синтаксиса jinja прописали инструкции: макросы, блоки и другие операции с элементами. 
Так вот при помощи FileSystemLoader можно загрузить нужный шаблон, далее создать окружение и оперировать 
этими инструкциями."""

file_loader = FileSystemLoader(searchpath='templates')  # Указать путь к директории, где искать шаблоны
env = Environment(loader=file_loader)  # Создать окружение с этим загрузчиком
tm = env.get_template(name='test.html')  # Искать в окружении нужный шаблон по имени
result = tm.render(cars=cars,  title=title)
print(result)
# Записать результат в файл и посмотреть какое будет готовое представление
with open('test.html', 'w', encoding='utf-8') as file:
    file.write(result)

'''Полный список загрузчиков можно найти в документации
Если задуматься, теперь понятно как django распознает jinja инструкции внутри шаблонов'''

