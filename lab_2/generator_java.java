import java.util.Random;

class Main {
    public static void getNextRandom() {
        for (int i = 0; i < 100; i++) {
            Random random = new Random();
            int seed = random.nextInt();
            System.out.print(Math.abs(seed % 2));
        }
    }

    public static void main(String[] args) {
        getNextRandom();
    }
}
// 1101010101000001110101110001111100100001000011100010010010000100001000111110111110101010001101000010
// 1100010011110111100000000000000100001001010011110110001110110111111101011101001011100100010100010100
