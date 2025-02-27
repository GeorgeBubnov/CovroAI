"""
frontend.py

Модуль управления интерфейсом пользователя.
Реализует взаимодействие через Flask + React.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    """
    Главная страница веб-интерфейса.
    """
    return render_template("index.html")

@app.route("/user_input", methods=["POST"])
def get_user_input():
    """
    Получает данные от пользователя.

    :return: JSON-ответ о статусе приёма данных.
    :rtype: dict
    """
    data = request.json
    return {"status": "received", "data": data}

@app.route("/feedback", methods=["POST"])
def send_feedback():
    """
    Отправляет обратную связь от пользователя.

    :return: JSON-ответ о статусе приёма обратной связи.
    :rtype: dict
    """
    feedback = request.json
    return {"status": "feedback received", "message": feedback}

def start_frontend():
    """
    Запуск веб-приложения.
    """
    app.run(debug=True)
