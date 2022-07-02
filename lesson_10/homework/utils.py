import requests

def load_candidates_list(url : str):
    """
    Функция загружающая из полученного по URL JSON-файла список словарей.
    :param url: Ссылка на JSON-файл со списком словарей.
    :return: Список словарей.
    """
    response = requests.get(url)
    data = response.json()

    return data