#User function Template for python3

class Solution:
    def MedianOfArrays(self, a1, a2):
            #code here
        m=len(a1)
        n=len(a2)
        h=(m+n)
        l=[]
        a=h//2
        i=0
        j=0
        while(i+j<=a+1 and i<m and j<n):
            if(a1[i]<a2[j]):
                l.append(a1[i])
                i+=1
            else:
                l.append(a2[j])
                j+=1
        while(i+j<=a+1 and i<m):
            l.append(a1[i])
            i+=1
        while(i+j<=a+1 and j<n):
            l.append(a2[j])
            j+=1
        if(h%2!=0):
            return l[a]
        s=(l[a]+l[a-1])
        if(s%2==0):
            return int(s/2)
        return s/2
            
            

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends