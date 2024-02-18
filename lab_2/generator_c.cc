#include <iostream>
#include <random>
#include <ctime>

#define MAX 100

using namespace std;

int generator() {
    srand(time(0));
    for (int i = 0; i < MAX; ++i) {
        unsigned long value = (rand() * 73129 + 95121) % 100000;
        std::cout << value % 2;
    }
    return 0;
}

int main() {
    cout << generator();
    // 01010100101110111101010111110100111000001101011001100101101100110000111000101011001001100100000100100
}