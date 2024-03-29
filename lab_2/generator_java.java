import java.util.Random;

/**
 * Осуществляет генерацию случайной бинарной последовательности
 */
class Main {
    /**
     * Необходим для генерации случайной бинарной последовательности
     * длиной 128 бит и вывода ее в консоль
     */
    public static void getNextRandom() {
        for (int i = 0; i < 128; i++) {
            Random random = new Random();
            int seed = random.nextInt();
            System.out.print(Math.abs(seed % 2));
        }
    }

    /**
     * Осуществляет вызов getNextRandom()
     *
     * @param args необходим для командной строки
     */
    public static void main(String[] args) {
        getNextRandom();
    }
}
