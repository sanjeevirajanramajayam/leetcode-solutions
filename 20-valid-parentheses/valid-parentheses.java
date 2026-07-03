class Solution {
    public boolean isValid(String s) {
        ArrayDeque st = new ArrayDeque();
        HashMap<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');

        for (var x : s.toCharArray()) {
            if (map.containsKey(x)) {
                if (st.peek() == map.get(x)) {
                    st.pop();
                }
                else {
                    return false;
                }   
            }
            else {
                st.push(x);
            }
        }

        return st.size() == 0;
    }
}