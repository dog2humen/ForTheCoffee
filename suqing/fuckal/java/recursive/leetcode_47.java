package recursive;
import java.util.*;

public class leetcode_47 {

    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) {
            return new ArrayList<>();
        }
        Map<String, List<String>> cache = new HashMap<>();
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = String.valueOf(ca);
            if (!cache.containsKey(key)) {
                cache.put(key, new ArrayList<>());
            }
            cache.get(key).add(s);
        }
        return new ArrayList<>(cache.values());
    }
}
