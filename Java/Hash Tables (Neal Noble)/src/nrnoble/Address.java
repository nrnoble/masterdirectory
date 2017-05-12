package nrnoble;

/**
 * Created by Neal on 4/29/2016.
 */
public class Address
{




       private int number;
        private String street;
        private String city;
        private String state;
        private int zip;
        private Integer hash;

        public Address(int number, String street, String city, String state, int zip)
        {
            this.number = number;
            this.street = street;
            this.city = city;
            this.state = state;
            this.zip = zip;
            generateHashCode();
            hash = hashCode();
        }


    @Override
    public boolean equals(Object _obj)
    {

        Address addressObj = (Address) _obj;

        // identical check
        if (this == _obj)
        {
            return true;
        }

        // null check
        if (_obj == null)
        {
            return false;
        }


        // class check
        if (getClass() != _obj.getClass())
        {
            return false;
        }

        // check hash
        if (this.hashCode() != ((Address) _obj).hashCode())
        {
            return false;
        }


        if (this.number != addressObj.number)
        {
            return false;
        }

        if (this.zip != addressObj.zip)
        {
            return false;
        }

        if (!(this.street != null && this.street.equals(addressObj.street) && addressObj.street != null))
        {
            return false;
        }

        if (!(this.city != null && city.equals(addressObj.city) && addressObj.city != null))
        {
            return false;
        }

        if (!(this.state != null && state.equals(addressObj.state) && addressObj.state != null))
        {
            return false;
        }
            return true;
    }

    @Override
    public int hashCode()
    {
        return hash;
    }



    private int generateHashCode()
    {
        String hash = "" + this.number;

        if (street != null)
        {
            hash += street;
        }

        if (city != null)
        {
            hash += city;
        }


        if (state != null)
        {
            hash += state;
        }


        hash += this.zip;

        this.hash = Math.abs (hash.hashCode());
        return this.hash;
    }





       public int getNumber()
        {
            return number;
        }

        public void setNumber(int number)
        {
            this.number = number;
            generateHashCode();
        }

        public String getStreet()
        {
            return street;
        }

        public void setStreet(String street)
        {
            this.street = street;
            generateHashCode();
        }

        public String getCity()
        {
            return city;
        }

        public void setCity(String city)
        {
            this.city = city;
            generateHashCode();
        }

        public String getState()
        {
            return state;
        }

        public void setState(String state)
        {
            this.state = state;
            generateHashCode();
        }

        public int getZip()
        {
            return zip;
        }

        public void setZip(int zip)
        {
            this.zip = zip;
            generateHashCode();
        }




}


