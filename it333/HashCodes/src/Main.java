import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class Main
{

    public static void main(String[] args)
    {
        System.out.println("Hello World!");



        List<String> names = new ArrayList<>();
        names.add("Jared");
        names.add("Carey");
        names.add("Sarah");
        names.add("Alvin");
        names.add("Emma");
        names.add("Jack");
        names.add("Teri");
        names.add("Neal");
        names.add("Zoe");
        names.add("Fred");
        String[] strs = new String[names.size()];

        for (String name: names)
        {

            int hashCode = mod (name.hashCode(), strs.length);
            System.out.println("Name: " + name + " hashcode: " + hashCode);
            int index = hashCode;

            do
            {
                if (strs[index] == null)
                {
                    strs[index] = name;
                    System.out.println("strs[" + index + "]: " + strs[index] +"(" + mod (strs[index].hashCode(), strs.length) + ")");
                    break;
                }
                index++;
                if (index == strs.length)
                {
                    index = 0;
                }
            } while (index != hashCode);

            System.out.println();
            System.out.println();
        }

        for (int i = 0; i <strs.length ; i++)
        {
            System.out.println("strs["+ i + "]: " + strs[i] + "(" + mod (strs[i].hashCode(), strs.length) + ")");
        }



    }

    public static int mod(int num, int _mod)
    {

        int hashCode = num % _mod;
        if (hashCode < 0)
        {
            return (hashCode * -1);
        }

        return hashCode;
    }
}
