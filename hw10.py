import os
import pickle
filename='score.bin'

def get_average(lst):
    s=0
    for i in range (len(lst)):
        s+=lst[i]
    avg=s/len(lst)
    return avg
    
def show_scores(lst):
    for i in range (len(lst)):
        print(lst[i],end=' ')
    print()

def input_scores():
    lst=[]
    n=1
    while True:
        a=int(input(f'#{n}? '))
        if a<0:
            break
        lst.append(a)
        n+=1
    return lst

def save_data(scrs,filepath):
    with open(filepath,'wb') as file:
        pickle.dump(scrs,file)

def load_data(filepath):
    lines=[]
    with open(filepath,'rb') as file:
        return pickle.load(file)

if os.path.exists(filename):
    print('[파일 읽기]')
    lst=load_data(filename)
    avg=get_average(lst)
    print('\n[점수 출력]')
    print(f'개인점수: ',end='')
    show_scores(lst)
    print(f'평균: {avg}')
else:
    print('[점수 입력]')
    lst=input_scores()
    avg=get_average(lst)
    print('\n[점수 출력]')
    print(f'개인점수: ',end='')
    show_scores(lst)
    print(f'평균: {avg}')
    save_data(lst,filename)
