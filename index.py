def mix():
    volume_1_puit = input("entrer le volume de chaque puit")
    volume_echantillon = input("entrer le volume de l'echantillon (ARN)")
    volume_mix_reactionnel = float(volume_1_puit) - float(volume_echantillon)
    print("le volume du mix réactionnel a prèparer est : " + str(volume_mix_reactionnel))
    nbr_puits= input("entrer le nombre de puits")
    print(" mix reactionnel Pour  un seul puit: ")
    volume_enzyme = input("volume de l'enzyme ")
    volume_amorce1= input("volume de l'amorce 1 ")
    volume_amorce2= input("volume de l'amorce 2 ")
    volume_eau = volume_mix_reactionnel - ( float(volume_enzyme) + float(volume_amorce1) + float(volume_amorce2 ))
    print (" volume de l'eau : " + str ( volume_eau))
    #Cacul pour le mix
    enzyme= (int(nbr_puits)*volume_enzyme)
    amorce1 = (int(nbr_puits)*float(volume_amorce1))
    amorce2 = (int (nbr_puits)*float(volume_amorce2))
    Eau  =  (float(nbr_puits)*float(volume_eau))
    print(" le mix reactionnel Pour" + nbr_puits + ": ")
    print("enzyme" " " + str ( enzyme ))
    print("amorce1" " " + str(amorce1))
    print("amorce2" " " + str(amorce2))
    print("eau" " " + str(Eau))



if __name__ == '__main__':
     mix()
