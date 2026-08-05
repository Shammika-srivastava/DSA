class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build graph (adjacency list)
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)  # to check incoming edges
        for a, b in invocations:
            graph[a].append(b)
            reverse_graph[b].append(a)
        
        # Step 2: DFS to find suspicious methods starting from k
        suspicious = set()
        
        def dfs(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for nei in graph[node]:
                dfs(nei)
        
        dfs(k)
        
        # Step 3: Check if removal is possible
        # If any outside node calls into suspicious set → not removable
        for s in suspicious:
            for caller in reverse_graph[s]:
                if caller not in suspicious:
                    # Outside method depends on suspicious → cannot remove
                    return list(range(n))
        
        # Step 4: Return remaining methods
        return [i for i in range(n) if i not in suspicious]
