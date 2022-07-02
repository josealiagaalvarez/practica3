gases = [
   {"elemento": "hidrogeno", "simbolo": "H", "na": 1, "pa": 1},
   {"elemento": "nitrogeno", "simbolo": "N", "na": 7, "pa": 14},
   {"elemento": "oxigeno", "simbolo": "O", "na": 8, "pa": 16},
   {"elemento": "fluor", "simbolo": "F", "na": 9, "pa": 19},
   {"elemento": "Cloro", "simbolo": "Cl", "na": 17, "pa": 35},
   {"elemento": "Helio", "simbolo": "He", "na": 2, "pa": 4},
   {"elemento": "Neon", "simbolo": "Ne", "na": 10, "pa": 20},
   {"elemento": "Argon", "simbolo": "Ar", "na": 18, "pa": 40},
   {"elemento": "Kripton", "simbolo": "Kr", "na": 36, "pa": 84},
   {"elemento": "Xenon", "simbolo": "Xe", "na": 54, "pa": 131},
   {"elemento": "Radon", "simbolo": "Rn", "na": 86, "pa": 222}
]
def mergeasc(lista, left, right,tipo):
   i = j = k = 0
   while i < len(left) and j < len(right):
       if left[i][tipo] < right[j][tipo]:
           lista[k] = left[i]
           i += 1
       else:
           lista[k] = right[j]
           j += 1
       k += 1
   while i < len(left):
       lista[k] = left[i]
       i += 1
       k += 1
   while j < len(right):
       lista[k] = right[j]
       j += 1
       k += 1

def mergedes(lista, left, right,tipo):
   i = j = k = 0
   while i < len(left) and j < len(right):
       if left[i][tipo] > right[j][tipo]:
           lista[k] = left[i]
           i += 1
       else:
           lista[k] = right[j]
           j += 1
       k += 1
   while i < len(left):
       lista[k] = left[i]
       i += 1
       k += 1
   while j < len(right):
       lista[k] = right[j]
       j += 1
       k += 1

def merge_sort(lista,tipo):
    if len(lista) > 1 :
      mid = len(lista) // 2
      left = lista[:mid]
      right = lista[mid:]
      merge_sort(left,tipo)
      merge_sort(right,tipo)
      if(tipo=="pa"):
         mergeasc(lista, left, right,tipo)
      else:
         mergedes(lista, left, right, tipo)

def main():
   print("Lista inicial")
   for x in gases:
    print(x)
   print()
   print("Listado ordenado de acuerdo al peso atomico")
   merge_sort(gases,tipo="pa")
   for x in gases:
    print(x)
   print()
   print("Listado ordenado de manera descendente de acuerdo al numero atomico")
   merge_sort(gases, tipo="na")
   for x in gases:
      print(x)
   print()

main()