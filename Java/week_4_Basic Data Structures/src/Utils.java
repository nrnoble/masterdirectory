import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ThreadLocalRandom;

public class Utils
{
    private static int COLUMWIDTH = 20;
    private static String DELETEDATAQUERY = "DELETE FROM nnoble_301.fruit WHERE 1";
    public static String SELECTQUERY = "SELECT `type`, `origin`, `weight`, `description` \rFROM nnoble_301.fruit";
    public Utils()
    {
        // TODO Auto-generated constructor stub
    }

    public static String underScore (String _string)
    {
        int strLength = _string.length();
        String underScoreString = "";
        for (int idx = 0;  idx < strLength; idx++)
        {
            underScoreString += "-";
        }

        return  underScoreString;

    }


    /**
     *
     * @param str string of characters
     * @param padding width of white spaces
     * @return padded string
     */
    public static String padRight(String str, int padding)
    {
        return String.format("%1$-" + padding + "s", str);
    }


    /**
     *
     * @param str string of characters
     * @param padding width of white spaces
     * @return padded string
     */
    public static String padLeft(String str, int padding) {
        return String.format("%1$" + padding + "s", str);
    }


    public static List<Integer> getRandomNumbers(int total, int lowerRange, int upperRange)
    {
        List<Integer> list = new ArrayList<Integer>();
        Random rnd = new Random();
        for (int i = 0; i <= total; i++)
        {
            Integer randomNumber = rnd.nextInt((upperRange - lowerRange) + 1) + lowerRange;
            System.out.println(randomNumber);
            list.add(randomNumber);
        }
        return list;
    }





    public static ArrayList<Integer>  randomNumberList (int _size)
    {
        ArrayList<Integer> randomNunbers  = new ArrayList<Integer>(_size);
        for (int i = 0; i < _size ; i++)
        {
            randomNunbers.add(randInt(1,_size));
        }

        return randomNunbers;
    }


    public static ArrayList<Integer> randomNumberList (int _size, int _lowerBound, int _upperBound)
    {
        ArrayList<Integer> randomNunbers  = new ArrayList<Integer>(_size);
        for (int i = 0; i < _size ; i++)
        {
            randomNunbers.add(randInt(_lowerBound,_upperBound));
        }

        return randomNunbers;
    }


    public static List<Integer> getUniqueRandomNumbers(int _size, int _lowerBound, int _upperBound)
    {

        ArrayList<Integer> randomNumbers = getUniqueRandomNumbers(_lowerBound, _upperBound);
        List<Integer> subList = randomNumbers.subList(0,_size);

//        for (Integer item : subList)
//        {
//            System.out.println("item: " + item );
//        }
//
        
        return subList;

    }



    public static ArrayList<Integer> getUniqueRandomNumbers(int _lower, int upperBound)
    {
        int counter = 0;                                            // counter++;
        ArrayList<Integer> randomNumbers = new ArrayList<Integer>(upperBound);                          // counter++;
        for (int i = _lower; i < upperBound; i++)
        {                                                           // counter++;
            int num = i+1;
            randomNumbers.add(num);                               //counter++;
            //System.out.println("i + 1: " + num);
        }

        for (int i = _lower; i < upperBound; i++)
        {
            int randomPosition  = Utils.randInt(_lower, upperBound - 1);
            int currentNumber  = randomNumbers.get(i);
            randomNumbers.set(i, randomNumbers.get(randomPosition));
            randomNumbers.set(randomPosition, currentNumber);
        }

//        for (Integer item : randomNumbers)
//        {
//            System.out.println("randomNumbers: " + item );
//        }



        return randomNumbers;
    }



    private static int randTestNum(int low, int high)
    {
        int randNum = 0;
        while(randNum == 0)
        {
            randNum = randInt(low,high);
        }
        return randNum;
    }

    /**
     *
     * @param _min lowest random value
     * @param _max highest random value
     * @return random number
     */
    public static int randInt(int _min, int _max)
    {
        return ThreadLocalRandom.current().nextInt(_min, _max + 1);

    }
    public static double randDouble(double _min, double _max)
    {
        return ThreadLocalRandom.current().nextDouble(_min, _max + 1);

    }


    /**
     *
     * @param _connnectToRemoteDB connection to DB
     * @return status of insert query
     * @throws SQLException exception
     * @return ResultSet
     */
    public static ResultSet viewFruit(Connection _connnectToRemoteDB) throws SQLException
    {
        //create a statement and query
        Statement stmt = _connnectToRemoteDB.createStatement();
        ResultSet resultSet = stmt.executeQuery(SELECTQUERY);
        displaySQLTable(resultSet);
        return resultSet;
    }

    /**
     *
     * @param connnectToRemoteDB connection to DB
     * @throws SQLException exception
     * @return true\false
     */
    public static boolean deleteSampleData(Connection connnectToRemoteDB) throws SQLException
    {
        //create a statement and query
        Statement stmt = connnectToRemoteDB.createStatement();
        return stmt.execute(DELETEDATAQUERY);
        //return stmt.executeUpdate(DELETEDATAQUERY);
    }



    /**
     * Display a basic text SQL Table in console
     * @param resultSet SQL table data
     * @throws SQLException Exception
     */
    public static void displaySQLTable(ResultSet resultSet) throws SQLException
    {
        // Get column data
        ResultSetMetaData metadata = resultSet.getMetaData();

        // display column headings
        int columCount = metadata.getColumnCount();
        for (int idx=1; idx <= columCount; idx++)
        {
            String ColumnName = Utils.padRight(metadata.getColumnName(idx),COLUMWIDTH);
            System.out.print(ColumnName);
        }

        System.out.println();

        // underscore the column headings
        for (int idx=1; idx <= columCount; idx++)
        {
            String ColumnName = Utils.padRight(Utils.underScore(metadata.getColumnName(idx)),COLUMWIDTH);
            System.out.print(ColumnName);
        }

        System.out.println();

        // display rows of data
        while(resultSet.next() != false)
        {
            // display a single row of data
            for (int idx=1; idx <= columCount; idx++)
            {
                String row =resultSet.getString(idx);
                String columData = Utils.padRight(row,COLUMWIDTH);
                System.out.print(columData);
            }
            System.out.println("");

        }


    }


}
