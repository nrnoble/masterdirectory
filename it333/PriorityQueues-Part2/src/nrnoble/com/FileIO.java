package nrnoble.com;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;


public class FileIO
{

    public static byte[] readFile(String filePath)
    {
        Path path = Paths.get(filePath);
        return readllBytes(path);
    }



    private static byte[] readllBytes(Path path)
    {
        try
        {
            return Files.readAllBytes(path);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

        return null;
    }


    /**
     * Get the relative path for the executing application
     * @return {String} Path of the executing application
     */
    public static String getPath()
    {
        String path1 = Main.class.getProtectionDomain().getCodeSource().getLocation().getPath();
        String decodedPath = null;
        try
        {
            decodedPath = URLDecoder.decode(path1, "UTF-8");
        } catch (UnsupportedEncodingException e)
        {
            e.printStackTrace();
        }
        decodedPath = decodedPath.substring(1);
        return decodedPath;
    }

    public static String getPath2()
    {
        String path1 = Main.class.getProtectionDomain().getCodeSource().getLocation().getPath();
        String decodedPath = null;
        try
        {
            decodedPath = URLDecoder.decode(path1, "UTF-8");
        } catch (UnsupportedEncodingException e)
        {
            e.printStackTrace();
        }
        decodedPath = decodedPath.substring(1);
        return decodedPath;
    }

}