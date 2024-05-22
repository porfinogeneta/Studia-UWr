class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL(object):

    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # po dodaniu wirzechołka trzeba zaaktualizować wysokości
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # bF = self.getHeight(root.right) - self.getHeight(root.left)

        # # LEFT HEAVY
        # if bF < -1 and key < root.left.key:
        #     return self.rotateRight(root)
        # # RIGHT HEAVY
        # if bF > 1 and key > root.right.key:
        #     return self.rotateLeft(root)
        # # LEFT-RIGHT
        # if bF < -1 and key > root.left.key:
        #     root.left = self.rotateLeft(root.left)
        #     return self.rotateRight(root)
        # # RIGHT-LEFT
        # if bF > 1 and key < root.right.key:
        #     root.right = self.rotateRight(root.right)
        #     return self.rotateLeft(root)

        return self.balanceTree(root)

    def delete(self, root, key):
        if root is None:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # prawy element wkładamy zamiast root'a
            if root.left is None:
                temp = root.right
                root = None
                return temp  # zwracamy temp, bo chcemy go podpiąć do wyrzszego root
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                temp = self.getFirstInOrder(root.right)
                root.key = temp.key
                root.right = self.delete(root.right, temp.key)

        # po usuwaniu naprawiamy wysokości
        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))

        return self.balanceTree(root)

    def balanceTree(self, root):
        # obliczamy balanceFactor, czy drzewo się zaburzyło
        bF = self.getHeight(root.left) - self.getHeight(root.right)

        # drzewo jest niezbalansowane dla bF > 1, a jest typu LEFT-LEFT dla lewego dziecka
        # z bF >= 0 (żeby w korzeniu mogła być liczba >1 to w lewe dziecko powinno dołożyć wysokość)
        if bF > 1 and self.getBalanceFactor(root.left) >= 0:
            return self.rotateRight(root)

        # RIGHT-RIGHT, sytuacja jest symetryczna
        if bF < -1 and self.getBalanceFactor(root.right) <= 0:
            return self.rotateLeft(root)

        # drzewo jest LEFT-RIGHT, gdy jest left-heavy i lewe dziecko ma ujemny bF
        if bF > 1 and self.getBalanceFactor(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # RIGHT-LEFT, sytuacja znowu symetryczna
        if bF < -1 and self.getBalanceFactor(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def getHeight(self, node):
        return 0 if not node else node.height

    # balance factor: root.left - root.right, dla AVL powinno to być {-1,0,1}
    def getBalanceFactor(self, node):
        return 0 if not node or (not node.left and not node.right) else (self.getHeight(node.left) - self.getHeight(node.right))

    def getFirstInOrder(self, root):
        if root.left is None:
            return root
        else:
            self.getFirstInOrder(root.left)

    # rotateLeft -> prawy do lewego rodzic prawego dziecka idzie do lewej gałęzi dziecka
    def rotateLeft(self, node):
        B = node.right
        Y = B.left

        B.left = node
        node.right = Y

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        B.height = 1 + max(self.getHeight(B.left), self.getHeight(B.right))

        return B

    # rotateRight -> lewy do prawego, lewe dzieko wrzuca na korzeń
    def rotateRight(self, node):
        B = node.left
        Y = B.right

        B.right = node
        node.left = Y

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        B.height = 1 + max(self.getHeight(B.left), self.getHeight(B.right))

        return B

    def preOrder(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)


if __name__ == "__main__":
    myTree = AVL()
    root = None
    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)

    # myTree.preOrder(root)

    myTree.delete(root, 30)

    myTree.preOrder(root)
