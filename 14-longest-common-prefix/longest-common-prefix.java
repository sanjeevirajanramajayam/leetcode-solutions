class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder ans = new StringBuilder("");
        Character currentChar = 'A';
        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i < strs.length; i++) {
            minLen = Math.min(minLen, strs[i].length());
        }

        for (int i = 0; i < minLen; i++) {
            for (int j = 0; j < strs.length; j++) {
                if (currentChar == 'A') {
                    currentChar = strs[j].charAt(i);
                }
                if (strs[j].charAt(i) != currentChar) {
                    return ans.toString();
                } 
            }
            ans.append(currentChar);
            currentChar = 'A';
        }

        return ans.toString();
    }
}