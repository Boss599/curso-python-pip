import uti

def run ():

  keys,value = uti.get_population()
  print(keys, value)



data= [
  {
    "Countri": "colombia",
    "Population":500
  },
  {
    "Countri": "bolivia",
    
    "Population":300
    
  }
]
countri=input("escriba el pais ")
countri=countri.lower()

result = uti.population_by_countri(data,countri)
print(result)


if__name__ == '__main__':
run()