class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        one_node = TreeNode()

        three_node = TreeNode()
        three_node.left = one_node
        three_node.right = one_node

        cache = [[one_node], [three_node]] + [None] * (n // 2 - 1)

        def possible_nodes(fbt_index):
            if cache[fbt_index] != None:
                return cache[fbt_index]

            return_nodes = []
            for i in range((fbt_index + 1) // 2):
                i_nodes = possible_nodes(i)
                j = fbt_index - i - 1
                j_nodes = possible_nodes(j)

                for i_node in i_nodes:
                    for j_node in j_nodes:
                        node = TreeNode()
                        node.left = i_node
                        node.right = j_node
                        return_nodes.append(node)

                        if i != j:
                            node = TreeNode()
                            node.left = j_node
                            node.right = i_node
                            return_nodes.append(node)

            cache[fbt_index] = return_nodes
            return return_nodes

        return possible_nodes((n - 1) // 2)

