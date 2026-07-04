class Solution {
    public int calculate(String s) {
        int currentNumber = 0;
        int sign = 1;
        int result = 0;
        Stack<Integer> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                currentNumber = (currentNumber * 10) + (c - 48);
            }
            else if (c == '+' || c == '-') {
                result += (currentNumber * sign);
                if (c == '-') {
                    sign = -1;
                }
                else {
                    sign = 1;
                }
                currentNumber = 0;
            }
            else if (c == '(') {
                stack.push(result);
                stack.push(sign);
                result = 0;
                sign = 1;
            }
            else if (c == ')') {
                result += (currentNumber * sign);
                currentNumber = 0;
                sign = 1;
                result *= stack.pop();
                result += stack.pop();
            }
        }
        result += (currentNumber * sign);
        return result;
    }
}