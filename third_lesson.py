def calculate_price(items, quantity,discount):
    suma = 0
    price_without_discount = 0
    for price in items:
        discount_price = price * discount/100
        suma += (price - discount_price) * quantity
        price_without_discount += price * quantity
    return round(suma),price_without_discount

items = list(map(int, input("Введите цены через пробел: ").split()))
quantity = int(input("Введите количество товаров: "))
discount = int(input("Введите процент скидки: "))
ww,price_without_discount = calculate_price(items, quantity, discount)
print("Цена с скидкой: ",ww,"\nЦена без скидки: ",price_without_discount)