from binarysearchtree import BinarySearchTree
def main():
    list_of_nums = []
    numbers = input('Enter a list of numbers separated by commas: ')
    nums = numbers.split(",")
    for item in nums:
        list_of_nums.append(int(item))

    BST = BinarySearchTree()
    for num in list_of_nums:
        BST.add(num)

    BST.pre_order()
    print("---------------")
    BST.post_order()
    print("---------------")
    BST.in_order()

main()