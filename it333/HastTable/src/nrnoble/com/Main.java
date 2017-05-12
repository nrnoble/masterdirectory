package nrnoble.com;

public class Main {

    public static void main(String[] args)
    {
	// write your code here

        HastTable<String> wordset = new HastTable<>();
        wordset.add("green");
        wordset.add("green");
        wordset.add("green");
        wordset.add("green");
        wordset.add("green");
        wordset.add("green");
        wordset.add("green");
//        wordset.add("pink");
//        wordset.add("yellow");
//        wordset.add("purple");
//        wordset.add("red");
//        wordset.add("black");

        System.out.println("Before reshash(): " + wordset.toString());

        wordset.add("purple");
        wordset.add("orange");

        System.out.println(" After reshash(): " + wordset.toString());
        System.out.println("remove(red): " + wordset.remove("red"));
        System.out.println("size(): " + wordset.size());

        for (String word: wordset)
        {
            System.out.println(word);
            //wordset.remove("pink");
        }


        HastTable<Integer> intSet = new HastTable<>();
        intSet.add(13);
        intSet.add(1);
        intSet.add(14);
        intSet.add(18);
       // intSet.add(13);
        intSet.add(59);
        intSet.add(44);
        System.out.println("Before reshash(): " + intSet.toString());

        intSet.add(12);
        intSet.add(85);
       // intSet.add(55);
       // intSet.add(78);
       // intSet.add(71);
       // intSet.add(16);

//        intSet.add(9);
//        intSet.add(34);
        System.out.println("After  reshash(): " + intSet.toString());


    }
}
