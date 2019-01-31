/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
    let res = [];
    let degree = 0;
    let dfs = function(u) {
        degree += 1;
        if (degree > res.length) {
            res.push(u.val);
        }
        if (u.right !== null) {
            dfs(u.right);
        }
        if (u.left !== null) {
            dfs(u.left);
        }
        degree -= 1;
    }
    if (root === null) {
        return res;
    } else {
        dfs(root);
        return res;
    }
};