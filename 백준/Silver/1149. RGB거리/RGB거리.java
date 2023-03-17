import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
	static int[][] cost, dp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine()), o=-1; 
		cost = new int[n][3]; dp = new int[n][3];
		
		while(o++<n-1) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			cost[o][0]=Integer.parseInt(st.nextToken());
			cost[o][1]=Integer.parseInt(st.nextToken());
			cost[o][2]=Integer.parseInt(st.nextToken());
		}
		dp[0][0] = cost[0][0];
		dp[0][1] = cost[0][1];
		dp[0][2] = cost[0][2];
		
		int[] cost3 = {cost(n-1,0),cost(n-1,1),cost(n-1,2)};
		int result = Arrays.stream(cost3).min().getAsInt();
		System.out.println(result);
	}
	
	static int cost(int n, int color) {
		if(dp[n][color]==0) {
			if(color==0) dp[n][0] = Math.min(cost(n-1,1),cost(n-1,2))+cost[n][0];
			else if(color==1) dp[n][1] = Math.min(cost(n-1,0),cost(n-1,2))+cost[n][1];
			else dp[n][2] = Math.min(cost(n-1,1),cost(n-1,0))+cost[n][2];
		}
		return dp[n][color];
	}
}