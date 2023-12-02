import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.lang.*;

public class day_01 {
    public static void main(String[] args) {
        try {
            File myObj = new File(System.getProperty("user.dir") + File.separator + "input.txt");
            Scanner myReader = new Scanner(myObj);

            int puzzle_1 = 0;
            int puzzle_2 = 0;

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                
                puzzle_1 += firstPuzzle(data);
                puzzle_2 += secondPuzzle(data);
            }
            System.out.println("Result of the first puzzle: " + puzzle_1);
            System.out.println("Result of the second puzzle: " + puzzle_2);
        } catch (FileNotFoundException e) {
            System.out.println("Error");
            e.printStackTrace();
        }

    }

    public static int firstPuzzle(String data) {
        String s1 = "";
        String s2 = "";
        for (int i = 0; i < data.length(); i++) {
            if (Character.isDigit(data.charAt(i))) {
                if (s1.equals("")) {
                    s1 += data.charAt(i);
                } else {
                    s2 = "";
                    s2 += data.charAt(i);
                }
            }
        }
        return Integer.parseInt(s1 + s2);
    }    


    public static int secondPuzzle(String data) {
        String temp = "";
        String s1 = "";
        String s2 = "";
        Map<String, String> new_map = createMap();

        for (int i = 0; i < data.length(); i++) {
            if (Character.isDigit(data.charAt(i))) {
                if (s1.equals("")) {
                    s1 += data.charAt(i);
                } else {
                    // Every time I find a new digit after the first one, I substitute it in the second string
                    s2 = "";
                    s2 += data.charAt(i);
                }
                temp = ""; // Finding a digit means that whatever was in the temporary string won't form a word contained in the map
            } else {
                temp += data.charAt(i);

                if (new_map.containsKey(temp)) {
                    if (new_map.get(temp).length() == 1) {
                        if (Character.isDigit(new_map.get(temp).charAt(0))) {

                            if (s1.equals("")) {
                                s1 = new_map.get(temp);
                            } else {
                                s2 = new_map.get(temp);
                            }
                            temp = "";
                            temp += data.charAt(i);
                        } else {
                            temp = new_map.get(temp);
                        }
                    }

                } else {
                    if (temp.length() > 1) {
                        temp = temp.substring(1);
                        /* The string can't be emptied even if it's not in the map,
                        because its substring could be the start of another number
                        (eg. "oni" could mean there's a "nine" after)*/
                    } else {
                        temp = "";
                        
                    }
                        
                }
            }
        }

        // If there's only one digit, it means it is both the first and the last digit
        if (s1.equals("")) {
            s1 += s2;
        } else if (s2.equals("")) {
            s2 += s1;
        }
        return Integer.parseInt(s1 + s2);
    }

    /* HELPER to create a Map to use for comparison */
    public static Map<String, String> createMap() {
        Map<String, String> hashmap = new HashMap<String, String>();
         
            hashmap.put("o", "o");
            hashmap.put("on", "on");
            hashmap.put("one", "1");
            hashmap.put("t", "t");
            hashmap.put("tw", "tw");
            hashmap.put("two", "2");
            hashmap.put("th", "th");
            hashmap.put("thr", "thr");
            hashmap.put("thre", "thre");
            hashmap.put("three", "3");
            hashmap.put("f", "f");
            hashmap.put("fo", "fo");
            hashmap.put("fou", "fou");
            hashmap.put("four", "4");
            hashmap.put("fi", "fi");
            hashmap.put("fiv", "fiv");
            hashmap.put("five", "5");
            hashmap.put("s", "s");
            hashmap.put("si", "si");
            hashmap.put("six", "6");
            hashmap.put("se", "se");
            hashmap.put("sev", "sev");
            hashmap.put("seve", "seve");
            hashmap.put("seven", "7");
            hashmap.put("e", "e");
            hashmap.put("ei", "ei");
            hashmap.put("eig", "eig");
            hashmap.put("eigh", "eigh");
            hashmap.put("eight", "8");
            hashmap.put("n", "n");
            hashmap.put("ni", "ni");
            hashmap.put("nin", "nin");
            hashmap.put("nine", "9");
        
        return hashmap;
    }

}
