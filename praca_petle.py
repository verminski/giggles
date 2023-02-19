wyslana_waga = 0
kontener_waga = 0
kontener_wyslane = 0
paczki_waga = 0
puste_kontener_kg = 0
puste_max_kg = 0
puste_kontener_max = 0

paczka_ilosc = int(input("Podaj liczbę paczek: "))

for paczka in range(1, paczka_ilosc +1):
    print("Podaj wagę paczki: ")
    paczki_waga = int(input())
    kontener_waga = kontener_waga + paczki_waga
    if paczki_waga > 10 or paczki_waga < 1:
        print("Błąd, waga paczki powinna być większa niż 1kg i mniejsza niż"
              " 10 kg, podaj dane ponownie.")
        break

    if kontener_waga > 20:
        kontener_wyslane += 1
        wyslana_waga += kontener_waga - paczki_waga
        puste_kontener_kg = kontener_waga - paczki_waga
        kontener_waga = paczki_waga
    elif kontener_waga == 20:
        kontener_wyslane += 1
        wyslana_waga += kontener_waga
        kontener_waga = 0
    elif paczka == paczka_ilosc:
        kontener_wyslane += 1
        wyslana_waga += kontener_waga
        if kontener_waga < 20:
            puste_kontener_kg = 20 - kontener_waga
    if puste_kontener_kg > puste_max_kg:
        puste_max_kg = puste_kontener_kg
        puste_kontener_max = kontener_wyslane

suma_pustej_wagi = 20*kontener_wyslane - wyslana_waga

print(f"Wysłano łącznie {kontener_wyslane} kontener/kontenerów.")
print(f"Wysłano łącznie {wyslana_waga}kg")
print(f"Suma pustych kilogramów: {suma_pustej_wagi}kg")
print(f"Najwięcej pustych kilogramów ma kontener: {puste_kontener_max}"
      f" ({puste_max_kg}kg)")

