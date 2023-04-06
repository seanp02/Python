def read_single_digit(d):
    if d=='0':
        return '영'
    elif d=='1':
        return '일'
    elif d=='2':
        return '이'
    elif d=='3':
        return '삼'
    elif d=='4':
        return '사'
    elif d=='5':
        return '오'
    elif d=='6':
        return '육'
    elif d=='7':
        return '칠'
    elif d=='8':
        return '팔'
    elif d=='9':
        return '구'

def read_number(n):
    if int(n)>99:
        hundred=read_single_digit(n[-3])
        ten=read_single_digit(n[-2])
        one=read_single_digit(n[-1])
        return f'{hundred} {ten} {one}'
    elif int(n)>9:
        ten=read_single_digit(n[-2])
        one=read_single_digit(n[-1])
        return f'{ten} {one}'
    else:
        one=read_single_digit(n[-1])
        return f'{one}'

number=str(input('세 자리 정수 입력: '))
print(read_number(number))
