#include <iostream>
#include <pthread.h>
#include <vector>

// Structure to pass data to threads
struct ThreadData {
    int start;
    int end;
    int* array;
    long long sum; // Each thread calculates a partial sum
};

// Function executed by each thread
void* calculatePartialSum(void* arg) {
    ThreadData* data = (ThreadData*)arg;
    data->sum = 0;
    for (int i = data->start; i < data->end; i++) {
        data->sum += data->array[i];
    }
    return nullptr;
}

int main() {
    // Array to be summed
    const int size = 10;
    int array[size] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Thread-related variables
    pthread_t threads[2];
    ThreadData threadData[2];

    int midpoint = size / 2;

    // Initialize data for the first thread
    threadData[0].start = 0;
    threadData[0].end = midpoint;
    threadData[0].array = array;

    // Initialize data for the second thread
    threadData[1].start = midpoint;
    threadData[1].end = size;
    threadData[1].array = array;

    // Create threads
    pthread_create(&threads[0], nullptr, calculatePartialSum, &threadData[0]);
    pthread_create(&threads[1], nullptr, calculatePartialSum, &threadData[1]);

    // Wait for threads to finish
    pthread_join(threads[0], nullptr);
    pthread_join(threads[1], nullptr);

    // Calculate total sum
    long long totalSum = threadData[0].sum + threadData[1].sum;

    // Output the result
    std::cout << "Sum of the array: " << totalSum << std::endl;

    return 0;
}
