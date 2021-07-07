  

name1=input("please enter your name before starting this game ")
def gamef(comp , you):
    if(comp=="r" and you == "r"):
        s=1
        return s
    if(comp=="r" and you =="s"):
        s=0
        return s
    if(comp=="r" and you == "p"):
        s=2
        return s
    if(comp=="p" and you == "r"):
        s=0
        return s
    if(comp=="p" and you =="s"):
        s=2
        return s
    if(comp=="p" and you == "p"):
        s=1
        return s
    if(comp=="s" and you == "r"):
        s=2
        return s
    if(comp=="s" and you =="s"):
        s=1
        return s
    if(comp=="s" and you == "p"):
        s=0
        return s
        
    


print(" ROCK PAPER SCISSOR BEST OF FIVE!!!" )
print("ROUND 1 ")
compscore = 0
yourscore =0
comp=0
import random
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
you=input(" enter your choice  rock(r) , paper(p) , scissor(s)")
print(" your choice \t " , you , " computers choice \t" , comp)
k=gamef(comp,you)
if(k==0):
    print("you loose \t")
    compscore=compscore +1
if(k==1):
    print(" its a draw")
    compscore=compscore+0.5
    yourscore=yourscore+0.5
if(k==2):
    print("you won congrats ")
    yourscore = yourscore+1

print(" yourscore is \t" , yourscore)
print(" computers score is " , compscore)

print("round 2")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
you=input(" enter your choice  rock(r) , paper(p) , scissor(s)")
print(" your choice \t " , you , " computers choice \t" , comp)
k=gamef(comp,you)
if(k==0):
    print("you loose \t")
    compscore=compscore +1
if(k==1):
    print(" its a draw")
    compscore=compscore+0.5
    yourscore=yourscore+0.5
if(k==2):
    print("you won congrats ")
    yourscore = yourscore+1

print(" yourscore is \t" , yourscore)
print(" computers score is " , compscore)
print("round 3 !!! ")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
you=input(" enter your choice  rock(r) , paper(p) , scissor(s)")
print(" your choice \t " , you , " computers choice \t" , comp)
k=gamef(comp,you)
if(k==0):
    print("you loose \t")
    compscore=compscore +1
if(k==1):
    print(" its a draw")
    compscore=compscore+0.5
    yourscore=yourscore+0.5
if(k==2):
    print("you won congrats ")
    yourscore = yourscore+1

print(" yourscore is \t" , yourscore)
print(" computers score is " , compscore)
print("round 4 !!! ")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
you=input(" enter your choice  rock(r) , paper(p) , scissor(s)")
print(" your choice \t " , you , " computers choice \t" , comp)
k=gamef(comp,you)
if(k==0):
    print("you loose \t")
    compscore=compscore +1
if(k==1):
    print(" its a draw")
    compscore=compscore+0.5
    yourscore=yourscore+0.5
if(k==2):
    print("you won congrats ")
    yourscore = yourscore+1

print(" yourscore is \t" , yourscore)
print(" computers score is " , compscore)
print("round 5")
randNo = random.randint(1,3) 
if randNo == 3:
    comp = 'r'
elif randNo == 1:
    comp = 'p'
elif randNo == 2:
    comp = 's'
you=input(" enter your choice  rock(r) , paper(p) , scissor(s)")
print(" your choice \t " , you , " computers choice \t" , comp)
k=gamef(comp,you)
if(k==0):
    print("you loose \t")
    compscore=compscore +1
if(k==1):
    print(" its a draw")
    compscore=compscore+0.5
    yourscore=yourscore+0.5
if(k==2):
    print("you won congrats ")
    yourscore = yourscore+1

print(" yourscore is \t" , yourscore)
print(" computers score is " , compscore)

if(yourscore>compscore):
    print(name1 ,"\t you won congratulations !!!")
if(compscore>yourscore):
    print (name1 ," \tyou lost better luck next time")
if(compscore==yourscore):
    print(name1,"\t its a tie ")   