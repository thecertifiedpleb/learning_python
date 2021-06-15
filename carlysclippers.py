hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
##### Calculate Average Price #####
total_price = 0
for num in prices:
  total_price += num

print("Average Haircut Price: ", total_price / len(prices))

##### Cut prices by $5 #####

new_prices = [num - 5 for num in prices]
print(new_prices)

##### Calculate Revenue #####

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])
print("Total Revenue: $", total_revenue)

avg_daily_rev = total_revenue / 7
print(avg_daily_rev)

##### Improve Advertising #####

under_30 = [hairstyles[i] for i in range(len(hairstyles) - 1) if new_prices[i] < 30]
print(under_30)
