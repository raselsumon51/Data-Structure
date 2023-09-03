class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None:
        return 0
    
    # Initialize a queue for level-order traversal
    queue = [root]
    depth = 0

    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        
        for i in range(level_size):
            # Dequeue a node
            node = queue.pop(0)

            # Enqueue its left and right children if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Increment the depth for each level
        depth += 1
    
    return depth

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Find the maximum depth of the tree
depth = maxDepth(root)
print("Maximum depth of the binary tree:", depth)
