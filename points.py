"""
list of arrays?
a[(clarity), (originality), (difficulty)]
b[(clarity), (originality), (difficulty)]
assign different positions a score
cp = total points a person earned
points = random number
"""
import array as arr

class Points:
    a = arr.array('i', [])
    b = arr.array('i', [])

    def __init__(self, a, b):
        self.a = a
        self.b = b

        """we're trying to compare the points, function should take in a number? or array? """
    def compareTriplets(self, a, b):
        a_cp = 0
        b_cp = 0
        for i in range(0,3):
            if(self.a[i]>self.b[i]):
                a_cp += 1
            if(self.a[i]<self.b[i]):
                b_cp += 1
            else:
                a_cp += 0
                b_cp += 0
        print(a_cp, b_cp)           
def main():
        #I'm thinking of putting an escape thing like a ! or ?, chck if correct though
    a = arr.array('i', [])
    b = arr.array('i', [])
    p = Points(a,b)       
    print("Enter points for the following categories: \n")
    clarity = int(input("Clarity: \n"))
    a.append(clarity)
    originality = int(input("Originality: \n"))
    a.append(originality)
    difficulty = int(input("Difficulty: \n"))
    a.append(difficulty)
    
    print("Enter points for the following categories: \n")
    clarity = int(input("Clarity: \n"))
    b.append(clarity)
    originality = int(input("Originality: \n"))
    b.append(originality)
    difficulty = int(input("Difficulty: \n"))
    b.append(difficulty)
         
    #passing function compareTriplets
    p.compareTriplets(a, b)
main()