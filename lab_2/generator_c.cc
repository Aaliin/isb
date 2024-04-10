#include <iostream>
#include <random>
#include <ctime>

#define MAX 128

using namespace std;

/**
 * @brief Необходима для генерации случайной бинарной последовательности
 * длиной 128 бит и вывода ее в консоль
 * 
 * @return 0 если программа успешно завершена
 */
int generator()
{
    srand(time(0));
    for (int i = 0; i < MAX; ++i)
    {
        unsigned long value = (1021 * rand() + 24631) % 116640;
        std::cout << value % 2;
    }
    return 0;
}

/**
 * @brief Необходима для вызова функции generator()
 */
int main()
{
    cout << generator();
}