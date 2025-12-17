import requests

# Посилання на API з параметрами за тиждень
url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240310&end=20240317&valcode=usd&sort=exchangedate&order=asc&json"

def get_nbu_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"{'Дата':<15} | {'Курс USD':<10}")
        print("-" * 30)
        for item in data:
            print(f"{item['exchangedate']:<15} | {item['rate']:<10} грн")
    else:
        print(f"Помилка: {response.status_code}")

if __name__ == "__main__":
    get_nbu_data()