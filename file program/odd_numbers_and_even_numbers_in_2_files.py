f1=open('number_list.txt','r')
f3=open('odd.txt','w')
f4=open('even.txt','w')
list_=(f1.read()).split(',')
for i in map(int,list_):
    if i%2!=0:
        f3.write(str(i)+',')
    else:
        f4.write(str(i)+',')
f3.close()
f4.close()
f1.close()
        
