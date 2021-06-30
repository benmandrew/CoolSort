#include <stdio.h>
#include <stdlib.h>

#define CACHELINE_SIZE 64
#define INTS_IN_CACHELINE (CACHELINE_SIZE / sizeof(int))


size_t minimum(size_t a, size_t b) {
    return a <= b ? a : b;
}

void printArray(int* a, size_t n) {
    for (size_t i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

void copy(int* a, int* b, size_t n) {
    for (size_t i = 0; i < n; i++) b[i] = a[i];
}

int* generateRandomArray(size_t size) {
    srand(0);
    int* arr = (int*)malloc(size*sizeof(int));
    for (size_t i = 0; i < size; i++) arr[i] = i;
    size_t i, j, tmp;
    for (i = size - 1; i > 0; i--) {
        j = rand() % (i + 1);
        tmp = arr[j];
        arr[j] = arr[i];
        arr[i] = tmp;
    }
    return arr;
}

int* insertionsort(int* a, size_t n, size_t runSize) {
    // Iterate over each subarray
    for (size_t run = 0; run < n; run += runSize) {
        // Sort subarray
        size_t i = run + 1;
        while (i < run + runSize) {
            size_t j = i;
            while (j > run && a[j-1] > a[j]) {
                size_t tmp = a[j-1];
                a[j-1] = a[j];
                a[j] = tmp;
                j--;
            }
            i++;
        }
    }
    return a;
}

void merge(int* a, size_t left, size_t right, size_t end, int* b) {
    size_t i = left, j = right;
    for (size_t k = left; k < end; k++) {
        if (i < right && (j >= end || a[i] <= a[j])) {
            b[k] = a[i];
            i++;
        } else {
            b[k] = a[j];
            j++;
        }
    }
}

int* mergesort(int* a, size_t n, size_t runSize) {
    int* b = (int*)malloc(n * sizeof(int));
    // Switches us between the primary (a) and auxiliary (b) arrays
    char isPrimaryArr = 1;
    for (size_t width = runSize; width < n; width *= 2) {
        // Merge runs together of increasing size
        for (size_t i = 0; i < n; i += 2 * width) {
            // Alternate between the a and b arrays
            if (isPrimaryArr) {
                merge(a, i, minimum(i + width, n), minimum(i + 2 * width, n), b);
            } else {
                merge(b, i, minimum(i + width, n), minimum(i + 2 * width, n), a);
            }
        }
        isPrimaryArr = !isPrimaryArr;
    }
    if (!isPrimaryArr) copy(b, a, n);
    free(b);
    return a;
}

int* coolsort(int* a, size_t n) {
    a = insertionsort(a, n, INTS_IN_CACHELINE);
    return mergesort(a, n, INTS_IN_CACHELINE);
}


int main(int argc, char** argv) {

    size_t n = 64;
    int* a = generateRandomArray(n);
    printArray(a, n);
    a = coolsort(a, n);
    printArray(a, n);
    
    return 0;
}
