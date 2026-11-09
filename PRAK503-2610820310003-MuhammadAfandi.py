def maksimal(a, b):
    # Lengkapi Function ini
    if a > b:
        return a
    else:
        return b

def minimal(a, b):
    # Lengkapi Function ini
    if a < b:
        return a
    else:
        return b

def main():
    batas = 0
    maks = -100000
    minim = 100000
    
    bilangan = int(input())
    nilai = []
    while len(nilai) < bilangan:
        nilai.extend([int(x) for x in input().split()])
        
    while batas < bilangan:
        maks = maksimal(maks, nilai[batas])
        minim = minimal(minim, nilai[batas])
        batas += 1
        
    print(f"{maks} {minim}")

if __name__ == "__main__":
    main()