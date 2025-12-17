import requests
import matplotlib.pyplot as plt

url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240310&end=20240317&valcode=usd&sort=exchangedate&order=asc&json"


def build_chart():
    data = requests.get(url).json()
    dates = [item['exchangedate'] for item in data]
    rates = [item['rate'] for item in data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, marker='o', linestyle='-', color='b')
    plt.title('Курс долара США (USD) за тиждень')
    plt.xlabel('Дата')
    plt.ylabel('Курс гривні')
    plt.grid(True)
    plt.xticks(rotation=45)

    # Зберігаємо графік як картинку в папку Pictures
    plt.savefig('Pictures/task3_.png')
    plt.show()


if __name__ == "__main__":
    build_chart()
