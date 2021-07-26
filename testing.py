weight = 3
# Ground Shipping
def ground_shipping(weight):
  if weight <= 2:
    return weight * 1.5 + 20
  elif weight >= 6:
    return weight * 3 + 20
  elif weight <= 10:
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20

ground_shipping()
    
