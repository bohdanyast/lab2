goods = (['copybook', 5, 100],
         ['watermelon', 15, 20],
         ['pillow', 10, 30],
         ['headphones', 150, 12]
         )

order = (['cop y b oo k', 90],
         ['    h e                 d        ph  o n es', 4]
         )

info = ''
total_value = 0
order_successful = True

for item in order:
    product_name, quantity = item
    found = False

    for good in goods:
        if product_name.lower().replace(' ', '') == good[0]:
            found = True
            if quantity <= good[2]:
                info += f'''
                {product_name.lower().replace(' ', '')}:
                ordered: {quantity}
                price: {good[1]}
                payment: {quantity * good[1]}
                '''

                total_value += quantity * good[1]

                good[2] -= quantity
            else:
                print(-1)
                order_successful = False

    if not found:
        print(-2)
        order_successful = False

if order_successful:
    print(info)
    print(f'Total payment: {total_value}')
    print(goods)
