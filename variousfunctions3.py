def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  
def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost = cost - 50
  elif days >=3:
    cost = cost - 20
  return cost;
