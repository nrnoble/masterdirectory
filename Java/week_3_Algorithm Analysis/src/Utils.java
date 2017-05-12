
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
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
