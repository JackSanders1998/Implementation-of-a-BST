import lab2
import unittest



class T0_tree__insert(unittest.TestCase):

    def test_tree_insert(self):
        print("\n")
        print("tree_insert_skewed")
        tree = lab2.Tree()

        for i in range(1, 8):
            tree.insert(i)

        list_tree = [node for node in tree]
        last_node = tree.root.right.right.right.right.right.right.data
        self.assertEqual(list_tree, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(last_node, 7)

        print("\n")

    def test_tree_insert_individual_check(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab2.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checking the min and the max functions")
        t = lab2.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum.data, 1)
        maximum = t.max()
        self.assertEqual(maximum.data, 7)

        print("\n")

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab2.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        postorder = [node for node in t.postorder()]

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("postorder traversal")
        self.assertEqual(postorder,[1, 3, 2, 5, 7, 6, 4])
        print("\n")




class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab2.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab2.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]


        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab2.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

class T6_empty_tree(unittest.TestCase):
    

    def test_empty_tree(self):
        print("\n")
        print("empty tree")
        t1 = lab2.Tree()
        empty_list1 = [node for node in t1]
        empty_list2 = [node for node in t1.inorder()]
        empty_list3 = [node for node in t1.preorder()]
        empty_list4 = [node for node in t1.postorder()]
        
        self.assertEqual(t1.min(), None)
        self.assertEqual(t1.max(), None)
        self.assertEqual(empty_list1, [])
        self.assertEqual(empty_list2, [])
        self.assertEqual(empty_list3, [])
        self.assertEqual(empty_list4, [])

        with self.assertRaises(KeyError):
            t1.find_successor(4)
            t1.delete(5)
        print("\n")

if __name__ == '__main__' :
    unittest.main()