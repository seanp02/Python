shopping_bag={}
print('[구입]')
while True:
    item=input('상품명? ')
    if item == '':
        break
    num=int(input('수량은? '))
    shopping_bag[item]=num
    print(f'장바구니에 {item} {num}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기:{shopping_bag}\n')

print('[검색]')
search=input('장바구니에서 확인하고자 하는 상품은? ')
res=shopping_bag[search]
print(f'{search}은(는) {res}개 담겨 있습니다.')
#이하는 반복해서 수량을 출력하고 장바구니에 담긴 상품인지 아닌지 확인하는 기능 추가.
#while True:
#    search=input('장바구니에서 확인하고자 하는 상품은? ')
#    if search == '':
#        break
#    elif search in shopping_bag:
#        res=shopping_bag[search]
#        print(f'{search}은(는) {res}개 담겨 있습니다.\n')
#    else:
#        print(f'{search}은(는) 장바구니에 담기지 않은 상품입니다.\n')
