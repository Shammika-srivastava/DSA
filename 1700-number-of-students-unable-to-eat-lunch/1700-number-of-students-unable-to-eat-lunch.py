from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        # Track how many consecutive rotations happen without anyone eating
        rotations = 0
        
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                # Student takes sandwich
                students.popleft()
                sandwiches.popleft()
                rotations = 0  # reset since someone ate
            else:
                # Student goes to end of queue
                students.append(students.popleft())
                rotations += 1
            
            # If all students rotated once without eating, stop
            if rotations == len(students):
                break
        
        return len(students)