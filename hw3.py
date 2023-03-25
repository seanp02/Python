def get_fixed_price(discounted_price):
    global discount_rate
    result=int(discounted_price/(1-(discount_rate/100)))
    return result
    



discount_rate=int(input('할인율은?'))
discounted_price_a=int(input('A 상품의 할인된 가격은?'))
discounted_price_b=int(input('B 상품의 할인된 가격은?'))
print('A 상품의 정가는',get_fixed_price(discounted_price_a),'원')
print('B 상품의 정가는',get_fixed_price(discounted_price_b),'원')
