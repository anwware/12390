amount_rub = float(input("Введите сумму в рублях: "))


currency = input("Выберите валюту для конвертации (доллары, евро или юани): ")


usd_rate = 75.0
eur_rate = 90.0
cny_rate = 11.0


if currency == "доллары":
    amount_currency = amount_rub / usd_rate
    currency_symbol = "$"
elif currency == "евро":
    amount_currency = amount_rub / eur_rate
    currency_symbol = "€"
elif currency == "юани":
    amount_currency = amount_rub / cny_rate
    currency_symbol = "¥"
else:
    print("Выбрана неподдерживаемая валюта")
    exit()
print(f"{amount_rub} рублей = {amount_currency:.2f} {currency_symbol}")