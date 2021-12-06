
import numpy as np
import pdb
#np.random.seed(314161)
fam = []

fam.append(np.array(["Tom","Laura"]))
fam.append(np.array(["Andrea","Eric","Will","Emma"]))
fam.append(np.array(["Brian","Jolie","Bode","Gunnar"]))
fam.append(np.array(["Geran","Olivia"]))

totfam = sum([len(element) for element in fam])

print ("\n\n"+str(len(fam)) + " familes: " )
for ii in range(len(fam)):
    print("Family " + str(ii))
    sfam = ""
    for jj in range(len(fam[ii])):
        sfam += fam[ii][jj] + " "
    print (sfam)

print ("\n")

nmaxgiver = 20
nmaxeffort = 260
neffort = 0
goodpairs = False
paired = {}
while (not goodpairs):
    giftees = []
    for ii in range(len(fam)):    
        for name in fam[ii]:
            famgind = np.random.choice(np.delete(np.arange(len(fam)),ii),1) # pick 1 from the other families
            # rand is taken from np.arange(len(fam)), not including ii
            goodgiftee = False; nit = 0
            while (not goodgiftee and nit<nmaxgiver):
                giftee = str(np.random.choice(fam[famgind[0]],1)[0])
                if giftee not in giftees:
                    paired[name] = giftee
                    giftees.append(giftee) ## append only if not already in this array
                    goodgiftee = True
                nit+=1
            if (nit is nmaxgiver):
#                print ("Too many iterations for giver " + name + ". Starting all over.")
                break
        if (nit is nmaxgiver):
            break

    neffort += 1
    # check if paired is proper length and non-empty. If so:    
    if len(paired) is totfam:
        goodpairs = True
        # Finally, make sure no one is giving to someone giving right back to them.
        for key,value in paired.items():
            for key2,value2 in paired.items():
                if key2 is key:
                    continue
                if key is value2 and value is key2:
                    goodpairs = False
                    break
            if not goodpairs:
                break

    if neffort is nmaxeffort:
        print("Exceeded " + str(nmaxeffort) + ". Bailing")
        break

if goodpairs is True:
    print ("Success after " + str(neffort) + " tries." + "\n")
    print("Proposed gifters=>giftees " )
    for key,value in paired.items():
        print(key, '=>', value)


