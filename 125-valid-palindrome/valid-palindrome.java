class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c) || Character.isDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        // System.out.print(sb + " " + sb.reverse());

        String original = sb.toString();
        String reversed = new StringBuilder(original).reverse().toString();

        return original.equals(reversed);

    }
}