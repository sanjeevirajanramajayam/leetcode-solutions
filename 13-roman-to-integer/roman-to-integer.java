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
        int prev = 0;
        
        for (int i = s.length() - 1; i >= 0; i-- ) {
            int val = map.get(s.charAt(i));
            if (prev > val) {
                sum -= val;
            }
            else {
                sum += val;
            }
            prev = val;
        }
        return sum;
    }
}