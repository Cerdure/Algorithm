import java.util.Scanner;

public class Main {
	static int n, count = 0;
	static int[] columnOf = new int[15];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		N_Queen(0);
		System.out.println(count);
	}

	static boolean isPossible(int n) {
		for (int i = 0; i < n; i++) {
			if (columnOf[n] == columnOf[i] || n - i == Math.abs(columnOf[n] - columnOf[i]))
				return false;
		}
		return true;
	}

	static void N_Queen(int x) {
		if (x == n) { 
			count++;
			return;
		}
		for (int i = 0; i < n; i++) {
			columnOf[x] = i;
			if (isPossible(x)) {
				N_Queen(x + 1);
			}
		}
	}
}