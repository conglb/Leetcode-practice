/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    var pre = [];
    for (let i=0; i<obstacleGrid[0].length; i++) {
        pre.push(0);
    }
    pre[0] = 1
    for (let line of obstacleGrid) {
        prev = 0;
        for (let i=0; i<line.length; i++) {
            if (line[i] === 0) {
                cur = pre[i] + prev;
            } else {
                cur = 0;
            }
            pre[i] = cur;
            prev = cur;
            console.log(cur)
        }
    }
    return cur
};