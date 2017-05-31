package nrnoble.com;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
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

}