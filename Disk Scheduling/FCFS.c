#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void FCFS(int *arr, int size, int head)
{
    int seek_count = 0;
    int cur_track, distance;
    
    for(int i = 0; i < size; i++)
    {
        cur_track = arr[i];
    
        // calculate absolute distance
        distance = abs(head - cur_track);
    
        // increase the total count
        seek_count += distance;
    
        // accessed track is now new head
        head = cur_track;
    }
    
    printf("Total number of seek operations: %d\n", seek_count);
    
    // Seek sequence would be the same
    // as request array sequence
    printf("Seek Sequence is:\n");
    for (int i = 0; i < size; i++) {
        printf("%d\n", arr[i]);
    }
}

int main()
{
    int size;
    printf("Enter the number of disk requests: ");
    scanf("%d", &size);
    
    // Dynamically allocate memory for the array
    int *arr = (int*)malloc(size * sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    printf("Enter the disk request sequence:\n");
    for(int i = 0; i < size; i++)
    {
        printf("Request %d: ", i + 1);
        scanf("%d", &arr[i]);
    }
    
    int head;
    printf("Enter the initial head position: ");
    scanf("%d", &head);
    
    FCFS(arr, size, head);
    
    // Free dynamically allocated memory
    free(arr);
    
    return 0;
}