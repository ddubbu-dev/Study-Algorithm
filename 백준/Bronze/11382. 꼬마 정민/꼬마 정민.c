#include <stdio.h>

int main(void) {
#ifndef ONLINE_JUDGE
  freopen("baekjoon/input.txt", "r", stdin);
  freopen("baekjoon/output.txt", "w", stdout);
#endif

  // 주의사항) 입력 변수 10^12 고려한 자료 선택 필요함
  long long a, b, c;

  scanf("%lld", &a);
  scanf("%lld", &b);
  scanf("%lld", &c);

  printf("%lld", a + b + c);

  return 0;
}