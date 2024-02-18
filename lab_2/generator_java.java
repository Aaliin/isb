class Main {
    public static int a = 41;
    public static int c = 11119;
    public static int m = 11113;
    public static int seed = 1;

    public static void getNextRandom() {
        for (int i = 0; i < 100; i++) {
            seed = (a * seed + c) % m; 
            System.out.print(seed % 2);
        }
    }

    public static void main(String[] args) { 
        getNextRandom(); 
    }
}
// 1101010101000001110101110001111100100001000011100010010010000100001000111110111110101010001101000010