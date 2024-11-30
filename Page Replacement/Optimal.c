#include <stdio.h>  
#include <stdlib.h>  
#include <stdbool.h>  
  
#define NUM_FRAMES 3  
#define NUM_PAGES 10  
  
// Function to find the page that will be referenced furthest in the future  
int findOptimalPage(int page[], int pageFrames[], int index, int numFrames) {  
    int farthest = -1;  
    int farthestIndex = -1;  
      
    for (int i = 0; i < numFrames; i++) {  
        int j;  
        for (j = index; j < NUM_PAGES; j++) {  
            if (pageFrames[i] == page[j]) {  
                 
if (j > farthest) {  
                     
farthest = j;  
                     
farthestIndex = i;  
                 
}  
                 
break;  
            }  
        }  
          
        if (j == NUM_PAGES) {  
             
return i;  
        }  
    }  
      
    if (farthestIndex == -1) {  
        return 0;  
    }  
      
    return farthestIndex;  
}  
  
int main() {  
    int pageReferences[NUM_PAGES] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3};  
    int pageFrames[NUM_FRAMES];  
    bool isPageInFrame[NUM_FRAMES];  
    int pageFaults = 0;  
  
    for (int i = 0; i < NUM_FRAMES; i++) {  
         
pageFrames[i] = -1;  
         
isPageInFrame[i] = false;  
    }  
  
     
printf("Page Reference String: ");  
    for (int i = 0; i < NUM_PAGES; i++) {  
         
printf("%d ", pageReferences[i]);  
    }  
    printf("\n");  
  
    for (int i = 0; i < NUM_PAGES; i++) {  
        int page = pageReferences[i];  
  
        if (!isPageInFrame[page]) {  
            int pageToReplace = findOptimalPage(pageReferences, pageFrames, i + 1, NUM_FRAMES);  
             
pageFrames[pageToReplace] = page;  
             
isPageInFrame[pageToReplace] = true;  
             
pageFaults++;  
  
             
printf("Page %d loaded into frame %d\n", page, pageToReplace);  
        }  
    }  
  
     
printf("Total Page Faults: %d\n", pageFaults);  
  
    return 0;  
}  