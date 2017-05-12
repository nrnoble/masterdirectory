package nrnoble;

import java.util.HashSet;

class Main
{
            public static void main(String[]args)
            {

                
                // Hashcode tests
                Address myAddress0 = new Address(1102,"8th ST NE", "Auburn","WA",98002);
                Address myAddress1 = new Address(1102,"8th ST NE", "Auburn","WA",98002);
                Address myAddress2 = new Address(1120,"8th ST NE", null,"WA",98002);
                System.out.println("myAddress0 hash: " + myAddress0.hashCode());
                System.out.println("myAddress1 hash: " + myAddress1.hashCode());
                System.out.println("myAddress2 hash: " + myAddress2.hashCode());

                if (myAddress0.hashCode() == myAddress1.hashCode())
                {
                    System.out.println("Hashcode Test: Pass. Both hash code match: " + myAddress1.hashCode());
                }
                else
                {
                    System.out.println("Hashcode Test: Fail. Hash codes do not match. myAddress0=" +
                            myAddress0.hashCode() + " myAddress1=" + myAddress1.hashCode() );
                }


                if (myAddress0.equals(myAddress1))
                {
                    System.out.println("Equals() Test: Pass. Both objects are equal. Hashcode: "
                            + myAddress1.hashCode());
                }
                else
                {
                    System.out.println("Equals() Test: Fail. Hash codes do not match. myAddress0 = "
                            + myAddress0.hashCode() + ", myAddress1 = " + myAddress1.hashCode() );
                }
                // End of hash code tests
                System.out.println();
                System.out.println();


                HashSet<String> wordSet = new HashSet<String>();

                wordSet.add("red");
                wordSet.add("black");
                wordSet.add("blue");
                wordSet.add("green");
                wordSet.add("white");
                wordSet.add("pink");

                wordSet.add("purple");
                wordSet.add("orange");
                wordSet.add("yellow");

                // should throw error when exceeding internal array size
                // resize has been disables per assignment instructions
               // wordSet.add("grey");

                System.out.println(wordSet.toString());

                if (wordSet.contains("black"))
                {
                    System.out.println("contains() Test passed: found the element 'black'");
                }
                else
                {
                    System.out.println("contains() Test failed: unable to find element 'black'");
                }


                // now remove the element 'black'
                if (wordSet.remove("black"))
                {
                    System.out.println("remove() Test passed: removed the element 'black'");
                }
                else
                {
                    System.out.println("remove() Test failed: unable remove element 'black'");
                }


                // verify black is nolonger in list
                if (!wordSet.contains("black"))
                {
                    System.out.println("contains() Test passed: found the element 'black' is nolonger in list");
                }
                else
                {
                    System.out.println("contains() Test failed: the element 'black' is still exists");
                }


                System.out.println(wordSet.toString());



            }

}