#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int main() {
	int A[100500];
	int N;
	long long result;
	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
		scanf("%d", A + i);
	result = A[1] - A[2];

	for (int i = 3; i <= N; i++)
		result += abs(A[i]);
	printf("%lld\n", result);

	for (int i = 3; i <= N; i++)
		if (A[i] >= 0)
			printf("%d\n", i);

	printf("2\n");

	for (int i = 3; i <= N; i++)
		if (A[i] < 0)
			printf("%d\n", i);

}
