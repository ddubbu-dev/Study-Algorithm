#include <stdio.h>

int main(void) {
#ifndef ONLINE_JUDGE
  freopen("baekjoon/input.txt", "r", stdin);
  freopen("baekjoon/output.txt", "w", stdout);
#endif

  // 주의사항) 입력 변수 10^4 < int 2*10^9
  int a, b;

  scanf("%d", &a);
  scanf("%d", &b);

  if (a > b) {
    printf(">");
  } else if (a == b) {
    printf("==");
  } else {
    printf("<");
  }

  return 0;
}