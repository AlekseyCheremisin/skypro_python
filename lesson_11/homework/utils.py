import json

# Список кандидатов.
candidates = []


def load_candidates_from_json(path: str):
    """
    Функция читает из json файла список словарей кандидатов.
    :param path: путь до файла json.
    :return: список словарей с данными кандидатов.
    """
    global candidates
    with open(path, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates

def get_candidate(candidate_id):
    """
    Функция поиска кандидата по его id.
    :param candidate_id: id кандидата.
    :return: словарь с данными о кандидате.
    Если поиск не дал результатов, то возвращаем
    словарь вида:
    {"missing": "Кандидат отсутствует"}
    """
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return {"missing": "Кандидат отсутствует"}

def get_candidates_by_name(candidate_name):
    """
    Функция поиска кандидатов по имени или части имени.
    :param candidate_name: имя кандидата или его часть.
    :return: Если получилось найти кандидатов,
    то возвращаем список словарей с данными кандидатов.
    Если поиск не дал результатов, то словарь вида:
    {"missing": "Кандитатов по этому имени не найдено"}
    """
    list_by_name = []
    for candidate in candidates:
        if candidate_name.lower() in str(candidate['name']).lower():
            list_by_name.append(candidate)
    if len(list_by_name) == 0:
        return {"missing": "Кандитатов по этому имени не найдено"}
    return list_by_name

def get_candidates_by_skill(skill_name: str):
    """
    Функция поиска кандидатов по навыкам.
    :param skill_name: искомый навык.
    :return: Если получилось найти кандидатов,
    то возвращаем список словарей с данными кандидатов.
    Если поиск не дал результатов, то словарь вида:
    {"missing": "Кандитатов по этому навыку не найдено"}
    """
    list_by_skill = []
    for candidate in candidates:
        if skill_name.lower() in str(candidate['skills']).lower():
            list_by_skill.append(candidate)
    if len(list_by_skill) == 0:
        return {"missing": "Кандитатов по этому навыку не найдено"}
    return list_by_skill


if __name__ == '__main__':
    l = load_candidates_from_json("data/candidates.json")
    assert l[0]['id'] == 1
    assert l[6]['age'] == 33

    c = get_candidate(2)
    assert c['name'] == 'Sheri Torres'

    c = get_candidate(0)
    assert c['missing'] == 'Кандидат отсутствует'

    lc = get_candidates_by_name("st")
    assert lc[0]['name'] == 'Burt Stein'
    assert lc[1]['name'] == 'Austin Cochran'

    lc = get_candidates_by_name("Totoro")
    assert lc['missing'] == 'Кандитатов по этому имени не найдено'

    ls = get_candidates_by_skill("python")
    assert ls[0]['id'] == 1
    assert ls[1]['id'] == 6
    assert ls[2]['id'] == 7

    ls = get_candidates_by_skill("spanghew")
    assert lc['missing'] == 'Кандитатов по этому имени не найдено'