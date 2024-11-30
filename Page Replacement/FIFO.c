#include <stdio.h>

int main() {
    int frames;
    printf("Enter the number of frames: ");
    scanf("%d", &frames);

    int incomingStream[100];
    int pages;
    printf("Enter the length of the incoming stream: ");
    scanf("%d", &pages);
    printf("Enter the incoming stream: ");
    for (int i = 0; i < pages; i++) {
        scanf("%d", &incomingStream[i]);
    }

    int pageFaults = 0;
    int temp[frames];

    for (int m = 0; m < frames; m++) {
        temp[m] = -1;
    }

    printf("\nIncoming");
    for (int i = 0; i < frames; i++) {
      if(i == 0) {
         printf("\tFrame %d", i + 1);
      } else {
        printf("\t\tFrame %d", i + 1);
      }
    }
    printf("\n");

    for (int m = 0; m < pages; m++) {
        int s = 0;
        for (int n = 0; n < frames; n++) {
            if (incomingStream[m] == temp[n]) {
                s++;
                pageFaults--;
            }
        }
        pageFaults++;

        if ((pageFaults <= frames) && (s == 0)) {
            temp[m] = incomingStream[m];
        } else if (s == 0) {
            temp[(pageFaults - 1) % frames] = incomingStream[m];
        }

        printf("%d", incomingStream[m]);
        for (int n = 0; n < frames; n++) {
            if (temp[n] != -1) {
                printf("\t\t%d", temp[n]);
            } else {
                printf("\t\t-");
            }
        }
        printf("\n");
    }

    printf("\nTotal Page Faults:\t%d\n", pageFaults);

    return 0;
}