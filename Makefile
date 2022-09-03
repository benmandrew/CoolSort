
coolsort: coolsort.c
	gcc -O3 -DCOOLSORT -o bin/coolsort coolsort.c

insertionsort: coolsort.c
	gcc -O3 -DINSERTIONSORT -o bin/insertionsort coolsort.c

mergesort: coolsort.c
	gcc -O3 -DMERGESORT -o bin/mergesort coolsort.c

all: coolsort insertionsort mergesort
