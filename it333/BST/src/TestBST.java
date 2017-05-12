/**
 * Created by Neal on 5/2/2017.
 */
public class TestBST
{
    public static void main(String[] args)
    {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        bst.add(60);
        bst.add(41);
        bst.add(74);
        bst.add(16);
        bst.add(53);
        bst.add(46);
        bst.add(55);
        bst.add(42);

        System.out.println("contains(60): " + bst.contains(60));
        System.out.println("contains(74): " + bst.contains(74));
        System.out.println("contains(0): " + bst.contains(0));

        bst.remove(60);
       System.out.println("contains(60): " + bst.contains(60));

        bst.inOrder();
        System.out.println();
        bst.postOrder();
        System.out.println();
        bst.preOrder();
        System.out.println();

            for (int element : bst)
            {
                System.out.println(element);
            }
    }
}
