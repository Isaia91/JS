import random
ppl=["yohann","vivian","gregory","Isaia","angelina","jonathan","brandon","corentin","leon","colin","noah","anselm","mavrick","elias"]
n=int(len(ppl))
k=(random.sample(ppl,3))

def remove_common(Pliste, Gliste): 
    
    for i in Pliste[:]:
        
        if i in Gliste:
            k=(random.sample(ppl,3))
            Pliste.remove(i)
            Gliste.remove(i)
            print("list la liste de départ est : ", Gliste)
            print("list petite liste est : ",Pliste)
            
remove_common(k, ppl)

