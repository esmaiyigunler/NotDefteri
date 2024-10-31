def menu():
    print("1.Notları Göster")
    print("2.Not Ekle")
    print("3.Not Sil")
    print("4.Çıkış")

notlar=[]
while True:
    menu()
    secim=int(input("Lütfen yapacağınız işlemi seçiniz"))
    if secim==1:
        if not notlar:
            print("Mevcut not bulunmuyor")
        else:
            print(notlar)
    elif secim==2:
        note=input("Lütfen notu giriniz")
        notlar.append(note)
    elif secim==3:
        noteid=int(input("Lütfen silmek istediğiniz notun id numarasını girin"))-1
        if 0<=noteid<len(notlar):
            notlar.pop(noteid)
        else:
            print("Not id bulunamadı")
    elif secim==4:
        break
        
