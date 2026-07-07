class Solution {
    public int calculate(String s2) {
        int currentNum = 0;
        Character sign = '+';
        Stack<Integer> s = new Stack<>();
        for (Character c: s2.toCharArray()) {
            if (c == ' ') {
                continue;
            }
            if (Character.isDigit(c)) {
                currentNum = currentNum * 10 + (c - 48);
                continue;
            }
            if (sign == '+') {
                s.push(currentNum);
            }
            else if (sign == '-') {
                s.push(-currentNum);
            }
            else if (sign == '*') {
                s.push(s.pop() * currentNum);
            }
            else {
                s.push(s.pop() / currentNum);
            }
            currentNum = 0;
            sign = c;
        }
        if (sign == '+'){
            s.push(currentNum);
        }
        else if (sign == '-') {
            s.push(-currentNum);
        }
        else if (sign == '*') {
            s.push(s.pop() * currentNum);
        }
        else {
            s.push(s.pop() / currentNum);
        }
        int res = 0;
        for (int x : s) {
            res += x;
        }
        return res;
    }
}