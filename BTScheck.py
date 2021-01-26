def BSTcheck(tree):
    if tree:
        leftChild = tree.getLeftChild()
        rightChild = tree.getRightChild()
    
        if leftChild != None:
            if leftChild.getRootVal() > tree.getRootVal():
                return False
        
        if rightChild != None:
            if rightChild.getRootVal() < tree.getRootVal():
                return False

    if tree:
        holder = BSTcheck(tree.getLeftChild())
        holder2 = BSTcheck(tree.getRightChild())
        
        if holder == False or holder2 == False:
            return False
            
    return True