#Exchange rate 

euro_rate = 0.88
usd_rate = 1

eur = 12.25
usd = 7.38

usd_to_eur = usd * euro_rate
eur_to_usd = usd / euro_rate


print("Hi, welcome to the usd to eur converter!")
print(usd, "Dollars is", round(usd_to_eur, 2), "euros.")
print(eur, "Euros is", round(eur_to_usd, 2), "dollars.")
print("Thank you.")
