def Biodata(tahunLahir, Namaku, Asal):
    tahun_sekarang = 2020
    # Lengkapi Function ini
    print(f"Perkenalkan Nama Saya : {Namaku}")
    print(f"Umur Saya : {tahun_sekarang - tahunLahir}")
    print(f"Saya Adalah Angkatan : {tahun_sekarang}")
    print(f"Asal Saya dari : {Asal}")

def main():
    tahunLahir = int(input())
    A = input()
    B = input()
    Biodata(tahunLahir, A, B)

if __name__ == "__main__":
    main()