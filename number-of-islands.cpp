char **arr;
int r,c;


void DFS(int x, int y) {
    if (x < 0 || x >= r || y < 0 || y >= c || arr[x][y] == '0') {
        return;
    }
    arr[x][y] = '0';
    DFS(x+1, y);
    DFS(x, y+1);
    DFS(x, y-1);
    DFS(x-1, y);
}

int numIslands(char** grid, int gridRowSize, int gridColSize) {
    arr = grid;
    r = gridRowSize;
    c = gridColSize;
    int ans = 0;
    for (int i=0; i<gridRowSize; i++) {
        for (int j=0; j<gridColSize; j++) {
            if (grid[i][j] == '1') {
                DFS(i,j);
                ans += 1;
            }
        }
    }
    return ans;
}

