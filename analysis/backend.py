"""
backend.py

Модуль управления данными и логикой приложения.
"""

class Backend:
    def __init__(self):
        """
        Инициализация модуля бекенда.
        """
        self.data_storage = {}

    def process_data(self, raw_data):
        """
        Обрабатывает входные данные.

        :param raw_data: Сырой HTML или JSON с сайта.
        :type raw_data: str
        :return: Обработанные данные.
        :rtype: dict
        """
        return {"processed": True, "data": raw_data}

    def store_data(self, key, value):
        """
        Сохраняет данные в памяти.

        :param key: Ключ для хранения данных.
        :type key: str
        :param value: Значение.
        :type value: any
        """
        self.data_storage[key] = value
        print(f"Данные сохранены под ключом {key}")

    def fetch_data(self, key):
        """
        Получает данные по ключу.

        :param key: Ключ.
        :type key: str
        :return: Запрашиваемые данные.
        :rtype: any
        """
        return self.data_storage.get(key, "Нет данных")
