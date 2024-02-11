import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class 회문Two {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static boolean isPalindrome(String str, int start, int end) {
        while (start < end) {
            if (str.charAt(start) != str.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

    public static void run() throws IOException {
        int T = Integer.parseInt(br.readLine());

        while (T > 0) {
            String str = br.readLine();
            int start = 0;
            int end = str.length() - 1;
            int cnt = 0;

            while (start < end) {
                if (str.charAt(start) == str.charAt(end)) {
                    start++;
                    end--;
                } else {
                    if (isPalindrome(str, start + 1, end) || isPalindrome(str, start, end - 1)) {
                        cnt++;
                        break;
                    } else {
                        System.out.println(2);
                        break;
                    }
                }
            }

            if (cnt == 0) {
                System.out.println(0);
            } else if (cnt == 1) {
                System.out.println(1);
            } else {
                System.out.println(2);
            }

            T--;
        }
    }

    public static void main(String[] args) throws IOException {
        run();
    }
}
