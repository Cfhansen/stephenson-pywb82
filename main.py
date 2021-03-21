###solution to exercise 82 from ben stephenson's "the python workbook".

def fare(km):
  fixed = 4
  variable = 0.25

  return fixed + variable * km

distance = float(input('How far did you travel? '))

print(f'Your fare was ${fare(distance):.2f}.')
