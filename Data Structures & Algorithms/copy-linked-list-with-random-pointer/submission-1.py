"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
         
        nodeMap = {}
        current = head

        while current:
            copyNode = Node(current.val)
            nodeMap[current] = copyNode
            current = current.next

        
        for original in nodeMap:
            nodeMap.get(original).next = nodeMap.get(original.next)
            nodeMap.get(original).random = nodeMap.get(original.random)
        
        return nodeMap[next(iter(nodeMap))]