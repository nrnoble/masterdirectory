package nrnoble;

/**
 * Created by Neal on 9/25/2016.
 */
public class Order
{
    private int orderID;
    private String Address_line_1;
    private String Address_line_2;
    private String Zip;
    private String City;


    public String getCity()
    {
        return City;
    }

    public void setCity(String city)
    {
        City = city;
    }

    public String getZip()
    {
        return Zip;
    }

    public void setZip(String zip)
    {
        Zip = zip;
    }

    public String getAddress_line_2()
    {
        return Address_line_2;
    }

    public void setAddress_line_2(String address_line_2)
    {
        Address_line_2 = address_line_2;
    }

    public String getAddress_line_1()
    {
        return Address_line_1;
    }

    public void setAddress_line_1(String address_line_1)
    {
        Address_line_1 = address_line_1;
    }

    public int getOrderID()
    {
        return orderID;
    }

    public void setOrderID(int orderID)
    {
        this.orderID = orderID;
    }

    private boolean validateZip()
    {
       return true;
    }



}




