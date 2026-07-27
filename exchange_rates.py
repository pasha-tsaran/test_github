import requests

url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url, timeout=10)
response.raise_for_status()
rates = response.json()["Valute"]
for code in ("USD", "EUR"):
    print(f"{code}: {rates[code]['Value'] / rates[code]['Nominal']:.4f} RUB")
