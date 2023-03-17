import java.io.*;
import java.util.Arrays;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static char[][] arr;

	static void arrValue(int w, int h, int N, boolean isSpace) {
		int index = 0;
		int Box9 = N / 3;
		if (isSpace == true) {
			for (int i = w; i < w + N; i++) {
				for (int j = h; j < h + N; j++) {
					arr[i][j] = ' ';
				}
			}
			return;
		}
		if (N <= 1) {
			arr[w][h] = '*';
			return;
		}
		for (int i = w; i < w + N; i += Box9) {
			for (int j = h; j < h + N; j += Box9) {
				index++;
				if (index == 5) {
					arrValue(i, j, Box9, true);

				} else {
					arrValue(i, j, Box9, false);
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		arr = new char[N][N];

		arrValue(0, 0, N, false);

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				sb.append(arr[i][j]);
			}
			sb.append("\n");
		}
		bw.write(sb.toString());
		bw.flush();
	}
}
