motSoBatKi=int(input('Hãy nhập một số bất kì'))
b=0
for i in range(motSoBatKi+1):
    if i % 2 == 0:
      b=b+i
print(b)