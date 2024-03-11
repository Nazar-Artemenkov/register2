from module1 import *


salasõnad=[]
kasutajanimed=[]
while True:
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutnime\n4-unustanud parooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("registreerimine")
        kasutajanimed,salasõnad=registeerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või paaroli muutmine")
        vastus=input("Kas muudame nime või parooli ")
        if vastus=="nime":
            kasutajanimed=nime_või_parooli_muutmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad=nime_või_parooli_muutmine(salasõnad)
        elif vastus=="mõlemad":
            print("nimi muutmine: ")
            kasutajanimed=nime_või_parooli_muutmine(kasutajanimed)
            print("Parooli muutmine")
            salasõnad=nime_või_parooli_muutmine(salasõnad)
    elif vastus==4:
        print("Unustanud paaaroli taastamine")
    elif vastus==5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")
