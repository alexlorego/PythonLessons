from tabulate import tabulate
from get_data import data_export as de


def show_data(data_array: list):
    col_names = ["ID", "Имя", "Фамилия", "Корп.почта", "Отдел", "Должность"]
    print(tabulate(data_array, headers=col_names, tablefmt="fancy_grid"))


def show_dep():
    departments = [[1, "Отдел продаж"], [2, "Отдел финансов"], [3, "Отдел кадров"],
                   [4, "Отдел маркетинга"], [5, "Отдел продукта"]]
    col_names = ["ID", "Отдел"]
    print(tabulate(departments, headers=col_names, tablefmt="fancy_grid"))


def show_pos():
    positions = [[1, "Ген.директор"], [2, "Руководитель"], [3, "Менеджер"],
                 [4, "Специалист"]]
    col_names = ["ID", "Должность"]
    print(tabulate(positions, headers=col_names, tablefmt="fancy_grid"))
