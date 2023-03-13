n =111414603535684224740921180161  # number
b = True
# for i in range(2,n//2):
#     if n % i == 0 :
#         b = False
#         print('not prime')
#         break
#     # else:
#     #     print('prime')
# if b :
#     print('prime')
b = True
for i in range(2,int(n**(1/2)+1)):
    if n % i == 0 :
        b = False
        print('not prime')
        break
    # else:
    #     print('prime')
if b :
    print('prime')