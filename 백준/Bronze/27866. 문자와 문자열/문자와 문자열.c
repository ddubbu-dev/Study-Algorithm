#include <stdio.h>

int main(void) {
#ifndef ONLINE_JUDGE
  freopen("baekjoon/input.txt", "r", stdin);
  freopen("baekjoon/output.txt", "w", stdout);
#endif
#define SIZE 1000

  int i;
  char arr[SIZE] = {};
  scanf("%s", arr);
  scanf("%d", &i);

  printf("%c", arr[i - 1]);
}
