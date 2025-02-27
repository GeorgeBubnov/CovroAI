"""
dashboard.py

Модуль визуализации данных и статистики.
Отображает графики, диаграммы и основные метрики.
"""

import matplotlib.pyplot as plt
import csv

class Dashboard:
    def __init__(self):
        """
        Инициализация модуля дашборда.
        """
        pass

    def display_metrics(self, data):
        """
        Отображает ключевые показатели.

        :param data: Словарь с метриками сайта.
        :type data: dict
        """
        print("Отображение ключевых показателей...")
        plt.figure()
        plt.plot(data.get("traffic", []))
        plt.show()

    def generate_report(self, data):
        """
        Создает текстовый отчет по аналитике.

        :param data: Словарь с аналитикой.
        :type data: dict
        :return: Текстовый отчет.
        :rtype: str
        """
        report = f"Трафик: {data.get('traffic', 0)}\nПоказатель отказов: {data.get('bounce_rate', 0)}%"
        print(report)
        return report

    def export_to_csv(self, data, filename="report.csv"):
        """
        Экспортирует данные в CSV-файл.

        :param data: Словарь с аналитикой.
        :type data: dict
        :param filename: Название файла.
        :type filename: str
        """
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Метрика", "Значение"])
            for key, value in data.items():
                writer.writerow([key, value])
        print(f"Данные сохранены в {filename}")
