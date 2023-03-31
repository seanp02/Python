def draw_line_string(name):
    greet=f' Hello {name}, '
    welcome=' Welcome to Seoul. '
    nstr=len(greet)if(len(greet)>len(welcome))else len(welcome)
    line='-'*nstr
    print(line)
    print(greet)
    print(welcome)
    print(line)

name=input('Input his/her name: ')
draw_line_string(name)