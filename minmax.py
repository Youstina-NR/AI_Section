
import math
#import rendom
def fun_Minmax(cd, node, maxt, scr, td):
    if(cd==td):
        return scr[node]
    if(maxt):
        return max(fun_Minmax(cd+1, node*2, False, scr, td),
                   fun_Minmax(cd+1, node*2+1, False, scr, td))  
    else:

        return min(fun_Minmax(cd+1, node*2, True, scr, td),
                   fun_Minmax(cd+1, node*2+1, True, scr, td))  


scr=[]
x=int(input("enter total number of leaf node= "))
for i  in range(x):
    y=int(input("enter leaf value: "))
    scr.append(y)

td=math.log(len(scr), 2)  

cd= int(input("enter current depth value: "))
nodev=int(input("enter node value: "))
maxt=True

print("the answer is: ", end= " ")
answer=fun_Minmax(cd, nodev, maxt, scr, td)
print(answer)
