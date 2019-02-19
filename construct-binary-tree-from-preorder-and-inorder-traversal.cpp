/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	TreeNode* build(vector<int>& preorder, vector<int>& inorder, int inPre, int leftIn, int rightIn) {
        cout << inPre << " " << leftIn << " " << rightIn << endl;
		if (leftIn > rightIn || leftIn < 0 || rightIn < 0 || leftIn == preorder.size() || rightIn == preorder.size()) {
			cout << "NULL apeard";
			return NULL;
		}
		if (leftIn == rightIn) {
			return new TreeNode(preorder[inPre]);
		}
        int i;
		for (i=leftIn; i<=rightIn; i++) 
		if (inorder[i] == preorder[inPre])
		{
			break;
		}
		TreeNode* root = new TreeNode(preorder[inPre]);
		root->left = this->build(preorder, inorder, inPre + 1, leftIn, i-1);
		root->right = this->build(preorder, inorder, inPre + i - leftIn + 1, i+1, rightIn);
		return root;
	}
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
		return build(preorder, inorder, 0, 0, inorder.size() - 1);
    }
};