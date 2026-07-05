class Solution {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            n--;
            int r = n % 26;
            sb.append((char)(65 + (r)));
            n = n / 26;
        }
        return sb.reverse().toString();
    }
}