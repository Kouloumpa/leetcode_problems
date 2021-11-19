class Solution {
    public int hammingDistance(int x, int y) {

        int result = 0;
        int[] x_binary = new int[31];
        int[] y_binary = new int[31];

        int id_x = 0;
        int id_y = 0;

        while (x > 0) {
            x_binary[id_x++] = x % 2;
            x = x / 2;
        }

        while (y > 0) {
            y_binary[id_y++] = y % 2;
            y = y / 2;
        }

        for (int i = 0; i<y_binary.length; i++) {
            if (x_binary[i] != y_binary[i]) {
                result += 1;
            }
        }

        return result;
    }
}