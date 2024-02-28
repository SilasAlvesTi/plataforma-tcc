#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int num1, num2, result;

    scanf("%d", &num1);
    scanf("%d", &num2);

    result = add(num1, num2);

    printf("%d", result);

    return 0;
}