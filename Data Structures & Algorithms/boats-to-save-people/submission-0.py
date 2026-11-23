from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        input:
              people - array of ints
                     people[i] is the weight of ith person
               boats - can carry maximum of limit
                       each boat can carry at most two peopl a maximum weight limit
        output:
               return the some of weight of those people at most limit
        Goal:
             I need to to figure out a way to find the minum number of boats to carry ever given person
        
         psedocode:
            first sort there the array
            Need to loop through the array 
            need to account for the heavest person
            If the lightest + heaviest people fit, they share a boat, so move both pointers.
            If they do not fit, the heaviest person cannot share a boat with anyone, 
            because everyone else weighs at least as much as the lightest person. 
            So the heaviest person takes a boat alone, and you move only the pointer at the end.
        '''

        count  = 0
        l = 0
        r = len(people) - 1
        people.sort()
        while l <= r:
            if people[l] + people[r] <= limit:
                count += 1
                r -= 1
                l += 1
            else:
                count += 1
                r -= 1
        return count