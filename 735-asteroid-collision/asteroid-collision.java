class Solution {
    public int[] asteroidCollision(int[] as) {
        Stack<Integer> a = new Stack<>();

        for (int i = 0; i < as.length; i++) {
            while (!(a.isEmpty()) && a.peek() > 0 && as[i] < 0 && -as[i] > a.peek()) {
                a.pop();
            }
            if (as[i] < 0) {
                if (!(a.isEmpty()) && a.peek() > 0) {
                    if (-as[i] < a.peek()) {
                        continue;
                    }
                    else {
                        a.pop();
                        continue;
                    }
                }
            }
            a.push(as[i]);
        }
        int[] array = new int[a.size()];
        int i = 0;
        for (int num : a) {
            array[i++] = num;
        }

        // System.out.println(a);
        return array;
    }
}