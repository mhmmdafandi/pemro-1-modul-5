#include <stdio.h>
#include <math.h>

int hitung(int nilai1, int nilai2){
    //Lengkapi Function ini
    int selisih = nilai1 - nilai2;
    if (selisih < 0) {
        selisih *= -1;
    }
    return selisih;
}

int mutlak(int angka){
    //Lengkapi Function ini
    if (angka < 0) {
        angka *= -1;
    }
    return angka;
}

int main()
{
    int a,b,c,d,Hasil;

    scanf("%d",&a);
    scanf("%d",&c);
    scanf("%d",&b);
    scanf("%d",&d);

    Hasil = hitung(a,b) + hitung(c,d);
    printf("%d",mutlak(Hasil));

    return 0;
}