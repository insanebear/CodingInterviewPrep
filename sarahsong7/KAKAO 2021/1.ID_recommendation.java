class Solution {
    public String solution(String new_id) {
        String answer = "";
        // step 1.
        answer = new_id.toLowerCase();
        // step 2.
        String temp = "";
        for (int i = 0; i<answer.length(); i++) {
            if (answer.charAt(i)=='-'||answer.charAt(i)=='_'||answer.charAt(i)=='.'||
               (answer.charAt(i)>='a' && answer.charAt(i)<='z') ||
               (answer.charAt(i)>='0' && answer.charAt(i)<='9') )
                temp += answer.charAt(i);
        }
        answer = temp;
        System.out.println(answer);
        // step 3.
        answer = stringReplace(answer);
        System.out.println(answer);
        // step 4.
        if (answer.length()!=0 && answer.charAt(0) == '.') {
            if (answer.length() != 1)
                answer = answer.substring(1);
            else 
                answer = "";
        }
        System.out.println(answer);
        if (answer.length()!=0 && answer.charAt(answer.length()-1) == '.') {
            if (answer.length()!=1)
                answer = answer.substring(0,answer.length()-1);
            else
                answer = "";
        }
        System.out.println(answer);
        // step 5.
        if (answer.equals(""))
            answer = "a";
        System.out.println(answer);
        // step 6.
        if (answer.length() > 15)
            answer = answer.substring(0,15);
        if (answer.charAt(answer.length()-1) == '.')
            answer = answer.substring(0,answer.length()-1);
        System.out.println(answer);
        // step 7.
        if (answer.length() == 1)
            answer = answer+answer+answer;
        if (answer.length() == 2)
            answer = answer + answer.charAt(1);
        System.out.println(answer);
        return answer;
    }
    
    String stringReplace(String temp) {
        
        String answer = "";
        Boolean isFormerDot = false;
        for (int i = 0; i<temp.length(); i++) {
            if (!isFormerDot) {
                answer+=temp.charAt(i);
                if (temp.charAt(i) == '.')
                    isFormerDot = true;
            } else {
                if (temp.charAt(i) != '.') {
                    answer+=temp.charAt(i);
                    isFormerDot = false;
                }
            }
        }
    
        return answer;
    }
}