package recursive;
import java.math.*;
/*
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。
 */
public class leetcode_50 {
    public double myPow(double x, int n) {
//        return myPow_v1(x, n);
        return myPow_v2(x, n);

    }
    public double myPow_v1(double x, int n) {
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        double res = helper(x, n);
        return res;
    }

    public double helper(double x, int n) {
        if (n == 0) {
            return 1.0;
        }

        double res = helper(x, n / 2);
        if (n % 2 == 0) {
            return res * res;
        } else {
            return res * res * x;
        }

    }
    public double myPow_v2(double x, int n) {
        if (n == 0) {
            return 1;
        } else if (n < 0) {
            n = -n;
            x = 1 / x;
        }
        return n % 2 == 0 ? myPow_v2(x * x, n / 2) : x * myPow_v2(x * x, n / 2);
    }

    public static void main(String[] args) {
        leetcode_50 obj = new leetcode_50();
        double x = 2.00000;
        int n = 10;
        double res = obj.myPow(x, n);
        System.out.println(res);
    }
}
