public class euler255
{
    public static int intSqrt(long n)
    {
        int numOfDigits = n.toString().length();
        return numOfDigits;
    }
    public static void main(String[] args)
    {
        long l = 2938424902403;
        System.out.println(intSqrt(l));
    }
}