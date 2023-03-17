import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n, min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
	static int[] num, opr = new int[4];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine()); num = new int[n];

		StringTokenizer st1 = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) num[i] = Integer.parseInt(st1.nextToken());
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) opr[i] = Integer.parseInt(st2.nextToken());

		DFS(1, num[0]);
		System.out.println(max + "\n" + min);
	}

	static void DFS(int depth, int x) {
		if (depth == n) {
			min = Math.min(min, x);
			max = Math.max(max, x);
			return;
		}

		for (int i = 0; i < opr.length; i++) {
			if (opr[i] >= 1) {
				opr[i]--;
				switch (i) {
				case 0: DFS(depth + 1, x + num[depth]); break;
				case 1: DFS(depth + 1, x - num[depth]); break;
				case 2: DFS(depth + 1, x * num[depth]); break;
				case 3: DFS(depth + 1, x / num[depth]); break;
				}
				opr[i]++;
			}
		}
	}
}