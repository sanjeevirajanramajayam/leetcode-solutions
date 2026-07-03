class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('M', 1000);
        map.put('D', 500);
        map.put('C', 100);
        map.put('L', 50);
        map.put('X', 10);
        map.put('V', 5);
        map.put('I', 1);

        int sum = 0;
        int last_digit = 0;
        int prev = 0;
        for (int idx = s.length() - 1; idx >= 0; idx--) {
            last_digit = map.get(s.charAt(idx));
            if (last_digit < prev)
                sum -= last_digit;
            else
                sum += last_digit;
            prev = last_digit;
        }
        return sum;
    }
}