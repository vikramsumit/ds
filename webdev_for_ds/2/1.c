#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "ISRO";
    char str2[] = "ISRO";

    if (strcmp(str1, str2) == 0) {
        printf("both are same");
    } else {
        printf("both are NOT same");
    }

    return 0;
}