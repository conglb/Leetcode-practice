/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    var prev = [];
    for (let i=0; i<=m; i++) {
        prev.push(0)
    }
    prev[1] = 1;
    for (let i=1; i<=n; i++) {
        pre = 0;
        for (let j=1; j<=m; j++) {
            cur = pre + prev[j];
            prev[j] = cur;
            pre = cur;
        }
    }
    return cur
};