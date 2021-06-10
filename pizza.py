# Your code below:

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We have " + str(num_pizzas) + " different varieties of pizza!")

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

pizza_and_prices = [1,1,1,1,1,1,1]
for x in range(0,7):
  pizza_and_prices[x] = [prices[x], toppings[x]]
print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print("Budget Friendly: ", cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
print("Highest Quality: ", priciest_pizza)

pizza_and_prices.pop(-1)
print(pizza_and_prices)

pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
