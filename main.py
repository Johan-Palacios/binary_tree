from core.binary_tree import BinaryTree
from core.utils import to_list


def createBinaryTree(nodes):
    tree = BinaryTree()
    for node in nodes:
        tree.insert(node)
    return tree


def main():
    nodes = (
        input("Introduce los nodos separados por comas: ").replace(" ", "").split(",")
    )
    nodes = to_list(nodes)
    print(f"Tu lista = { nodes }")
    tree = createBinaryTree(nodes)
    # Draw Tree
    tree.drawtree(tree.root)
    # Print traversals
    print("Recorrido Post orden")
    print(tree.postorder(tree.root, []))
    print("Recorrido En orden")
    print(tree.inorder(tree.root, []))
    print("Recorrido Pre orden")
    print(tree.preorder(tree.root, []))
    print("Recorrido por niveles")
    print(tree.levelorder(tree.root))


if __name__ == "__main__":
    main()
