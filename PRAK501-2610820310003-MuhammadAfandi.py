def MaxBilangan(a, b, c, d):
    maks = a
    if b > maks:
        maks = b
    if c > maks:
        maks = c
    if d > maks:
        maks = d
    return maks

def main():
    masukan = input().split()
    a = int(masukan[0])
    b = int(masukan[1])
    c = int(masukan[2])
    d = int(masukan[3])
    
    hasil = MaxBilangan(a, b, c, d)
    print(hasil)

if __name__ == "__main__":
    main()