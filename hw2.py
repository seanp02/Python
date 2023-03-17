def exchange(money):
    coin500=money//500
    coin100=money%500//100
    coin50=money%100//50
    coin10=money%50//10
    print('500원 동전의 개수:',coin500)
    print('100원 동전의 개수:',coin100)
    print('50원 동전의 개수:',coin50)
    print('10원 동전의 개수:',coin10)

def get_integer(prompt):
    res=int(input(prompt))
    return res

money=get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(money)
