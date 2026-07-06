class Solution {
    public int calculate(String s) {
        int currentNum = 0;
        int result = 0;
        int sign = 1; // old sign value
        Stack<Integer> st = new Stack<>();

        for (Character c: s.toCharArray()) {
            if (c == ' ') {
                continue;
            }
            if (Character.isDigit(c)) {
                currentNum  = currentNum * 10 + (c - 48);
                continue;
            }
            if (c == '+') {
                result += currentNum * sign; // use old sign
                sign = 1;
            }
            else if (c == '-') {
                result += currentNum * sign;
                sign = -1;
            }
            else if (c == '(') {
                st.push(result);
                st.push(sign);
                result = 0;
                // currenNum = 0;
                sign = 1;
            }
            else if (c == ')') {
                result += currentNum * sign;
                result *= st.pop();
                result += st.pop();
            }
            currentNum = 0;
        }
        // System.out.println(currentNum * sign + " " + st);
        result += (currentNum * sign);
        // System.out.println(currentNum * sign + " " + st);
        // int sum = 0;
        // for (int x : st) {
        //     sum += x;
        // }
        return result;
    }
}