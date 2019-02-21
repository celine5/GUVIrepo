#include <stdio.h>

// Function to find n'th Fibonacci number
int fib(int n)
{
	if (n <= 1)
		return n;

	return fib(n - 1) + fib(n - 2);
}

// main function
int main() 
{
	int n = 9;

	printf("n'th Fibonacci number is %d", fib(9));

	return 0;
}
