import java.util.*;

public class Main {

    public static void main(String[] args)
    {
        List<Integer> list = new ArrayList<Integer>();
        Random rnd = new Random ();
        for (int i = 0; i <=25 ; i++)
        {
            list.add(rnd.nextInt(100));
        }

        Collections.sort(list);

        int item = 0;
        for (Integer i : list)
        {
            System.out.println(item++ + " " + i);
        }

        System.out.println(list.get(12));

    }
}
