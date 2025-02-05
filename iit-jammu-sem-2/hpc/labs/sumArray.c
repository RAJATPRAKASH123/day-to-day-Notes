#include <stdio.h>
#include <pthread.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 10000000
#define NUM_THREADS 6

int array[SIZE];
int partial_sum[NUM_THREADS];
pthread_t threads[NUM_THREADS];

typedef struct {
    pthread_mutex_t mutex;
    pthread_cond_t cond;
    int count;
    int trip_count;
} custom_barrier_t;

custom_barrier_t barrier;

// Initialize the custom barrier
void custom_barrier_init(custom_barrier_t *barrier, int count) {
    pthread_mutex_init(&barrier->mutex, NULL);
    pthread_cond_init(&barrier->cond, NULL);
    barrier->count = 0;
    barrier->trip_count = count;
}

// Wait on the custom barrier
void custom_barrier_wait(custom_barrier_t *barrier) {
    pthread_mutex_lock(&barrier->mutex);
    barrier->count++;

    if (barrier->count == barrier->trip_count) {
        barrier->count = 0;
        pthread_cond_broadcast(&barrier->cond);
    } else {
        pthread_cond_wait(&barrier->cond, &barrier->mutex);
    }

    pthread_mutex_unlock(&barrier->mutex);
}

// Destroy the custom barrier
void custom_barrier_destroy(custom_barrier_t *barrier) {
    pthread_mutex_destroy(&barrier->mutex);
    pthread_cond_destroy(&barrier->cond);
}

// Thread function to calculate the partial sum for a segment of the array
void *thread_worker(void *arg) {
    int thread_id = *(int *)arg;

    // Calculate partial sum
    int start = thread_id * (SIZE / NUM_THREADS);
    int end = (thread_id == NUM_THREADS - 1) ? SIZE : start + (SIZE / NUM_THREADS);

    partial_sum[thread_id] = 0;
    for (int i = start; i < end; i++) {
        partial_sum[thread_id] += array[i];
    }

    // Synchronize threads for tree reduction
    custom_barrier_wait(&barrier);

    int step = 1;
    while (step < NUM_THREADS) {
        if (thread_id % (2 * step) == 0 && thread_id + step < NUM_THREADS) {
            partial_sum[thread_id] += partial_sum[thread_id + step];
        }
        step *= 2;

        custom_barrier_wait(&barrier);
    }

    return NULL;
}

// Sequential sum calculation
int calculate_sum_sequential() {
    int total_sum = 0;
    for (int i = 0; i < SIZE; i++) {
        total_sum += array[i];
    }
    return total_sum;
}

int main() {
    // Initialize the array with random numbers
    for (int i = 0; i < SIZE; i++) {
        array[i] = (rand() % 10) + 1;
    }

    int thread_ids[NUM_THREADS];
    int total_sum_sequential = 0;

    struct timespec start, end;
    double time_threaded, time_sequential;

    // Initialize custom barrier
    custom_barrier_init(&barrier, NUM_THREADS);

    // Measure time for threaded sum
    clock_gettime(CLOCK_MONOTONIC, &start);

    // Create threads
    for (int i = 0; i < NUM_THREADS; i++) {
        thread_ids[i] = i;
        if (pthread_create(&threads[i], NULL, thread_worker, &thread_ids[i]) != 0) {
            fprintf(stderr, "Error: Unable to create thread %d\n", i);
            exit(EXIT_FAILURE);
        }
    }

    // Join threads
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    clock_gettime(CLOCK_MONOTONIC, &end);
    time_threaded = (end.tv_sec - start.tv_sec) +
                    (end.tv_nsec - start.tv_nsec) / 1e9;

    // Sequential sum calculation
    clock_gettime(CLOCK_MONOTONIC, &start);
    total_sum_sequential = calculate_sum_sequential();
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_sequential = (end.tv_sec - start.tv_sec) +
                      (end.tv_nsec - start.tv_nsec) / 1e9;

    // Print results
    printf("Threaded Total Sum: %d\n", partial_sum[0]);
    printf("Sequential Total Sum: %d\n", total_sum_sequential);
    printf("Threaded Execution Time: %.9f seconds\n", time_threaded);
    printf("Sequential Execution Time: %.9f seconds\n", time_sequential);

    // Destroy custom barrier
    custom_barrier_destroy(&barrier);

    return 0;
}
