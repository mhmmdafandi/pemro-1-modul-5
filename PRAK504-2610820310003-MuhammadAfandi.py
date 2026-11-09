def reverse(n):
    # Lengkapi Function ini
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev

def main():
    masukan = []
    while len(masukan) < 2:
        masukan.extend(input().split())
        
    A = int(masukan[0])
    B = int(masukan[1])
    
    A = reverse(A)
    B = reverse(B)
    C = A + B
    print(reverse(C))

if __name__ == "__main__":
    main()