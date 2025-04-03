#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> numbers;
    int input;

    std::cout << "Enter numbers (0 to stop): ";

    while (true) {
        std::cin >> input;
        if (input == 0) break;
        numbers.push_back(input);
    }

    std::sort(numbers.begin(), numbers.end());

    std::cout << "Sorted numbers: ";
    // YOUR CODE
    // print the sorted numbers using a for loop

    return 0;
}