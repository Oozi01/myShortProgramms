from locale import currency


availableCurrencies = ['EUR', 'USD', 'PLN', 'GBP', 'CAD', 'AUD', 'JPY', 'INR', 'NZR', 'CHF']

print(f'Currently available Currencies: {availableCurrencies}')



def converter(currency1, amountOfMoney, currency2):
    if currency1 == 'EUR':
        if currency2 == 'USD':
            convertedMoney = amountOfMoney * 1.05
            return f'{convertedMoney} USD'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 4.62
            return f'{convertedMoney} PLN'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.84
            return f'{convertedMoney} GBP'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 1.35
            return f'{convertedMoney} CAD'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 1.50
            return f'{convertedMoney} AUD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 135.0
            return f'{convertedMoney} JPY'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 82.21
            return f'{convertedMoney} INR'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 1.64
            return f'{convertedMoney} NZD'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 1.02
            return f'{convertedMoney} CHF'
    elif currency1 == 'USD':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 0.94
            return f'{convertedMoney} EUR'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 4.38
            return f'{convertedMoney} PLN'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.80
            return f'{convertedMoney} GBP'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 1.28
            return f'{convertedMoney} CAD'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 1.42
            return f'{convertedMoney} AUD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 127.88
            return f'{convertedMoney} JPY'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 77.86
            return f'{convertedMoney} INR'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 1.56
            return f'{convertedMoney} NZD'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 0.97
            return f'{convertedMoney} CHF'
    elif currency1 == 'PLN':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 0.21
            return f'{convertedMoney} EUR'
        elif currency2 == 'USD':
            convertedMoney = amountOfMoney * 0.22
            return f'{convertedMoney} USD'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.18
            return f'{convertedMoney} GBP'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 0.29
            return f'{convertedMoney} CAD'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 0.32
            return f'{convertedMoney} AUD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 29.19
            return f'{convertedMoney} JPY'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 17.77
            return f'{convertedMoney} INR'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 0.35
            return f'{convertedMoney} NZD'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 0.22
            return f'{convertedMoney} CHF'
    elif currency1 == 'GBP':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 1.18
            return f'{convertedMoney} EUR'
        elif currency2 == 'USD':
            convertedMoney = amountOfMoney * 1.24
            return f'{convertedMoney} USD'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 5.47
            return f'{convertedMoney} PLN'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 1.60
            return f'{convertedMoney} CAD'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 1.77
            return f'{convertedMoney} AUD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 159.75
            return f'{convertedMoney} JPY'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 97.27
            return f'{convertedMoney} INR'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 1.95
            return f'{convertedMoney} NZD'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 1.21
            return f'{convertedMoney} CHF'
    elif currency1 == 'CAD':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 0.73
            return f'{convertedMoney} EUR'
        elif currency2 == 'USD':
            convertedMoney = amountOfMoney * 0.77
            return f'{convertedMoney} USD'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 3.41
            return f'{convertedMoney} PLN'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.62
            return f'{convertedMoney} GBP'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 1.10
            return f'{convertedMoney} AUD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 99.68
            return f'{convertedMoney} JPY'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 60.69
            return f'{convertedMoney} INR'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 1.21
            return f'{convertedMoney} NZD'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 0.75
            return f'{convertedMoney} CHF'
    elif currency1 == 'AUD':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 0.66
            return f'{convertedMoney} EUR'
        elif currency2 == 'USD':
            convertedMoney = amountOfMoney * 0.70
            return f'{convertedMoney} USD'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 3.08
            return f'{convertedMoney} PLN'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.56
            return f'{convertedMoney} GBP'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 0.90
            return f'{convertedMoney} CAD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 89.99
            return f'{convertedMoney} JPY'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 54.79
            return f'{convertedMoney} INR'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 1.09
            return f'{convertedMoney} NZD'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 0.68
            return f'{convertedMoney} CHF'
    elif currency1 == 'JPY':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 0.0074
            return f'{convertedMoney} EUR'
        elif currency2 == 'USD':
            convertedMoney = amountOfMoney * 0.0078
            return f'{convertedMoney} USD'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 0.0342
            return f'{convertedMoney} PLN'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.0062
            return f'{convertedMoney} GBP'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 0.0100
            return f'{convertedMoney} CAD'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 0.0111
            return f'{convertedMoney} AUD'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 0.6089
            return f'{convertedMoney} INR'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 0.0122
            return f'{convertedMoney} NZD'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 0.0076
            return f'{convertedMoney} CHF'
    elif currency1 == 'INR':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 0.0121
            return f'{convertedMoney} EUR'
        elif currency2 == 'USD':
            convertedMoney = amountOfMoney * 0.0128
            return f'{convertedMoney} USD'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 0.0562
            return f'{convertedMoney} PLN'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.0102
            return f'{convertedMoney} GBP'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 0.0164
            return f'{convertedMoney} CAD'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 0.0182
            return f'{convertedMoney} AUD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 1.64
            return f'{convertedMoney} JPY'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 0.0200
            return f'{convertedMoney} NZD'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 0.0125
            return f'{convertedMoney} CHF'
    elif currency1 == 'NZD':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 0.60
            return f'{convertedMoney} EUR'
        elif currency2 == 'USD':
            convertedMoney = amountOfMoney * 0.64
            return f'{convertedMoney} USD'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 2.80
            return f'{convertedMoney} PLN'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.51
            return f'{convertedMoney} GBP'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 0.82
            return f'{convertedMoney} CAD'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 0.91
            return f'{convertedMoney} AUD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 81.91
            return f'{convertedMoney} JPY'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 49.87
            return f'{convertedMoney} INR'
        elif currency2 == 'CHF':
            convertedMoney = amountOfMoney * 0.62
            return f'{convertedMoney} CHF'
    elif currency1 == 'CHF':
        if currency2 == 'EUR':
            convertedMoney = amountOfMoney * 0.97
            return f'{convertedMoney} EUR'
        elif currency2 == 'USD':
            convertedMoney = amountOfMoney * 1.02
            return f'{convertedMoney} USD'
        elif currency2 == 'PLN':
            convertedMoney = amountOfMoney * 4.49
            return f'{convertedMoney} PLN'
        elif currency2 == 'GBP':
            convertedMoney = amountOfMoney * 0.82
            return f'{convertedMoney} GBP'
        elif currency2 == 'CAD':
            convertedMoney = amountOfMoney * 1.31
            return f'{convertedMoney} CAD'
        elif currency2 == 'AUD':
            convertedMoney = amountOfMoney * 1.45
            return f'{convertedMoney} AUD'
        elif currency2 == 'JPY':
            convertedMoney = amountOfMoney * 131.20
            return f'{convertedMoney} JPY'
        elif currency2 == 'INR':
            convertedMoney = amountOfMoney * 79.88
            return f'{convertedMoney} INR'
        elif currency2 == 'NZD':
            convertedMoney = amountOfMoney * 1.60
            return f'{convertedMoney} NZD'
        
    
        


print(converter('PLN', 500, 'USD'))