from currency import convert, exchange_rates

def main():
    print("Доступные валюты:", list(exchange_rates.keys()))
    
    # Ввод данных
    amount = float(input("Сумма: "))
    from_currency = input("Из какой валюты (например USD): ").upper()
    to_currency = input("В какую валюту (например EUR): ").upper()
    
    # Конвертация
    result = convert(amount, from_currency, to_currency)
    
    # Вывод
    if isinstance(result, float):
        print(f"{amount} {from_currency} = {result} {to_currency}")
    else:
        print(result)

if __name__ == "__main__":
    main()
