/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) {
        return '';
    }
    res = strs[0];
    for (let str of strs) {
        for (var i=0; i<str.length; i++) {
            if (str[i] !== res[i]) {
                break;
            }
        }
        res = res.slice(0,i);
    }
    return res;
};