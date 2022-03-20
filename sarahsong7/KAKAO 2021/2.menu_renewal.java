import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Stack;

class Solution {
    public String[] solution(String[] orders, int[] course) {
//         // trim menu ABCDEFGH
//         int maxOrder = 0;
//         Set<Character> menuSet = new HashSet<Character>();
//         for(String order: orders) {
//             if (order.length()>maxOrder)
//                 maxOrder = order.length();
//             for (int i = 0; i<order.length(); i++) {
//                 menuSet.add(order.charAt(i));
//             }
//         }
        
//         arr = menuSet.toArray(new Character[0]);
//         Arrays.sort(arr);
        
        //combination
        // int menuSetSize = menuSet.size();
        int maxOrder = 0;
        for( String order: orders) {
            arr = order.toCharArray();
            Arrays.sort(arr);
            if (order.length()>maxOrder)
                maxOrder = order.length();
            for (int c: course) {
                if (c<=maxOrder && arr.length>=c)
                    combination(arr.length, c, 0);
            }
        }

        // gen. map (comb, ordered num)
        Map<String, Integer> map = new HashMap<String, Integer>();
        for(String order: newKeys) {
            map.put(order,0);
            System.out.println(order);
        }
        
        // fill map
        int[] maxValue = new int[maxOrder+1];
        for (String order: orders) {
            for (String key: map.keySet()) {
                if (key.length()>order.length())
                    continue;
                // if(order.length()==key.length()) {
                //    if(!order.equals(key))
                //         continue;
                //     else {
                //         map.put(key,map.get(key)+1);
                //         if (maxValue[key.length()]<map.get(key)) {
                //             maxValue[key.length()] = map.get(key);
                //         }
                //         continue;
                //     }
                // }
                if(compare(order,key).equals(key)) {
                    map.put(key,map.get(key)+1);
                    if (maxValue[key.length()]<map.get(key)) {
                        maxValue[key.length()] = map.get(key);
                    }
                }
            }
        }
        
        // get answer
        ArrayList<String> arrayAns = new ArrayList<String>();
        for (int c: course) {
            for(String key: map.keySet()) {
                if (key.length()==c && map.get(key) == maxValue[key.length()] && map.get(key)>1) {
                    arrayAns.add(key);
                }
            }
        }
        
        String[] answer = arrayAns.toArray(new String[0]);
        Arrays.sort(answer);
        return answer;
    }
    
    Stack<String> st=new Stack<String>();
    char[] arr;
    Set<String> newKeys= new HashSet<String>();
    
    void addC () {
        String key="";
        for (int i=0; i<st.size(); i++) {
            key+=st.get(i);
        }
        newKeys.add(key);
    }
    
    void combination (int n, int r, int index) {
        if (r==0) {
            addC();
            return;
        } else if (n==r) {
            for (int i = 0; i<n; i++) st.add(Character.toString(arr[index+i]));
            addC();
            for (int i =0; i<n; i++) st.pop();
        } else {
            st.add(Character.toString(arr[index]));
            combination(n-1, r-1, index+1);
            st.pop();
            combination(n-1, r, index+1);
        }
    }
    
    String compare (String a, String b) {
        String ans = "";
        int ind = 0;
        char[] aa = a.toCharArray();
        char[] bb = b.toCharArray();
        Arrays.sort(aa);
        Arrays.sort(bb);
        for (int i=0; i<aa.length; i++) {
            for (int j = ind; j<bb.length; j++) {
                if(aa[i]==bb[j]){
                    ans+=bb[j];
                    ind=j+1;
                    break;
                }
            }
        }
        return ans;
    }
}