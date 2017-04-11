package part1;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * Created by Neal on 4/9/2017.
 */
public class ShaHash
{


    ShaHash()
    {
        // default constructor
    }

    // from http://www.sha1-online.com/sha256-java/
    public static String getShaHash (Object obj) {
        String text = "abc";
        MessageDigest digest = null;
        try {
            digest = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        byte[] encodedBytes = new byte[0];


        encodedBytes = serialize(obj);

        byte[] hashArray = digest.digest(encodedBytes);
        StringBuffer strBuff = new StringBuffer();
        for (int i = 0; i < hashArray.length; i++) {
            strBuff.append(Integer.toString((hashArray[i] & 0xff) + 0x100, 16).substring(1));
        }

        return strBuff.toString();
    }



    // from http://stackoverflow.com/questions/3736058/java-object-to-byte-and-byte-to-object-converter-for-tokyo-cabinet
    public static byte[] serialize(Object obj)
    {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        ObjectOutputStream os = null;
        try {
            os = new ObjectOutputStream(out);
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            os.writeObject(obj);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return out.toByteArray();
    }
}
