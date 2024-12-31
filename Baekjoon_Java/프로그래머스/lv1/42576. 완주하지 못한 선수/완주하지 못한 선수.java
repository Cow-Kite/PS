import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        for(int i=0; i<participant.length; i++){
            map.put(participant[i], map.get(participant[i])==null?1:map.get(participant[i])+1);
            }

        for(int i=0; i<completion.length; i++){
            if(map.containsKey(completion[i]))
                map.replace(completion[i],  map.get(completion[i])-1);
        }

        for(String key : map.keySet()){
            if(map.get(key)!=0){
                answer = key;
                break;
            }
        }
        return answer;
    }
}