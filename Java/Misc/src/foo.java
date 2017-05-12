/**
 * Created by Neal on 5/4/2016.
 */
public class foo<T>
{
    private T t;

    public foo (T _item)
    {
        t = _item;
    }

    public T get(){
        return this.t;
    }

    public void set(T t1){
        this.t=t1;
    }
}
