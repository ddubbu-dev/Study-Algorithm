#include <stdio.h>

int main(void) {
#ifndef ONLINE_JUDGE
  freopen("baekjoon/input.txt", "r", stdin);
  freopen("baekjoon/output.txt", "w", stdout);
#endif

  int n;
  scanf("%d", &n);

  for (int i = 1; i <= 9; i++) {
    printf("%d * %d = %d\n", n, i, n * i);
  }

  return 0;
}