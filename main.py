import requests

def cotacao(link):

    headers = {}
    dados = {}

    requisicao = requests.get(link, headers=headers, data=dados)

    lista = []
    itens = requisicao.json()

    for key, value in itens.items():
        lista.append({
            'moeda': key,
            'moeda_de_coversao': value['name'],
            'preco_atual': float(value['bid'])
        })

        
    for item in lista:
        if item['moeda'] == 'USDBRL':
            item['moeda'] = 'Dólar americano'
        if item['moeda'] == 'EURBRL':
            item['moeda'] = 'Euro'
        if item['moeda'] == 'BTCBRL':
            item['moeda'] = 'Bitcoin'

        if item['moeda_de_coversao'] == 'Dólar Americano/Real Brasileiro':
            item['moeda_de_coversao'] = 'conversão do Dólar Americano para Real'
        if item['moeda_de_coversao'] == 'Euro/Real Brasileiro':
            item['moeda_de_coversao'] = 'conversão de Euro para Real'
        if item['moeda_de_coversao'] == 'Bitcoin/Real Brasileiro':
            item['moeda_de_coversao'] = 'conversao de Bitcoin para Real'

    return lista


link = " https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
moedas = cotacao(link)

print('COTAÇÃO DAS PRINCIPAIS MOEDAS')
for item in moedas:
    print(f'O {item['moeda']} na cotação atual, na {item['moeda_de_coversao']}, está valendo R${item['preco_atual']:.2f}')
    print()
