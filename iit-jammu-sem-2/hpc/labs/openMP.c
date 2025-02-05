#include <omp.h>

#include <stdio.h>
#include <stdlib.h>



#define SIZE 10
#define num_threads 4
#define CHUNK_SIZE 2

/*
The lastprivate clause in OpenMP ensures that the last iteration’s value of variable 
inside a parallel loop is preserved even outside the loop.
*/
int main()
{
    int *A, *B, *C;
    double start_time, end_time;
    int tid, trackId;
    trackId = 55;

    A = (int *)malloc(SIZE * sizeof(int));
    B = (int *)malloc(SIZE * sizeof(int));
    C = (int *)malloc(SIZE * sizeof(int));
    for (int i = 0; i < SIZE; i++)
    {
        A[i] = rand() % 10;
        B[i] = rand() % 10;
    }

// static 

    start_time = omp_get_wtime();
#pragma omp parallel num_threads(NUM_THREADS) shared(trackId) 
    {
#pragma omp for schedule(static, CHUNK_SIZE)
        for (int i = 0; i < SIZE; i++)
        {
            tid = omp_get_thread_num();
            if (tid == 1)
            {
                for (int j = 0; j < 1000000000; j++)
                {
                }
            }
            printf("static : %d %d", tid, i);
            printf("\n");
            C[i] = A[i] + B[i];
        }
    }
    end_time = omp_get_wtime();
    printf("Static Parallel Execution Time: %f seconds\n", end_time - start_time);

// dynamic

    start_time = omp_get_wtime();
#pragma omp parallel num_threads(NUM_THREADS) shared(trackId)
    {
#pragma omp for schedule(dynamic) firstprivate(trackId)
        for (int i = 0; i < SIZE; i++)
        {
            tid = omp_get_thread_num();
            if (tid == 1)
            {
                for (int j = 0; j < 1000000000; j++)
                {
                }
            }
            printf("dynamic : %d %d", omp_get_thread_num(), i);
            printf("\n");
            C[i] = A[i] + B[i];
            trackId = i;
        }
    }
    end_time = omp_get_wtime();
    printf(" trackId: %d", trackId);
    printf("\n");
    printf("Dynamic Parallel Execution Time: %f seconds\n", end_time - start_time);

    //  seq

    start_time = omp_get_wtime();
    for (int i = 0; i < SIZE; i++)
    {
        printf("sequential: %d", i);
        printf("\n");
        C[i] = A[i] + B[i];
    }
    end_time = omp_get_wtime();
    printf("Sequential Execution Time: %f seconds\n", end_time - start_time);

    free(A);
    free(B);
    free(C);

    return 0;
}