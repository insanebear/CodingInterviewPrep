class Solution {
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        int[][][][][] memory = new int[4][3][3][3][100001];
        for (String i: info) {
            String[] application = i.split(" ");
            int lang,major,career,food,score = 0;
            
            if(application[0].equals("cpp"))
                lang = 1;
            else if (application[0].equals("java"))
                lang = 2;
            else
                lang = 3;
            
            if(application[1].equals("backend"))
                major = 1;
            else
                major = 2;
            
            if (application[2].equals("junior"))
                career = 1;
            else
                career = 2;
            
            if(application[3].equals("chicken"))
                food = 1;
            else
                food = 2;
            
            score = Integer.parseInt(application[4]);
            
            memory[lang][major][career][food][score]++;
            
            memory[lang][major][career][0][score]++;
            memory[lang][major][0][food][score]++;
            memory[lang][0][career][food][score]++;
            memory[0][major][career][food][score]++;
            
            memory[lang][major][0][0][score]++;
            memory[lang][0][career][0][score]++;
            memory[0][major][career][0][score]++;
            memory[lang][0][0][food][score]++;
            memory[0][major][0][food][score]++;
            memory[0][0][career][food][score]++;
            
            memory[0][0][0][food][score]++;
            memory[0][0][career][0][score]++;
            memory[0][major][0][0][score]++;
            memory[lang][0][0][0][score]++;
            
            memory[0][0][0][0][score]++;
            
        }
        for (int i=100000; i>0; i--) {
            for (int l = 0; l<4; l++) {
                for (int m = 0; m<3; m++) {
                    for (int c = 0; c<3; c++) {
                        for (int f = 0; f<3; f++) {
                            memory[l][m][c][f][i-1]+=memory[l][m][c][f][i];                
                        }
                    }
                }
            }
        }
        
        int iter = 0;
        for (String q: query) {
            String[] items = q.split(" ");
            int lang=0, major=0, career=0, food=0, score = 0;
            
            if(items[0].equals("cpp"))
                lang = 1;
            else if (items[0].equals("java"))
                lang = 2;
            else if (items[0].equals("python"))
                lang = 3;
            
            if(items[2].equals("backend"))
                major = 1;
            else if (items[2].equals("frontend"))
                major = 2;
            
            if (items[4].equals("junior"))
                career = 1;
            else if (items[4].equals("senior"))
                career = 2;
            
            if (items[6].equals("chicken"))
                food = 1;
            else if (items[6].equals("pizza"))
                food = 2;
            
            score = Integer.parseInt(items[7]);               
            
            answer[iter]=memory[lang][major][career][food][score];
            iter++;
        }
        
        return answer;
    }
}