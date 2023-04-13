from jinja2 import Template
from test import nums, cars

"""Тема: Фильтры и макросы: macro, call. Каждая ниже приведенная функция, демонстрирует определенную тему урока"""
"""На этом уроке много материала и разные темы, поэтому представления сделаны в виде функций"""


def demonstarate_sum() -> None:
    print('Фильтр sum для вычисления суммы указанных полей коллекции')
    print(*cars, sep='\n')
    print('''Синтаксис sum(iterable, attribute=None, start=0)''')
    sum_string = 'Суммарная цена автомобилей будет составлять: {{ cars | sum(attribute="price") }}'
    print(sum_string)
    tm = Template(sum_string)
    result = tm.render(cars=cars)
    print('[RESULT]:', result)
    print('_' * 80)
    sum_string = "Сумма чисел в списке: {{ nums | sum}}"
    print(sum_string)
    tm = Template(sum_string)
    result = tm.render(nums=nums)
    print('[RESULT 2]:', result)
    print('_' * 80)
    maxitem_string = "Элемент таблицы с максимальной ценой:  {{ cars | max(attribute='price')}}"
    print(maxitem_string)
    tm = Template(maxitem_string)
    result = tm.render(cars=cars)
    print('[RESULT 3]', result)
    print('_' * 80)


def demonstrate_filter_block() -> None:
    print("Применение фильтров в блоке filter")
    print("""Синтаксис:
    {% filter <filter name> %}
        <фрагмент к которому применяется фильтр>
    {% endfilter %}"""
          )
    tmpl = """
    <ul>
    {% for item in cars -%}
        {% filter lower %}<li>{{ item.brand }}</li>{% endfilter %}
    {% endfor -%}
    </ul"""
    print(tmpl)
    tm = Template(tmpl)
    result = tm.render(cars=cars)
    print('[RESULT 4]:', result)

    with open('test.html', 'w', encoding='utf-8') as file:
        file.write(result)

    print('''Существует множество фильтров. Полный список можно изучить в документации.''')
    print('_' * 80)


def demonstrate_macros() -> None:
    print("""Макросы — своеобразные функции, для избежания повторения кода; 
    прописываешь тело макроса с функционалом, но при рендере его не видно""")

    print("""Синтаксис:
    {% macro <macros name>(attributes) -%}
        <фрагмент кода куда подставляются атрибуты макроса>
    {% endmacro -%}"""
          )

    print('''Пример создания вложенных списков с помощью вложенного макроса call()''')

    html = """
        {% macro autos_list(cars)-%}
         <ul>
            {% for item in cars -%}
                <li>{{ item.brand }}</li> {{ caller(item) }}
            {% endfor -%}
         </ul>
        {% endmacro -%}
        
        {% call(item) autos_list(cars) -%}
            <ul>
                <li>model: {{ item.model }}</li>
                <li>price: {{ item.price }}</li>
            </ul>
        {% endcall -%}"""
    print(html)
    print('''Первый макрос создает главный список и внутри этого вызывает другой call(), 
    который отвечает за вложенный список.''')

    tm = Template(html)
    result = tm.render(cars=cars)
    print('[RESULT 5]:', result)

    with open('test.html', 'w', encoding='utf-8') as file:
        file.write(result)
    print('_' * 80)


def get_help() -> None:
    il = ('sum', 'macros', 'filter')
    print('Cписок доступных на этом уроке инструкций для демонстрации:')
    print(*il, sep='\n')
    print('_' * 80)


if __name__ == '__main__':
    while True:
        command = input('Введите название инструкции / help, чтобы увидеть список / break, чтобы выйти: ')
        if command == 'help':
            get_help()
        elif command == 'sum':
            demonstarate_sum()
        elif command == 'filter':
            demonstrate_filter_block()
        elif command == 'macros':
            demonstrate_macros()
        elif command == 'break':
            break
        else:
            print('Представления с таким названием не существует в этом уроке')
