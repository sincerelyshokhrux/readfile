# print='Task1'

# name=input('Ismingizni kiriting:')
# age=int(input("Yoshingizni kiriting:"))

# with open('malumot.txt', 'w') as f:
#     f.write(f"Name:{name}\n")
#     f.write(f"Age:{age}\n")


# print='Task2'

# with open('fanlar.txt','w') as f:
#     for i in range(5):
#         fan=input(f"{i+1} nchi fan nomini kiriting:")
#         f.write(fan + '\n')


# print='Task3'
# son1=int(input('1-sonni kiriting:'))
# son2=int(input('2-sonni kiriting:'))
# son3=int(input('3-sonni kiriting:'))

# yigindi= son1+ son2+son3
# ortacha=yigindi/3

# with open("hisob.txt", 'w') as f:
#     f.write(f"Yigindi:{yigindi}\n")
#     f.write(f"Ortacha:{ortacha}\n")

# Task4
# name=input('Ismingizni kiriting:')
# familya=input('Familyangizni kiriting:')
# yosh=int(input('Yoshingizni kiriting:'))

# with open('oquvchi.csv', 'w') as f:
#     f.write(f"Ism:{name}\n")
#     f.write(f"Famulya:{familya}\n")
#     f.write(f"Yosh:{yosh}\n")

# Task5
# for a in range(3):
#     name=input('Ismingizni kiriting:')
#     age=int(input('Yoshingizni kiriting:'))
# with open ('baholar.csv', 'w') as f:
#     f.write(f"Ism:{name}\n")
#     f.write(f"Yosh:{age}\n")

# Task6
with open('sonlar.txt', 'w') as txt_f:
    for x in range(5):
        son =int(input(f"{x+1}-son:"))
        print(son , file=txt_f)

        if son%2==0:
            with open('juft_sonlar.csv', 'w') as csv_f:
                print(son, file=csv_f)