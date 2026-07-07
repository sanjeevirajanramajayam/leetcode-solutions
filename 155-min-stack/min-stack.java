class MinStack {
    Stack<Long> st;
    long min;
    public MinStack() {
        this.st = new Stack<>();
        this.min= Long.MAX_VALUE;
    }
    
    public void push(int value) {
        if (st.isEmpty()){
            min = (long)value;
            st.push((long)value);
        }
        else if (value >= min) {
            st.push((long)value);
        }
        else {
            // x < oldMin
            // add x on both sides and move oldMin
            // push onto stack: 
            // 2*x - oldMin < x

            st.push(2L * value - min);
            min = (long)value;
        }
        // System.out.println(st);
    }
    
    public void pop() {
        if (st.peek() >= this.min) {
            // return this.min;
            st.pop();
        }
        else {
            // 2 * x - oldMin = encoded
            // 2 * x - encoded = oldMin
            this.min = (2L * this.min - st.peek());
            st.pop();
        }
        // System.out.println(st);

    }
    
    public int top() {
        if (st.peek() >= this.min) {
        // System.out.println(st);

            return st.peek().intValue();
        }
        else {
        // System.out.println(st);

            // 2 * x - oldMin = encoded
            // 2 * x - encoded = oldMin
            return (int)this.min;
        }

    }
    
    public int getMin() {
        // System.out.println(st);

        return (int)this.min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(value);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */