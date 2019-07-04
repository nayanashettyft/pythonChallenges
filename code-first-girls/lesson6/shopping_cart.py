def shopping_cart(list):
    print("what do you want to buy")
    item = input()
    list.append(item)
    return list

my_shopping_list = []
while True:
    my_shopping_list = shopping_cart(my_shopping_list)
    if (my_shopping_list[-1] == "Pay") or (my_shopping_list[-1] == "pay"):
        my_shopping_list.pop()
        break
    else:
        print("Continue")
        continue

print("Printing everything you want to buy now")
for x in my_shopping_list:
    print(x, end=" ")

print("")
