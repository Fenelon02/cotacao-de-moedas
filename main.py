import requests

def currency_quote(link):
    headers = {}
    data = {}

    # Fetching data from the API
    response = requests.get(link, headers=headers, data=data)

    quotes_list = []
    items = response.json()

    # Parsing and organizing the response
    for key, value in items.items():
        quotes_list.append({
            'currency': key,
            'conversion_currency': value['name'],
            'current_price': float(value['bid'])
        })

    # Customizing display names for currencies
    for item in quotes_list:
        if item['currency'] == 'USDBRL':
            item['currency'] = 'US Dollar'
        if item['currency'] == 'EURBRL':
            item['currency'] = 'Euro'
        if item['currency'] == 'BTCBRL':
            item['currency'] = 'Bitcoin'

        if item['conversion_currency'] == 'Dólar Americano/Real Brasileiro':
            item['conversion_currency'] = 'US Dollar to Brazilian Real conversion'
        if item['conversion_currency'] == 'Euro/Real Brasileiro':
            item['conversion_currency'] = 'Euro to Brazilian Real conversion'
        if item['conversion_currency'] == 'Bitcoin/Real Brasileiro':
            item['conversion_currency'] = 'Bitcoin to Brazilian Real conversion'

    return quotes_list

# API link
link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
currencies = currency_quote(link)

# Printing the results
print('EXCHANGE RATE OF MAIN CURRENCIES')
for item in currencies:
    print(f"The {item['currency']} in the current exchange rate, in the {item['conversion_currency']}, is valued at R${item['current_price']:.2f}")
    print()
