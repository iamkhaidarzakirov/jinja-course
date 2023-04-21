"""Экранирование и блоки raw, for, if"""
"""На этом уроке много материала и разные темы, поэтому представления сделаны в виде функций"""

from jinja2 import Template
from jinja2.filters import escape
from test import cities


def demonstarate_raw() -> None:
    print('Экранирование конструкций для вывода при помощи блока raw')
    print('''Синтаксис:
    {% raw %}
        <expression>
    {% endraw %}'''
          )

    data = """Модуль Jinja 
    вместо определения {{name}}
    подставляет указанное значение Antonio"""

    template = Template(data)
    msg = template.render(name='Antonio')
    print('[RESULT 1]:', msg)

    raw_data = """{% raw %}Теперь модуль Jinja 
    вместо определения {{name}}
    не подставляет значение Antonio{% endraw %}"""
    template = Template(raw_data)
    msg = template.render(name='Antonio')
    print('[RESULT 2]:', msg)
    print('_' * 80)


def demonstrate_escape() -> None:
    print("""Экранирование специальных символов, например тегов Html, чтобы в браузере отобразить их в первоначальном
    виде в виде текста при помощи блока e или функции escape()"""
          )
    print('Экранирование специальных символов. Функция escape()')
    # Неправильный вывод
    link = '''В HTML документе ссылки определяются так:
    <a href='#'>Ссылка</a>
    '''
    tm = Template(link)
    msg = tm.render()
    with open('test_wrong.html', 'w', encoding='utf-8') as file:  # Проверь сохраненную страницу
        file.write(msg)
    # С помощью инструкции е
    tm = Template('{{ link | e }}')
    msg = tm.render(link=link)
    with open('test_e.html', 'w', encoding='utf-8') as file:  # Проверь сохраненную страницу
        file.write(msg)

    '''Самое оптимальное решение при помощи функции escape()'''
    tm = escape(link)

    """Попробовать записать в файл и открыть в браузере, чтобы увидеть результат"""
    with open('test_escape.html', 'w', encoding='utf-8') as file:  # Проверь сохраненную страницу
        file.write(tm)
    print('Можете проверить результат HTML')
    print('_' * 80)


def demonstrate_for() -> None:
    print('Работа с блоком инструкций for')
    print('''Формирует список на основе итерируемого объекта. Синтаксис:
    {% for <expression> -%}
        <repeat>
    {% endfor -%}'''
          )

    '''Допустим есть некоторая таблица с данными и из них нужно сделать структуру HTML'''

    html_block = '''
    <select name="cities">
        {% for item in cities -%} 
            <option value="{{item['id']}}">{{item['city']}}</option>
        {% endfor -%}
    </select>'''

    tm = Template(html_block)
    msg = tm.render(cities=cities)
    """Попробовать записать в файл и открыть в браузере, чтобы увидеть результат"""
    with open('test.html', 'w', encoding='utf-8') as file:
        file.write(msg)
        print('Можете проверить результат HTML')
    print('_' * 80)


def demonstrate_if() -> None:
    """Простыми словами, аналогичный блок условий Python, только с немного другим синтаксисом"""
    print('Работа с блоком условий if')
    print('''Синтаксис:
    {% if <condition> %}
        <блок кода выполняется, если условие истинно>
    {% endif %}'''
          )

    html_block = '''
    <select name="cities">
        {% for item in cities -%}
            {% if item.name == 'Moscow' -%}  
                <option value="{{item['id']}}">{{item['city']}}(Capital of Russia)</option>
            {% elif item.name == 'Kazan' -%}
                <option value="{{item['id']}}">{{item['city']}}(Capital of Tatarstan)</option>
            {% else -%}
                <option value="{{item['id']}}">{{item['city']}}</option>
            
            {% endif -%}
        {% endfor -%}
    </select>'''

    tm = Template(html_block)
    msg = tm.render(cities=cities)
    """Попробовать записать в файл и открыть в браузере, чтобы увидеть результат"""
    with open('test.html', 'w', encoding='utf-8') as file:
        file.write(msg)
        print('Можете проверить результат HTML')
    print('_' * 80)


def get_help() -> None:
    il = ('raw', 'escape', 'for', 'if')
    print('Cписок доступных на этом уроке инструкций для демонстрации:')
    print(*il, sep='\n')
    print('_' * 80)


if __name__ == '__main__':
    while True:
        command = input('Введите название инструкции / help, чтобы увидеть список / break, чтобы выйти: ')
        if command == 'help':
            get_help()
        elif command == 'raw':
            demonstarate_raw()
        elif command == 'escape':
            demonstrate_escape()
        elif command == 'for':
            demonstrate_for()
        elif command == 'if':
            demonstrate_if()
        elif command == 'break':
            break
        else:
            print('Представления с таким названием не существует в этом уроке')
