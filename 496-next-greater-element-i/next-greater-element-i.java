class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> st = new Stack<>();
        // ArrayList<Integer> a = new ArrayList<>();
        HashMap<Integer, Integer> m = new HashMap<>();
        int a[] = new int[nums2.length];

        for (int i = nums2.length - 1; i>=0; i--) {
            m.put(nums2[i], i);
            while ((!st.isEmpty()) && nums2[i] >= st.peek()) {
                st.pop();
            }

            if (st.isEmpty()){
                a[i] = -1;
            }
            else {
                a[i] = st.peek();
            }

            st.push(nums2[i]);
        }

        // System.out.println(Arrays.toString(a) + " " + m);

        int[] arr = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            arr[i] = (a[m.get(nums1[i])]);
        }
        return arr;
    }
}