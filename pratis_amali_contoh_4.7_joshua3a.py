pi=3.142
def kira_kuboid(tinggi,panjang,tebar):
    isipadu_kuboid=tinggi*panjang*lebar
    return isipadu_kuboid
def kuboid():
    tinggi=float(input("Masukkan tinggi"))
    panjang=float(input("Masukkan panjang:"))
    lebar=float(input("Masukkan lebar:"))
    print("Isipadu kuboid=",kira_kuboid(tinggi,panjang,lebar))
def kira_silinder():
    jejari=float(input("Masukkan jejari:"))
    tinggi=float(input("Masukkan tinggi:"))
    print("isipadu silinder=",kira_silinder(pi,jejari,tinggi))
def kira_kon(pi,jejari,tinggi):
    isipadu_kon=(1/3)*pipi(jejari**2)*(tinggi)
    return isipadu_kon
def kon():   
    jejari=float(input("Masukkan jejari:"))
    tinggi=float(input("Masukkan tinggi:"))
    print("Isipadu kon=",kira_kon(pi,jejari,tinggi))
def kira_sfera(pi,jejari):
    isipadu_sfera=4/3(pi*(jejari**3))
    return isipadu_sfera
def sfera():
    jejari=float(input("Masukkan jejari:"))
    print("Isipadu sfera=",kira_sfera(pi,jejari))
ulang=True

while(ulang):
    print("""*****************
    *     Menu Mengira Isi Padu    *
    ***************************
    1.Kuboid
    2.Silinder
    3.kon
    4.sfera
    5.Keluar Dari Program""")
    print("")
    pilih=int(input("Slia masukkan pilihan anda:"))
    if(pilih==1):
        kuboid()
    elif(pilih==2):
        silinder()
    elif(pilih==3):
        kon()
    elif(pilih==4):
        sfera()
    elif(pilih==5):
        ulang=False
        print("Bye Bye")
        exit
    else:
        print("Pilihan tiada dalam senarai")
        print("")



