import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] english = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        HashMap<String, String> map = new HashMap<>();
        
        for (int i=0; i<10; i++){
            map.put(english[i], Integer.toString(i));
        }
        
        
        for (String str:english){
            if (s.contains(str)){
                s = s.replace(str, map.get(str));
            }
        }
        
        return Integer.parseInt(s);
    }
}