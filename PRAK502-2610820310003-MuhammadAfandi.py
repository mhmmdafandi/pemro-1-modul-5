def hitung(nilai1, nilai2):
    # Lengkapi Function ini
    selisih = nilai1 - nilai2
    if selisih < 0:
        selisih *= -1
    return selisih

def mutlak(angka):
    # Lengkapi Function ini
    if angka < 0:
        angka *= -1
    return angka

def main():
    masukan = []
    while len(masukan) < 4:
        masukan.extend(input().split())
        
    a = int(masukan[0])
    c = int(masukan[1])
    b = int(masukan[2])
    d = int(masukan[3])
    
    Hasil = hitung(a, b) + hitung(c, d)
    print(mutlak(Hasil))

if __name__ == "__main__":
    main()