package recursive;
import java.util.*;
public class leetcode_17 {

    public List<String> letterCombinations(String digits) {
        List<String> res = new LinkedList<>();
        if (digits == null || digits.length() == 0) {
            return res;
        }
        Map<Character, String> maps = new HashMap<Character, String>() {
            {
                put('2', "abc");
                put('3', "def");
                put('4', "ghi");
                put('5', "jkl");
                put('6', "mno");
                put('7', "pqrs");
                put('8', "tuv");
                put('9', "wxyz");
            }
        };
        helper(digits, "", maps, digits.length(), 0, res);
        return res;
    }

    public void helper(String digits, String prefix, Map<Character, String> maps, int size, int level, List<String> res) {
        if (prefix.length() >= size) {
            res.add(prefix);
            return ;
        }
        String letters = maps.get(digits.charAt(level));
        for (int i = 0; i < letters.length(); i++) {
            helper(digits, prefix + letters.charAt(i), maps, size, level + 1, res);
        }

    }

    public static void main(String[] args) {
        leetcode_17 obj = new leetcode_17();
        String dig = "";
        List<String> res = obj.letterCombinations(dig);
        System.out.println(res);
    }
}
