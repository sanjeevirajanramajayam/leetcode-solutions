class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> m = new HashMap<>();
        HashMap<Character, Integer> m2 = new HashMap<>();

        for (Character c : s.toCharArray()) {
            m.put(c, m.getOrDefault(c ,0) + 1);
        }

        for (Character c : t.toCharArray()) {
            m2.put(c, m2.getOrDefault(c ,0) + 1);
        }
        // System.out.println(m + " " + m2);
        return m.equals(m2);
    }
}