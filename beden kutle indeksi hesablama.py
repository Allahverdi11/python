ad = str(input("adiniz: "))
kilo = float(input("kilonuz : "))
boy = float(input("boy(m) :"))
bki = float(kilo/(boy*boy))
if bki < 18.5 :
  print(f"Hormetli, {ad}, kilonuz cok asagi,       indexiniz: {bki}")
elif bki>18.5 and bki<27.5 : 
  print(f"Hormetli, {ad}, kilonuz normal, indexiniz: {bki}")
if bki> 27.5 :
  print(f"Hormetli, {ad}, kilonuz coxdur, indexiniz: {bki}")

