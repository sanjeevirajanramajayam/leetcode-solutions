class Solution {
    public int calculate(String s) {
        Stack<Integer> st = new Stack<>();
        int currentNum = 0;
        char sign = '+';
        for (Character c: s.toCharArray()) {
            if (c == ' ')
                continue;
            if (Character.isDigit(c)) {
                currentNum = currentNum * 10 + (c - 48);
                continue;
            }
            else if (sign == '+') {
                st.push(currentNum);
            }
            else if (sign == '-') {
                st.push(-currentNum);
            }
            else if (sign == '*') {
                st.push(st.pop() * currentNum);
            }
            else if (sign == '/') {
                st.push(st.pop() / currentNum);
            }
            currentNum = 0;
            sign = c;
        }

        if (sign == '+') {
            st.push(currentNum);
        }
        else if (sign == '-') {
            st.push(-currentNum);
        }
        else if (sign == '*') {
            st.push(st.pop() * currentNum);
        }
        else if (sign == '/') {
            st.push(st.pop() / currentNum);
        }

        // System.out.println(st);
        return st.stream().mapToInt(Integer::intValue).sum();
    }
}