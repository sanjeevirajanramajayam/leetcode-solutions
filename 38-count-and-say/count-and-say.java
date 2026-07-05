class Solution {
    String fn(int n, String temp, int f) {
        if (n == f ) {
            return temp;
        }
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        char ch = 'a';
        for (char c: temp.toCharArray()) {
            if (ch == 'a') {
                ch = c;
                cnt += 1;
                continue;
            }
            if (ch != c) {
                sb.append((cnt));
                sb.append((char)(ch));
                cnt = 1;
                ch = c;
            }
            else {
                cnt += 1;
            }
        }
        sb.append(cnt);
        sb.append(ch);
        return fn(n+1, sb.toString(), f);
    }
    public String countAndSay(int n) {
        return fn(1, "1", n);
    }
}