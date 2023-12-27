#oop (object oriented programing ) BASIC
class BidangDatar:
    luas = None
    jenis = None

def luas_segitiga():
    print()
    print("luas segitiga")
    alas = int(input("masukan alas : "))
    tinggi = int (input("masukan tinggi : "))
    luas = 0.5 * alas * tinggi

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "segitiga"
    
    return bidang_datar

def luas_persegi_panjang():
    bidang_datar = "persegi panjang"
    print()
    print("luas persegi panjang")
    panjang = int(input("masukan panjang : "))
    lebar = int (input("masukan lebar : "))
    luas = panjang * lebar

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "persegi panjang"
    
    return bidang_datar

def luas_lingkaran():
    bidang_datar = 'lingkaran'
    print()
    print("luas lingkaran")
    pi = 3.14
    r = int(input("masukan jari jari : "))
    luas = pi * r * r

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "lingkaran"

    return bidang_datar

def luas_jajar_genjang():
    bidang_datar = "jajargenjang"
    print()
    print("luas jajargenjang")
    alas = int(input("masukan alas : "))
    tinggi = int (input("masukan tinggi : "))
    luas = alas * tinggi

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas 
    bidang_datar.jenis = "jajargenjang"

    return bidang_datar

if __name__ == "__main__":
    while True:
        print("Menu")
        print(20*"=")
        print("1. luas segitiga")
        print("2. luas persegi panjang")
        print("3. luas lingkaran")
        print("4. luas jajar genjang")
        print("5. keluar")
        menu = int(input("pilih menu : "))


        if menu == 1:
            bidang_datar = luas_segitiga()
        elif menu == 2:
            bidang_datar = luas_persegi_panjang()
        elif menu == 3:
            bidang_datar = luas_lingkaran()
        elif menu == 4:
            bidang_datar = luas_jajar_genjang()
        elif menu == 5:
            break

        print("luas {} adalah : {}".format(bidang_datar.jenis,bidang_datar.luas))
        print()
