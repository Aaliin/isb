#include <iostream>
#include <random>
#include <ctime>

#define MAX 128

using namespace std;

int generator() {
    srand(time(0));
    for (int i = 0; i < MAX; ++i) {
        unsigned long value = (8253729 * rand() + 2396403) % 32768;
        std::cout << value % 2;
    }
    return 0;
}

int main() {
    cout << generator(); 
}
