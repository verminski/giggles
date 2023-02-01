
# Poz - Pozyczka - Kwota raty w danym miesiacu
# Roz - Roznica - Roznica miedzy X a Y
# "Styczen2021" - Rok 1, "Styczen2022" - Rok 2

pozyczka = 12000
rata = 200
proc = 3

InfStyczen = 1.592824484
InfLuty = -0.453509101
InfMarzec = 2.324671717
InfKwiecien = 1.261254407
InfMaj = 1.782526286
InfCzerwiec = 2.329384541
InfLipiec = 1.502229842
InfSierpnien = 1.782526286
InfWrzesien = 2.328848994
InfPazdziernik = 0.616921348
InfListopad = 2.352295886
InfGrudzien = 0.337779545
InfStyczen2 = 1.577035247
InfLuty2 = -0.292781443
InfMarzec2 = 2.48619659
InfKwiecien2 = 0.267110318
InfMaj2 = 1.417952672
InfCzerwiec2 = 1.054243267
InfLipiec2 = 1.480520104
InfSierpnien2 = 1.577035247
InfWrzesien2 = -0.07742069
InfPazdziernik2 = 1.165733399
InfListopad2 = -0.404186718
InfGrudzien2 = 1.499708521

#Styczen2021
PozSty = ((1+((InfStyczen+proc)/pozyczka))*pozyczka-rata)
RozSty = pozyczka - PozSty
#Luty2021
PozLut = ((1+((InfLuty+proc)/pozyczka))*PozSty-rata)
RozLut = PozSty - PozLut
#Marzec2021
PozMarz = ((1+((InfMarzec+proc)/pozyczka))*PozLut-rata)
RozMarz = PozLut - PozMarz
#Kwiecien2021
PozKwie = ((1+((InfKwiecien+proc)/pozyczka))*PozMarz-rata)
RozKwie = PozMarz - PozKwie
#Maj2021
PozMaj = ((1+((InfMaj+proc)/pozyczka))*PozKwie-rata)
RozMaj = PozKwie - PozMaj
#Czerwiec2021
PozCzerw = ((1+((InfCzerwiec+proc)/pozyczka))*PozMaj-rata)
RozCzerw = PozMaj - PozCzerw
#Lipiec2021
PozLip = ((1+((InfLipiec+proc)/pozyczka))*PozCzerw-rata)
RozLip = PozCzerw - PozLip
#Siepien2021
PozSie = ((1+((InfSierpnien+proc)/pozyczka))*PozLip-rata)
RozSie = PozLip - PozSie
#Wrzesien2021
PozWrz = ((1+((InfWrzesien+proc)/pozyczka))*PozSie-rata)
RozWrz = PozSie - PozWrz
#Pazdziernik2021
PozPaz = ((1+((InfPazdziernik+proc)/pozyczka))*PozWrz-rata)
RozPaz = PozWrz - PozPaz
#Listopad2021
PozLis = ((1+((InfListopad+proc)/pozyczka))*PozPaz-rata)
RozLis = PozPaz - PozLis
#Grudzien2021
PozGru = ((1+((InfGrudzien+proc)/pozyczka))*PozLis-rata)
RozGru = PozLis - PozGru
#Styczen12022
PozSty2 = ((1+((InfStyczen2+proc)/pozyczka))*PozGru-rata)
RozSty2 = PozGru - PozSty2
#Luty22022
PozLut2 = ((1+((InfLuty2+proc)/pozyczka))*PozSty2-rata)
RozLut2 = PozSty2 - PozLut2
#Marzec22022
PozMarz2 = ((1+((InfMarzec2+proc)/pozyczka))*PozLut2-rata)
RozMarz2 = PozLut2 - PozMarz2
#Kwiecien22022
PozKwie2 = ((1+((InfKwiecien2+proc)/pozyczka))*PozMarz2-rata)
RozKwie2 = PozMarz2 - PozKwie2
#Maj22022
PozMaj2 = ((1+((InfMaj2+proc)/pozyczka))*PozKwie2-rata)
RozMaj2 = PozKwie2 - PozMaj2
#Czerwiec22022
PozCzerw2 = ((1+((InfCzerwiec2+proc)/pozyczka))*PozMaj2-rata)
RozCzerw2 = PozMaj2 - PozCzerw2
#Lipiec22022
PozLip2 = ((1+((InfLipiec2+proc)/pozyczka))*PozCzerw2-rata)
RozLip2 = PozCzerw2 - PozLip2
#Siepien22022
PozSie2 = ((1+((InfSierpnien2+proc)/pozyczka))*PozLip2-rata)
RozSie2 = PozLip2 - PozSie2
#Wrzesien22022
PozWrz2 = ((1+((InfWrzesien2+proc)/pozyczka))*PozSie2-rata)
RozWrz2 = PozSie2 - PozWrz2
#Pazdziernik22022
PozPaz2 = ((1+((InfPazdziernik2+proc)/pozyczka))*PozWrz2-rata)
RozPaz2 = PozWrz2 - PozPaz2
#Listopad2022
PozLis2 = ((1+((InfListopad2+proc)/pozyczka))*PozPaz2-rata)
RozLis2 = PozPaz2 - PozLis2
#Grudzien2022
PozGru2 = ((1+((InfGrudzien2+proc)/pozyczka))*PozLis2-rata)
RozGru2 = PozLis2 - PozGru2

print(f"Styczen 2021: Twoja pozostala kwota kredytu to {PozSty}, "
      f"to {RozSty} mniej"
      f" niż w poprzednim miesiacu")
print(f"Luty 2021: Twoja pozostala kwota kredytu to {PozLut}, "
      f"to {RozLut} mniej"
      f" niż w poprzednim miesiacu")
print(f"Marzec 2021: Twoja pozostala kwota kredytu to {PozMarz}, "
      f"to {RozMarz} mniej"
      f" niż w poprzednim miesiacu")
print(f"Kwiecien 2021: Twoja pozostala kwota kredytu to {PozKwie}, "
      f"to {RozKwie} mniej"
      f" niż w poprzednim miesiacu")
print(f"Maj 2021: Twoja pozostala kwota kredytu to {PozMaj}, "
      f"to {RozMaj} mniej"
      f" niż w poprzednim miesiacu")
print(f"Czerwiec 2021: Twoja pozostala kwota kredytu to {PozCzerw}, "
      f"to {RozCzerw} mniej"
      f" niż w poprzednim miesiacu")
print(f"Lipiec 2021: Twoja pozostala kwota kredytu to {PozLip}, "
      f"to {RozLip} mniej"
      f" niż w poprzednim miesiacu")
print(f"Sierpien 2021: Twoja pozostala kwota kredytu to {PozSie}, "
      f"to {RozSie} mniej"
      f" niż w poprzednim miesiacu")
print(f"Wrzesien 2021: Twoja pozostala kwota kredytu to {PozWrz}, "
      f"to {RozWrz} mniej"
      f" niż w poprzednim miesiacu")
print(f"Pazdziernik 2021: Twoja pozostala kwota kredytu to {PozPaz}, "
      f"to {RozPaz} mniej"
      f" niż w poprzednim miesiacu")
print(f"Listopad 2021: Twoja pozostala kwota kredytu to {PozLis}, "
      f"to {RozLis} mniej"
      f" niż w poprzednim miesiacu")
print(f"Grudzien 2021: Twoja pozostala kwota kredytu to {PozGru}, "
      f"to {RozGru} mniej"
      f" niż w poprzednim miesiacu")
print(f"Styczen 2022: Twoja pozostala kwota kredytu to {PozSty2}, "
      f"to {RozSty2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Luty 2022: Twoja pozostala kwota kredytu to {PozLut2}, "
      f"to {RozLut2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Marzec 2022: Twoja pozostala kwota kredytu to {PozMarz2}, "
      f"to {RozMarz2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Kwiecien 2022: Twoja pozostala kwota kredytu to {PozKwie2}, "
      f"to {RozKwie2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Maj 2022: Twoja pozostala kwota kredytu to {PozMaj2}, "
      f"to {RozMaj2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Czerwiec 2022: Twoja pozostala kwota kredytu "
      f"to {PozCzerw2}, to {RozCzerw2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Lipiec 2022: Twoja pozostala kwota kredytu "
      f"to {PozLip2}, to {RozLip2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Sierpien 2022: Twoja pozostala kwota kredytu "
      f"to {PozSie2}, to {RozSie2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Wrzesien 2022: Twoja pozostala kwota kredytu "
      f"to {PozWrz2}, to {RozWrz2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Pazdziernik 2022: Twoja pozostala kwota kredytu "
      f"to {PozPaz2}, to {RozPaz2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Listopad 2022: Twoja pozostala kwota kredytu "
      f"to {PozLis2}, to {RozLis2} mniej"
      f" niż w poprzednim miesiacu")
print(f"Grudzien 2022: Twoja pozostala kwota kredytu "
      f"to {PozGru2}, to {RozGru2} mniej"
      f" niż w poprzednim miesiacu")

print("W celu uzyskania informacji, podaj swoj login")
login = input()
print(f"Witaj {login}, Twoje pozyczka wynosi {pozyczka} PLN, oprocentowanie"
      f" wynosi {proc}%, Twoja miesieczna rata wynosi {rata} PLN")
