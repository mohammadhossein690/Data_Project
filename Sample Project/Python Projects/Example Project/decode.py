'''
Author : Mohammad Hossein Radpour
Project.No : 05
'''
# This program will decode our password sent from ships into language that can be readable
def decode(text:str) -> str:
    mylist = ['-' for i in range(len(text.split()))]
    for i in text.split():
        if i[0] == '_':
            mylist[int(i[1:])] = ' '
            continue
        mylist[int(i[1:])] = i[0]
    return ''.join(mylist)

# This text below is from encoding from next project
text  = 'h7 l2 i8 _10 t14 i11 s9 _5 s16 e15 H0 _13 e1 o4 T6 t17 s12 l3'
print(decode(text=text))