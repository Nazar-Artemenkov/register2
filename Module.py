from pickle import FALSE, TRUE


def Korrutis(arv1:float,arv2:float,arv3:float,arv4=1.0)->float:
    """funktsioon tagastab 4 arvude korrutis,arvud sisestab kasutaja. Vaikimisi arv4=1.0.tulemus tagastatakse float formaadis

    :param float arv1: sisestatakse nagu parameeter
    :param float arv2:  sisestatake nagu parameeter
    :param float arv3: sisestatakse nagu parameeter
    :param float arv4: sisestatakse nagu parameeter, vaikimisi võrdub ühega
    :rtype: float
    """
    k=arv1*arv2*arv3*arv4
    return k
def Suurim_element(arvud1:list,arvud2:list,):
    """Funktsioon kuvab ekraanile suurim arv listidest.
    
    :param list arvud1: Arvude loetelu
    :param list arvud2: Arvude loetelu
    
    """
    suurim1=max(arvud1)
    suurim2=max(arvud2)
    suurim=max(suurim1,suurim2)
    print(suurim)

#1
def arithmetic(arv1:float, arv2:float, sumb:str)->any:
    """Funktsion tagastab aritmeetiliste tehtede tulemused,
    + - liitumine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float arv1: ujukomaarv mis sisestab kasutaja
    :param float arv2: ujukomaarv mis sisestab kasutaja
    :param str sumb: sõne/tehe, mis sisestab kasutaja
    """
    if sumb=="+":
        vastus=arv1+arv2
    elif sumb=="-":
        vastus=arv1-arv2
    elif sumb=="*":
        vastus=arv1*arv2
    elif sumb=="/":
        if arv2==0:
            vastus="DIV/0"
        else:
            vastus=arv1/arv2
    else:
        vastus="tundmatu operatsioon"
    return vastus

#2
def is_year_leap(aasta:int)-> bool:
    """Funktsioon tagastab True, kui aasta on liigaasta, või False Kui aasta on tavaline
    
    :param int aasta: Kasutaja sisestab aasta number
    :rtype: bool
    """
    if aasta%4==0:
        vastus=true
    else:
        vastus=FALSE
    return vastus