class Solution {
    public String getHint(String secret, String guess) {
        HashMap<Character, Integer> m = new HashMap<>();

        for (char c : secret.toCharArray()) {
            m.put(c, m.getOrDefault(c, 0) + 1);
        }

        int bulls = 0;
        int cows = 0;

        for (int i = 0; i < guess.length(); i++) {
            if (secret.charAt(i) == guess.charAt(i)) {
                bulls += 1;
                char c = secret.charAt(i);
                m.put(c, m.getOrDefault(c, 0) - 1);
            } 
        }
        for (int i = 0; i < guess.length(); i++){
                if ((m.getOrDefault(guess.charAt(i), 0) != 0) && !(secret.charAt(i) == guess.charAt(i))){
                    System.out.println(guess.charAt(i) + " " + m +  " " +m.getOrDefault(guess.charAt(i), 0));
                    cows += 1;
                    char c = guess.charAt(i);
                    m.put(c, m.getOrDefault(c, 0) - 1);
                }
        }
        // System.out.println(bulls + " " + cows);
        return bulls + "A" + cows + "B";
    
    }
}