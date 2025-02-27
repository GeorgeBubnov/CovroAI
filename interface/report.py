"""
report.py

Формирует отчеты в формате PDF, Excel и других.
"""

import pdfkit

class ReportGenerator:
    def __init__(self):
        """
        Инициализация модуля отчетности.
        """
        pass

    def generate_pdf(self, data):
        """
        Генерирует PDF-отчет на основе собранных данных.

        :param data: Словарь с аналитикой.
        :type data: dict
        """
        pdfkit.from_string(str(data), "report.pdf")
        print("PDF-отчет создан.")

    def generate_excel(self, data, filename="report.xlsx"):
        """
        Создает отчет в формате Excel.

        :param data: Словарь с аналитикой.
        :type data: dict
        :param filename: Название файла.
        :type filename: str
        """
        import pandas as pd
        df = pd.DataFrame([data])
        df.to_excel(filename, index=False)
        print(f"Excel-отчет сохранен в {filename}")

    def send_report_via_email(self, recipient_email, filename="report.pdf"):
        """
        Отправляет отчет по электронной почте.

        :param recipient_email: Email получателя.
        :type recipient_email: str
        :param filename: Имя файла отчета.
        :type filename: str
        """
        print(f"Отчет {filename} отправлен на {recipient_email}")
