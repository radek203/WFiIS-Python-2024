static void sortuj(int *arr, int size) {
    for (int i = 1; i < size; i++) {
        int elem = arr[i];
        int j = i - 1;
        while (j>=0 && arr[j] > elem) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1]=elem;
    }
}

static void mnoz(int **a, int **b, int **c, int wierszy1, int kolumn1, int kolumn2) {
    for (int wiersz1 = 0; wiersz1 < wierszy1; wiersz1++) {
        for (int kolumna2 = 0; kolumna2 < kolumn2; kolumna2++) {
            for (int kolumna1 = 0; kolumna1 < kolumn1; kolumna1++) {
                c[wiersz1][kolumna2] += a[wiersz1][kolumna1] * b[kolumna1][kolumna2];
            }
        }
    }
}