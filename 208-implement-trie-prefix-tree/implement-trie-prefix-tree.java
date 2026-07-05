class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

class Trie {
    TrieNode root;
    public Trie() {
        this.root = new TrieNode();
    }
    
    public void insert(String word) {
        
        TrieNode curr = this.root;
        for (Character c: word.toCharArray()) {
            if (curr.children[(c - 97)] == null) {
                curr.children[(c - 97)] = new TrieNode();
            } 
            curr = curr.children[(c - 97)];

        }
        curr.isEnd = true;
    }
    
    public boolean search(String word) {
        TrieNode curr = this.root;
        for (Character c: word.toCharArray()) {
            if (curr.children[(c - 97)] != null) {
                curr = curr.children[(c - 97)];
            } 
            else {
                return false;
            }
        }
        if (curr.isEnd == true) {
            return true;
        }
        else {
            return false;
        }

    }
    
    public boolean startsWith(String prefix) {
        TrieNode curr = this.root;
        for (Character c: prefix.toCharArray()) {
            if (curr.children[(c - 97)] != null) {
                curr = curr.children[(c - 97)];
            } 
            else {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */