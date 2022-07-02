from flask import Flask

import utils

# Получаем список кандидатов.
candidates = utils.load_candidates_list('https://jsonkeeper.com/b/S2R5')

# Создаем приложение.
app = Flask(__name__)

@app.route('/')
def page_index():
    """
    Представление для главной страницы.
    :return: Выводим на главную страницу список кандидатов, следующим образом:
        Имя кандидата -
        Позиция кандидата
        Навыки через запятую
    """
    content = ""
    for person in candidates:
        content += f"{person['name']} - <br>{person['position']}<br>{person['skills']}<br><br>"

    return content

@app.route('/candidate/<int:id>')
def candidate(id: int):
    """
    Представление для страницы кандидата /candidate/id.
    :param id: Номер профиля кандидата.
    :return: Выводим на страницу картинку из профиля и информацию по кандидату в виде:
        Имя кандидата -
        Позиция кандидата
        Навыки через запятую
    """
    content = ""
    for person in candidates:
        if id == int(person['id']):
            content = f'<img src={person["picture"]}><br><br>{person["name"]} - <br>{person["position"]}<br>{person["skills"]}'

    return content

@app.route('/skill/<skill>')
def skill(skill: str):
    """
    Представление для страницы навыков /skill/skill.
    :param skill: Навык по которому будем искать кандидатов.
    :return: Выводим на страницу всех кандидатов у которых есть этот навык в виде:
        Имя кандидата -
        Позиция кандидата
        Навыки через запятую
    """
    content = ""
    for person in candidates:
        skills = str(person['skills']).lower().split(', ')
        if skill.lower() in skills:
            content += f"{person['name']} - <br>{person['position']}<br>{person['skills']}<br><br>"

    return content

app.run()