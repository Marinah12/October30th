cookies = 0

while cookies < 200: #Won't leave loop until user enters a value >= 200
    cookies = int(input("How many cookies are being sold: "))

crates = int(cookies/240)
remaining = cookies % 240 #Figure out how many cookies are left over
boxes = int(remaining/12)
singles = remaining % 12 #We know the leftovers are the single cookies

#Calculate total sales for each seperately
crate_sales = crates * 80
box_sales = boxes * 5
single_sales = singles * .5
total_sales = float(crate_sales + box_sales + single_sales)
total_sales = "$" + str(round(total_sales, 2)) #Turn total sales into a string for easy printing

print("\n%d crates will be sold" % crates)
print("\n%d boxes will be sold" % boxes)
print("\n%d single cookies will be sold" % singles)
print("\nTotal sales will be %s" % total_sales)
gf