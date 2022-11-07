

# Method 1 using List 

def hasCycle(self, head: Optional[ListNode]) -> bool:
    seen = []

    while head:
        if head in seen:
            return True
        seen.append(head)
        head = head.next

    return False

# using set

def hasCycle(self, head: Optional[ListNode]) -> bool:
	seen = set() #set of nodes we have already seen
	while head:
		if head in seen: #if we already saw this node then there is a cycle
			return True
		seen.add(head) #add node to our list of seen nodes
		head = head.next #visit next node
	return False #we reached the end of the list -- no cycle!

# Method 3: Two-pointers; Time: O(N), Memory: O(1)

def hasCycle(self, head: Optional[ListNode]) -> bool:
	slow = fast = head #slow and fast pointers
	while fast and fast.next: #while not at the end of the list
		slow = slow.next #slow moves forward by 1
		fast = fast.next.next #fast moves forward by 2
		if slow == fast: #if they are the same then we must have a cycle!
			return True
	return False #no cycle found