import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.lang.*;

public class day_02 {

    public static void main(String[] args) {
        try {

            File myObj = new File(System.getProperty("user.dir") + File.separator + "cio.txt");
            Scanner myReader = new Scanner(myObj);

            Map<String, Integer> colours_num = new HashMap<String, Integer>();
            colours_num.put("red", 12);
            colours_num.put("green", 13);
            colours_num.put("blue", 14);

            int puzzle_1 = 0;
            int puzzle_2 = 0;
            int num_line = 0;

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();

                int pw_temp = 1;
                num_line++;                
                
                Map<String, Integer> to_compare = findValues(data);
                boolean check = true;
                for (Map.Entry<String, Integer> ent : to_compare.entrySet()) {
                    pw_temp *= ent.getValue();
                    if (colours_num.get(ent.getKey()) != null && colours_num.get(ent.getKey()) < ent.getValue()) {
                        check = false;
                    }
                }
                if (check) {
                    puzzle_1 += num_line;
                }
                puzzle_2 += pw_temp;
                
            }
            System.out.println(puzzle_1);
            System.out.println(puzzle_2);

        } catch (FileNotFoundException e) {
            System.out.println("Error");
            e.printStackTrace();
        }

    }

    public static HashMap<String, Integer> findValues(String data) {

        HashMap<String, Integer> result = new HashMap<String, Integer>();

        data = data.trim();
        int start_index = data.indexOf(":") + 2;
        data = data.substring(start_index);
        String[] games = data.split("; ");
        for (String game : games) {
            String[] temp = game.split(", ");
            for (String tem : temp) {
                String[] couple = tem.split(" ");
                if (result.containsKey(couple[1])) {
                    result.replace(couple[1], Math.max(Integer.parseInt(couple[0]), result.get(couple[1])));
                } else {
                    result.put(couple[1], Integer.parseInt(couple[0]));
                }
                
            }
        }
        return result;
        


    }
}