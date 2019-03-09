class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
  		int m = grid.size();
  		if (m == 0) return 0;
  		int n = grid[0].size();

  		int f[m][n];
  		for (int i = 0; i < m; i++) {
  			for (int j = 0; j < n; j++) {
  				f[i][j] = 123456789;
	  			if (i != 0) {
	  				f[i][j] = f[i-1][j] + grid[i][j];
	  			}
	  			if (j != 0) {
	  				f[i][j] = f[i][j-1] + grid[i][j];
	  			}
	  			if (i == 0 && j == 0) f[i][j] = grid[i][j];
  			}
  		}
  		return f[m-1][n-1];
    }
};