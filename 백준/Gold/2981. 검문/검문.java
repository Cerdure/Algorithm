import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static ArrayList<Integer> al = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine()), m = n;
		int[] iar = new int[n];

		while (n-- > 0) iar[n] = Integer.parseInt(br.readLine());

		Arrays.sort(iar);
		int gcd = iar[1] - iar[0];

		for(int i = 2; i < m; i++) gcd = GCD(gcd, iar[i] - iar[i - 1]);
		for(int i = 2; i <= gcd; i++) if(gcd % i == 0) System.out.print(i + " ");
	}

	private static int GCD(int a, int b) {
		while (b != 0) {
			int temp = a % b;
			a = b;
			b = temp;
		}
		return a;
	}
}