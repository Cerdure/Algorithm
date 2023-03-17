import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static StringBuilder sb = new StringBuilder();
	static int count = 0;

	public static void main(String[] args) {
		int N = sc.nextInt();
		set(N, 1, 2, 3);
		System.out.println(count + "\n" + sb);
	}

	static void set(int N, int s1, int s2, int s3) {
		count++;
		if (N == 1) {
			sb.append(s1 + " " + s3 + "\n");
		} else {
			set(N - 1, s1, s3, s2);
			sb.append(s1 + " " + s3 + "\n");
			set(N - 1, s2, s1, s3);
		}
	}
}