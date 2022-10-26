import view as v
from get_data import data_export as de


def search(key_word):
    array = de()
    res = []
    for line in array:
        if key_word in line:
            res.append(line)

    if not res:
        print('Совпадений не найдено')
    else:
        return res


def dep_choice(id: str):
    departments = {"1": "отдел_продаж",
                   "2": "отдел_финансов",
                   "3": "отдел_кадров",
                   "4": "отдел_маркетинга",
                   "5": "отдел_продукта"}
    return departments[id]


def pos_choice(id: str):
    positions = {"1": "ген.директор",
                 "2": "руководитель",
                 "3": "менеджер",
                 "4": "специалист"}
    return positions[id]
