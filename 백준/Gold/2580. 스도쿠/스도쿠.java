import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	public static int[][] arr = new int[9][9];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				
		for (int i = 0; i < 9; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < 9; j++) arr[i][j] = Integer.parseInt(st.nextToken());
		}
		fill_sdk(0, 0);
	}

	public static void fill_sdk(int row, int col) {
		if (col == 9) {
			fill_sdk(row + 1, 0); return;
		}
		if (row == 9) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) sb.append(arr[i][j]).append(' ');
				sb.append('\n');
			}
			System.out.println(sb); System.exit(0);
		}
		if (arr[row][col] == 0) {
			for (int i = 1; i <= 9; i++) {
				if (notOverlap(row, col, i)) {
					arr[row][col] = i;
					fill_sdk(row, col + 1);
				}
			}
			arr[row][col] = 0; return;
		}
		fill_sdk(row, col + 1);
	}

	public static boolean notOverlap(int row, int col, int value) {
		for (int i = 0; i < 9; i++) if (arr[row][i] == value) return false;
		for (int i = 0; i < 9; i++) if (arr[i][col] == value) return false;
		for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++)
		if (arr[i + (row / 3) * 3][j + (col / 3) * 3] == value) return false;
		return true;
	}
}