# pip install currencyconverter

from currency_converter import CurrencyConverter

# Initialize converter
c = CurrencyConverter()

# User input
amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD, EUR, TRY): ").upper()
to_currency = input("To currency (e.g., USD, EUR, TRY): ").upper()

try:
    converted = c.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
except Exception as e:
    print("Error:", e)
