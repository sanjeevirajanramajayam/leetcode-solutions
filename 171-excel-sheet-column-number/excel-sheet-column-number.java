class Solution {
    public int titleToNumber(String c) {
        int ans = 0;
        for (int i = c.length() - 1; i >= 0; i-- ) {
            int power = c.length() - 1 - i;
            ans += ((c.charAt(i) - 'A' + 1) * (int)Math.pow(26, power));
        }
        return ans;
    }
}