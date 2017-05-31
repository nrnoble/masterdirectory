package nrnoble.com;

/** Class ManualTests **/
public class ManualTests
{
    public static void main(String[] args)
    {

        MaryHeap dh = new MaryHeap(10,3);
        //MarryHeap<Integer> dh = new MarryHeap<>();

        // int[] input = {140,130,120,110,100,90,80,70,60,5,40,30,20,10};
        // int[] input = {14,13,12,11,10,9,8,7,6,5,4,3,2,1};
        // int[] input = {13,12,11,10,9,8,7,6,5,4,3,2,1};
        // int[] input = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
      //   String [] input = {"a", "c", "b", "a"};
        // int[] input = {6, 22, 5, 77, 12, 11, 42, 150, 11, 11, 11};

       //  int[] input = {12,11,10,9,8,7,6,5,4,3,2,1};
         int[] input = {25,8,32,9,5,6,14,4,11,12,3, 2, 1};

            // Broken [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 6, 12, 13, 15, 16, 17, 18, 19, 14, 20, 21, 22, 23, 24, 25]

        // Working MaryHeap Order:           [0]:01, [1]:5, [2]:02, [3]:14, [4]:12, [5]:09, [6]:6, [7]:03, [8]:19, [09]:18, [10]:23, [11]:16, [12]:15, [13]:25, [14]:20, [15]:13, [16]:22, [17]:11, [18]:10, [19]:21, [20]:08, [21]:07, [22]:24, [23]:17, [24]:04
                    // not working [0]:null, [1]:01, [2]:5, [3]:02, [4]:14, [5]:12, [6]:09, [7]:6, [8]:03, [9]:19, [10]:18, [11]:23, [12]:16, [13]:15, [14]:25, [15]:20, [16]:13, [17]:22, [18]:11, [19]:10, [20]:21, [21]:08, [22]:07, [23]:24, [24]:17
    //       int[] input = {25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
           //String[] input = {"z","y","x","w","v","u","t","s","r","q","p","o","n","m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"};

        dh.printHeap();

        for (int i = 0; i < input.length; i++)
        {
            System.out.print("size (" + (String.format("%03d", dh.size()) + ") " + "inserting input[" + String.format("%02d",i) + "]: " + String.format("%02d",input[i]) + "  "));
            dh.insert(input[i]);
            dh.printHeap();
        }



//        for (int i = 1; i <= 10; i++)
//        {
//            System.out.println("inserting: " + i);
//            dh.insert(i);
//        }
//
//
//       for (int i = 11; i > 0; i--)
//        {
//            System.out.println("inserting: " + i);
//            dh.insert(i);
//        }
//


     //   dh.printHeap();

        int lineCount = 0;
      //  MaryHeap dh2 = new MaryHeap(10,3);
     //   MarryHeap<Integer> dh2 = new MarryHeap<>();
        while (!dh.isEmpty())
        {
         //   System.out.print(dh.delete(0) + " ");
            int num = (int) dh.delMin();
            System.out.print(String.format("%03d", ++lineCount) + " Pulling: " + String.format("%03d",num )  + "... ");
            dh.printHeap();
        }
        System.out.println();
        System.out.println();
        System.out.println();
        lineCount = 0;

//        while (!dh2.isEmpty())
//        {
//            //   System.out.print(dh.delete(0) + " ");
//
//            int num = (int) dh2.delMin();
//            System.out.print(String.format("%03d", ++lineCount) + " Pulling: " + String.format("%03d",num )  + "... ");
//            dh2.printHeap();
//        }
//        System.out.println();

    }
}