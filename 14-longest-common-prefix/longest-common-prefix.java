class Trie {
    TrieNode root;

    Trie() {
        this.root = new TrieNode();
    }

    void insert(String s) {
        TrieNode curr = this.root;
        for (Character c : s.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new TrieNode();
            }
            curr = curr.children[c - 'a'];
        }
        // return True;
        curr.isEnd = true;
    }

    String search() {
        TrieNode curr = this.root;
        StringBuilder sb = new StringBuilder();
        while (!curr.isEnd && cntChildren(curr) == 1) {
            for (int i = 0; i < curr.children.length; i++) {
                if (curr.children[i] != null) {
                    sb.append((char)('a' + i));
                    curr = curr.children[i];
                    break;
                }
            }
        }
        return sb.toString();
    }

    int cntChildren (TrieNode root) {
        int cnt = 0;
        for (TrieNode x : root.children) {
            if (x != null) {
                cnt += 1;
            }
        }
        return cnt;
    }
}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

class Solution {
    public String longestCommonPrefix(String[] strs) {
        Trie t = new Trie();
        for (String s: strs) {
            t.insert(s);
        }
        return t.search();
    }
}