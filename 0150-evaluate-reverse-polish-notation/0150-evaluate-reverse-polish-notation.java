class Solution {
    public int evalRPN(String[] tokens) {
        int a,b;
        Stack<Integer> stk = new Stack<>();
        for(String str : tokens){
            if(str.equals("+")){
                a = stk.pop();
                b = stk.pop();
                stk.push(b+a);
            }
            else if(str.equals("-")){
                a = stk.pop();
                b = stk.pop();
                stk.push(b - a);
            }
            else if(str.equals("*")){
                a = stk.pop();
                b = stk.pop();
                stk.push(b*a);
            }
            else if(str.equals("/")){
                a = stk.pop();
                b = stk.pop();
                stk.push(b/a);
            }
            else{
                stk.push(Integer.parseInt(str));
            }
        }
        return stk.pop();
    }
}