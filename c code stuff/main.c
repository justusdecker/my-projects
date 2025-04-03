//(c) Masterschool
#include <stdio.h>

int compute_sum(int limit) {
	int sum = 0;//init variable integer. Value: 0
	for (int i = 1; i <= limit; i++) { // loop from 1 to limit and add each iteration i to sum
		sum += i;
	}
	return sum;
}

int main() {
	int max_number = 100;//init variable integer. Value: 100
	int result = compute_sum(max_number); //write the return from compute sum to result
	printf("Sum of numbers from 1 to %d is %d\n", max_number, result);//print to the console
	return 0;
}