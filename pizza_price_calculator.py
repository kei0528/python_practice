size = input("How big do you want have your pizza? S, M, L?\n")
add_pepperoni = input("Do you want have pepperoni on the top? Y,N\n")
with_cheese = input("Do you want extra cheese? Y,N\n")

price = 0
if size == "S":
    price += 15

    if add_pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20

    if add_pepperoni == "Y":
        price += 3
else:
    price += 25

if with_cheese == "Y":
    price += 1

print(f"Pizza costs {price} €!")
