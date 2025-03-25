class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if self.checkHorizontalCuts(rectangles):
            return True
        if self.checkVerticalCuts(rectangles):
            return True
        
        return False
    
    def checkHorizontalCuts(self, rectangles):
        events = []
        for startx, starty, endx, endy in rectangles:
            events.append((starty, 1))  
            events.append((endy, -1))  
        
        events.sort()
        valid_cuts = []
        active_rectangles = 0
        prev_y = -1
        
        for y, event_type in events:
            if active_rectangles == 0 and prev_y != -1:
                valid_cuts.append(y)
            
            active_rectangles += event_type
            prev_y = y
        
        for i in range(len(valid_cuts) - 1):
            cut1 = valid_cuts[i]
            for j in range(i + 1, len(valid_cuts)):
                cut2 = valid_cuts[j]
                below, between, above = 0, 0, 0
                
                for startx, starty, endx, endy in rectangles:
                    if endy <= cut1:
                        below += 1
                    elif starty >= cut2:
                        above += 1
                    else:
                        between += 1
                
                if below > 0 and between > 0 and above > 0:
                    return True
        
        return False
    
    def checkVerticalCuts(self, rectangles):
        events = []
        for startx, starty, endx, endy in rectangles:
            events.append((startx, 1))  # Rectangle starts
            events.append((endx, -1))   # Rectangle ends
        
        events.sort()
        
        valid_cuts = []
        active_rectangles = 0
        prev_x = -1
        
        for x, event_type in events:
            if active_rectangles == 0 and prev_x != -1:
                valid_cuts.append(x)
            
            active_rectangles += event_type
            prev_x = x
        
        for i in range(len(valid_cuts) - 1):
            cut1 = valid_cuts[i]
            for j in range(i + 1, len(valid_cuts)):
                cut2 = valid_cuts[j]
                left, between, right = 0, 0, 0
                
                for startx, starty, endx, endy in rectangles:
                    if endx <= cut1:
                        left += 1
                    elif startx >= cut2:
                        right += 1
                    else:
                        between += 1
                
                if left > 0 and between > 0 and right > 0:
                    return True
        
        return False

def test_checkValidCuts():
    solution = Solution()
    
    # Test case 1: Example 1 from the problem
    n1 = 5
    rectangles1 = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    result1 = solution.checkValidCuts(n1, rectangles1)
    print(f"Test case 1: {result1}")  
    
    # Test case 2: Example 2 from the problem
    n2 = 4
    rectangles2 = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    result2 = solution.checkValidCuts(n2, rectangles2)
    print(f"Test case 2: {result2}")  
    
    # Test case 3: Example 3 from the problem
    n3 = 4
    rectangles3 = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    result3 = solution.checkValidCuts(n3, rectangles3)
    print(f"Test case 3: {result3}") 
    
    # Custom test case
    n4 = 6
    rectangles4 = [[0,0,2,2],[3,0,5,2],[0,3,2,5],[3,3,5,5]]
    result4 = solution.checkValidCuts(n4, rectangles4)
    print(f"Test case 4: {result4}")  


if __name__ == "__main__":
    test_checkValidCuts()