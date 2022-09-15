#------fonction qui mélange les élements d'un tableau(ici nos prénoms) et affiche 5groupes (quatres groupes de 3 et un groupe de deux)
import random
malist = ["yohann","vivian","gregory","Isaia","angelina","jonathan","brandon","corentin","leon","colin","noah","anselm","mavrick","elias"]
random.shuffle(malist)
def  group(malist,depart,fin):
    groupe=[]
    for n in malist[:]:
     groupe.append(malist[n])
    print(groupe)
group(malist,0,3)
group(malist,3,6)
group(malist,6,9)
group(malist,9,12)
group(malist,12,14)
