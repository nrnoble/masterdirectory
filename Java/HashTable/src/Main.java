public class Main {

    public static void main(String[] args)
    {
        System.out.println("Hello World!");


        MyHashTable<String> wordSet = new MyHashTable<String>();

        wordSet.add("red");
        wordSet.add("black");
        wordSet.add("blue");
        wordSet.add("green");
        wordSet.add("white");
        wordSet.add("pink");

        System.out.println("Before " + wordSet.toString());


        wordSet.add("purple");

        System.out.println("After " + wordSet.toString());

    }
}
