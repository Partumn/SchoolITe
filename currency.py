exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "RUB": 75.0,
    "GBP": 0.73,
    "JPY": 145.0,
}

def convert(amount, from_currency, to_currency):
    """Конвертирует сумму из одной валюты в другую"""
    # Проверяем, есть ли валюты в списке
    if from_currency not in exchange_rates:
        return f"Валюта {from_currency} не поддерживается"
    if to_currency not in exchange_rates:
        return f"Валюта {to_currency} не поддерживается"
    
    # Вычисляем курс
    rate_from = exchange_rates[from_currency]
    rate_to = exchange_rates[to_currency]
    
    # Конвертируем
    result = amount * (rate_to / rate_from)
    return round(result, 2)
