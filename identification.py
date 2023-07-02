import random as r

alcoholConditions = ["dil HCl, ZnCl2", "NaBr, H2SO4", "NaI, H3PO4", "PCl5", "Red P, Br2/I2", "SOCl2, Pyridine", "SOCl2", "443K conc H2SO4", "440K 85% H2SO4", "358K 15% H2SO4", "[O]", "[O], heat, pressure", "i. KMnO4/H+ ii.peroxiacid", "Cu, 573K", "LiAlH4, H+/H2O","413K conc H2SO4",]
phenolConditions = ["pthalic anhydride, conc H2SO4","Acid Chloride, pyridine", "Acid anhydride, conc H2SO4", "Br2, CS2", "Br2, H2O", "i. conc H2SO4, ii. conc HNO3", "dil HNO3", "oleum 288K", "oleum 373K", "i. CHCl3 NaOH ii. refluxed at 340K", "i. CCl4 NaOH ii. refluxed at 340K", "CO2 NaOH & 400K 4-7atm", "H2Ni 573K", "Zn dust, heat"]
allylConditions = ["i. B2H6, THF", "i. Hg(OAc)2 ii. NaBH4", "Br2 CCl4", "HBr, peroxide, heat", "heat, light, NBS, HBr", "X2, 673-873K", "SO2Cl2", "i. dil H2SO4 ii. H+/H2O"]
haloConditions = ["moist Ag2O/aq KOH", "KCN", "AgCN", "KNO2", "AgNO2", "aq RCOOAg", "AgF/CoF2", "alkoxide", "Na, dry ether, heat", "aq KOH, AgNO3", "NH3, sealed tube, 383K", "LiAlH4", "Cu [halocompound is iodobenzene]", "C2H5OH, H2O, heat", "NaOH, 623K, 300atm, H2O", "NaI, acetone, heat"]
bdcConditions = ["phenol, pH = 10", "phenol, pH =14", "phenol, pH = 3", "HBF4", "KI" , "boil with H2O", "CuCl/HCl", "Cu powder, HCl/HBr"]
etherConditions = ["HBr/HI 373K", "HBr/HI excess 373K"]
print("Write the products and byproducts formed. If necessary, name the type of product required to take the reaction to completion. Name the reaction where necessary")
def problemGen():

    type = r.randint(1,6)
    answer = ""
    if type == 1:
        print("Reagent: Alcohol")
        i = r.randint(0, len(alcoholConditions)-1)
        print(alcoholConditions[i])
        if(i ==0):
                answer = "Product: Chloroalkane, Name: Grove's Process"
        elif(i ==1): 
                answer = "Product: Bromoalkane"
        elif(i==2):
                answer= "Product: Iodoalkane"
        elif(i==3):
                answer= "Product: Chloroalkane, SNi mechanism"
        elif(i==4):
                answer= "Product: Bromo/Iodoalkane"
        elif(i==5):
                answer="Product: Chloroalkane, complete retention"  
        elif(i==6):
                answer="Product: Chloroalkane, complete inversion" 
        elif(i==7):
                answer="Product: Alkene" 
        elif(i==8):
                answer="Product: Alkene" 
        elif(i==9): 
                answer="Product: Alkene"
        elif(i==10):
                answer="Product: Ketone" 
        elif(i==11):
                answer="Product: Mixture of carboxylic acid, provided an adjacent CH2 group to the carbonyl group is present"
        elif(i==12):
                answer="Product: Ester, Name: Baeyer Villiger Reaction"
        elif(i==13):
                answer="Product: Aldehyde when primary, Ketone when secondary, Alkene when tertiary"
        elif(i==14):
                answer="Product: Alkane"
        elif(i==15):
                answer="Product: Ether for primary, mixture of compounds for secondary, alkene for tertiary"
        input()
        print(answer)
        alcoholConditions.pop(i)
    if type == 2: 
        print("Reagent: Phenol")
        i = r.randint(0, len(phenolConditions)-1)
        print(phenolConditions[i])
        if(i == 0):
            answer="Product: Phenolphthalein"
        elif(i == 1): 
            answer="Product: (2-hydroxybenzene)ketone + (4-hydroxybenzene)ketone, Name: Schotten Baumann Reaction"
        elif(i == 2): 
            answer="Product: (2-hydroxybenzene)ketone + (4-hydroxybenzene)ketone, Name: Schotten Baumann Reaction" 
        elif(i == 3):
            answer="Product: bromophenol" 
        elif(i == 4): 
            answer="Product: tribromophenol" 
        elif(i ==5):
            answer="Product: picric acid" 
        elif(i == 6):
            answer="Product: nitrophenol"
        elif(i==7):
            answer="Product: [KCP] o-hydroxybenzene sulfonic acid" 
        elif(i ==8):
            answer="Product: [TCP] p-hydroxybenzene sulfonic acid"
        elif(i ==9): 
            answer="Product: Salicylaldehyde, Name: Reimer Tiemann Reaction"
        elif(i ==10):
            answer="Product: Salicylic Acid, Name: Reimer Tiemann Reaction"
        elif(i ==11):
            answer="Product: Salicylic Acid, Name: Kolbe-Schmitt Reaction"
        elif(i==12):
             answer="Product: Benzene"
        elif(i==13):
             answer="Product: Cyclohexanol"
        input()
        print(answer)
    if type == 3: 
        print("Reagant: Allyl group")
        i = r.randint(0, len(allylConditions)-1)
        print(allylConditions[i])
        if(i==0):
            answer = "Product: Antimarkovnikoff (whatever the spelling is) addition of hydroxyl. Reaction: Hydroboration Oxidation"
        elif(i ==1):
            answer = "Product: Markovnikoff addition product of hydroxyl, reaction is oxymerucration demercuration"
        elif(i==2):
            answer = "Product: vicinal dibromide"
        elif(i==3):
            answer = "Product: bromide"
        elif(i==4):
            answer = "Product: antimarkovnikoff addition product of bromide"
        elif(i==5):
            answer = "Product: Allylic addition of bromide"
        elif(i==6):
            answer = "Product: Allylic addition of chloride"
        elif(i==7):
            answer = "Product: Markovnikoff addition of hydroxyl"
        elif(i==8): 
            answer = "Product: cyclohexanol"
        elif(i==9):
            answer = "Product: benzene"
        input()
        print(answer)
    if type == 4:
        print("Reagent: Halocompound")
        i = r.randint(0, len(haloConditions)-1)
        print(haloConditions[i])
        if(i == 0): 
            answer = "Product: Alcohol"
        elif(i == 1):
            answer = "Product: alkanenitrile. Can be hydrolysed to either amide or carboxylic acid"
        elif(i ==2): 
            answer = "Product: alkaneisonitrile. Can be hydrolysed to primary amine."
        elif(i ==3):
            answer = "Product: alkanenitrite"
        elif(i==4):
            answer = "Product: nitroalkane"
        elif(i==5):
            answer = "Product: ester"
        elif(i==6):
            answer = "Product: flouroalkane, Name: Swarts Reaction/Halide Exchange Reaction"
        elif(i==7):
            answer = "Product: Ether, Name: Williamson Ether Synthesis"
        elif(i==8):
            answer = "Product: alkane, Name: Wurtz Reaction"
        elif(i==9):
            answer = "Product: ppt, distinguishing test for haloalkanes"
        elif(i==10): 
            answer = "Product: Mixture of primary, secondary, tertiary and quaternary amines. 1:10 HX:NH3 ratio gives primary as major product, reciprocal gives quaternary as major product. Name: Hoffman Ammonolysis"
        elif(i==11):
            answer = "Product: Alkane"
        elif(i==12):
            answer = "Product: biphenyl, Name: Ullman Biaryl Synthesis"
        elif(i==13):
            answer = "Product: alkene, E1 Mechanism"
        elif(i==14): 
            answer = "Product: Phenol when reagent is benzene, Name: Dows Process"
        elif(i==15):
            answer = "Product: Iodobenzene, Name: Finkelstein Reaction"
        input()
        print(answer)
    if(type == 5):
        print("Reagent: BDC")
        i = r.randint(0, len(bdcConditions)-1)
        print(bdcConditions[i])
        if(i == 0): 
            answer = "Product: paradihydroxyazobenzene (azo dye), an orange dye"
        elif(i == 1):
            answer = "Product: Sodium diazoate"
        elif(i == 2):   
            answer = "Product: No product formed due to low phenoxide concentrations"
        elif(i ==3): 
            answer = "Product: Fluorobenzene, Name: Balz Schiemann Reaction"
        elif(i==4): 
            answer = "Product: Iodobenzene"
        elif(i==5):
            answer = "Product: Phenol"
        elif(i==6): 
            answer = "Product: Chlorobenzene, Name: Sandmeyer Reaction"
        elif(i==7):
            answer = "Product: Chloro/Bromobenzene, Name: Gatermann Reaction"
        input()
        print(answer)
    if(type==6):
        print("Reagent: Ether")
        i = r.randint(0,1)
        print(etherConditions[i])
        if(i ==1): 
            answer = "Product: Smaller alkyl halide and alcohol"
        if(i ==2):
            answer = "Product: Mixture of alkyl halides"
        input()
        print(answer)
    print("\n")
while(1>0):
    problemGen()
#important ones
#commercial spirit production 
#commercial ethanol production 
