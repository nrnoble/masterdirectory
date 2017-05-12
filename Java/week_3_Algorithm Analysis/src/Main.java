public class Main {

    public static void main(String[] args) {


         int testLoop = 10;
         int n = 10;
         Algorithm_1 algorithm_1 = new Algorithm_1(new int[]{250,500,1000,2000});
         Algorithm_2 algorithm_2 = new Algorithm_2(new int[]{25000,50000,100000,200000,400000,800000});
         Algorithm_3 algorithm_3 = new Algorithm_3(new int[]{100000,200000,400000,800000,1600000,3200000,6400000});

        System.out.println("\n\r");
        System.out.println("b) Write (separate) programs to execute each algorithm 10 times, and record the average" +
                " number of operations made each execution.");
        System.out.println("------------------------------------------------------------------------------------" +
                "----------------------------------------------");

        long executionSteps_1 = algorithm_1.testLoop_b(testLoop,n);
        long executionSteps_2 = algorithm_2.testLoop_b(testLoop,n);
        long executionSteps_3 = algorithm_3.testLoop_b(testLoop,n);


        System.out.println("------------------------------------------------------------------------------------" +
                "----------------------------------------------");
        System.out.println("\n\r");

        System.out.println("c) (1) for N = 250, 500, 1,000, 2,000;\n\r   (2) for N = 25,000, " +
                "50,000, 100,000, 200,000, 400,000, 800,000;\r\n   (3) for N = 100,000, 200,000, 400,000, " +
                "800,000, 1,600,000, 3,200,000, 6,400,000.");
        System.out.println("------------------------------------------------------------------------------------" +
                "----------------------------------------------");

        algorithm_1.testLoop_c();
        System.out.println("------------------------------------------------------------------------------------" +
                "----------------------------------------------");
        algorithm_2.testLoop_c();
        System.out.println("------------------------------------------------------------------------------------" +
                "----------------------------------------------");
        algorithm_3.testLoop_c();

        System.out.println("------------------------------------------------------------------------------------" +
                "----------------------------------------------");


        System.out.println("------------------------------------------------------------------------------------" +
                "----------------------------------------------");
        System.out.println("\n\r");
        System.out.println("\n\r");

        System.out.println("\n\r\r\r");
        System.out.println("Exiting program");
    }
}
