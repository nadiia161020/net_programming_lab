from flask import Flask, request

app = Flask(__name__)

@app.route("/currency")
def get_currency():
    # Отримуємо параметр 'today'
    today = request.args.get('today')
    # Повертаємо статичне значення
    return "USD - 41,5"

if __name__ == '__main__':
    app.run(port=8000)