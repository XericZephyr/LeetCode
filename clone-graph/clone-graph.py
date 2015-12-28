
from utils import UndirectedGraphNode


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        stack = [node]
        visit = {node.label: UndirectedGraphNode(node.label)}
        while stack:
            current = stack.pop()
            for n in current.neighbors:
                if n.label not in visit:
                    stack.append(n)
                    visit[n.label] = UndirectedGraphNode(n.label)
                visit[current.label].neighbors.append(visit[n.label])
        return visit[node.label]


if __name__ == '__main__':
    root = UndirectedGraphNode(-1)
    node2 = UndirectedGraphNode(1)
    root.neighbors.append(node2)
    node2.neighbors.append(root)
    node2.neighbors.append(node2)
    print root.neighbors
    print root[1].neighbors

    root_clone = Solution().cloneGraph(root)
    print root_clone.neighbors
    print root_clone[1].neighbors

