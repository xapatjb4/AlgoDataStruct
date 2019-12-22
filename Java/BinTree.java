/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.ArrayList;
import java.util.List;

class BinTree{
  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
  }
  
  public List<Integer> preorderTraversal(TreeNode root) {
    //root left right for preorder
    List<Integer> toAdd = new ArrayList<Integer>();
        
    //If root null return empty arraylist
    if(root == null)
    return toAdd; //there's nothing in node
        
    //Add root
    toAdd.add(root.val);
        
    //add left
    toAdd.addAll(preorderTraversal(root.left));
        
    //add right
    toAdd.addAll(preorderTraversal(root.right));
        
    //return List
    return toAdd;
   
  }
}
