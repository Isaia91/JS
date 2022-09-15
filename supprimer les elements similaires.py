import random
ppl=["yohann","vivian","gregory","Isaia","angelina","jonathan","brandon","corentin","leon","colin","noah","anselm","mavrick","elias"]
n=int(len(ppl))
k=(random.sample(ppl,3))

def remove_common(k, ppl): 
    for i in k[:]:
        if i in ppl:
            s=0
            k.remove(i)
            ppl.remove(i)

            print("list ppl : ", ppl)
            print("list k : ",k)
            s=s+1
remove_common(k, ppl)

