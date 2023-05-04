def buy(lst):
    print('[구입]')
    item=input('상품명? ')
    if item == '':
        return False
    num=int(input('수량은? '))
    shopping_bag[item]=num
    print(f'장바구니에 {item} {num}개가 담겼습니다.\n')

def show(lst):
    print(f'\n>>> 장바구니 보기: {shopping_bag}\n')

def find(lst):
    print('[검색]')
    search=input('장바구니에서 확인하고자 하는 상품은? ')
    if search in shopping_bag:
        res=shopping_bag[search]
        print(f'{search}은(는) {res}개 담겨 있습니다.\n')
    else:
        print(f'장바구니에 {search}은(는) 없습니다.\n')

shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break
show(shopping_bag)
find(shopping_bag)




