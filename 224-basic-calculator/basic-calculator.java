class Solution {
    public int calculate(String s) {
        int currentNum = 0;
        int result = 0;
        int sign = 1;
        Stack<Integer> st = new Stack<>();

        for (Character c: s.toCharArray()) {
            if (Character.isDigit(c)) {
                currentNum = currentNum * 10;
                currentNum += (c - '0');
                continue;
            }
            if (c == ' ') {
                continue;
            }
            if ( c == '+') {
                result += (currentNum * sign);
                currentNum = 0;
                sign = 1;
            }
            else if (c == '-') {
                result += (currentNum * sign);
                sign = -1;
                currentNum = 0;
            }
            else if (c == '(') {
                st.push(result);
                st.push(sign);

                currentNum = 0;
                result = 0;
                sign = 1;
            }
            else if (c == ')') {
                result += currentNum * sign;
                result *= st.pop();
                result += st.pop();
                currentNum = 0;
            }

        }
        result += currentNum * sign;
        return result;
    }
}