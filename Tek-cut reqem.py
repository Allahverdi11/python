
say = float(input("Bir say girin: "))
if say>0 and (say%2 == 0 ):
  print("pozitif cut eded")
elif say<0 and (say %2== 0):
  print("negatif, cut eded")
elif say>0 and (say %2==1):
  print("pozitif, tek eded")
elif say<0 and (say%2==1):
  print("negatif, tek eded")
if say==0 and (say%2==0):
  print("ne negativ, ne pozitiv")