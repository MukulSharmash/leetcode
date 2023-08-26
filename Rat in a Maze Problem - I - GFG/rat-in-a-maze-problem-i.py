#User function Template for python3

class Solution:
    def check(m,nx,ny,n,visited)->bool:
        if(nx<0 or nx>n-1 or ny<0 or ny>n-1):
            return False
        if(m[nx][ny]!=1):
            return False
        if(visited[nx][ny]==1):
            return False
        return True
    
    def solve(m,n,l,x,y,visited,s):
        if(x==n-1 and y==n-1):
            l.append(s[:])
            return
        visited[x][y]=1
        #down
        nx=x+1
        ny=y
        f=Solution.check(m,nx,ny,n,visited)
        if(f==True):
            s.append("D")
            Solution.solve(m,n,l,nx,ny,visited,s)
            s.pop()
        
        #lefft
        nx=x
        ny=y-1
        f=Solution.check(m,nx,ny,n,visited)
        if(f==True):
            s.append("L")
            Solution.solve(m,n,l,nx,ny,visited,s)
            s.pop()
        
        #right
        nx=x
        ny=y+1
        f=Solution.check(m,nx,ny,n,visited)
        if(f==True):
            s.append("R")
            Solution.solve(m,n,l,nx,ny,visited,s)
            s.pop()
            
        #up
        nx=x-1
        ny=y
        f=Solution.check(m,nx,ny,n,visited)
        if(f==True):
            s.append("U")
            Solution.solve(m,n,l,nx,ny,visited,s)
            s.pop()
        
        visited[x][y]=0
    
    def findPath(self, m, n):
        if(m[0][0]==0):
            return []
        x=0
        y=0
        l=[]
        visited=[]
        for i in range(n):
            a=[]
            for j in range(n):
                a.append(0)
            visited.append(a)
        
        s=[]
        d=[]
        Solution.solve(m,n,l,x,y,visited,s)
        for i in range(len(l)):
            a=""
            for j in l[i]:
                a=a+j
            d.append(a)
        d.sort()
            
        return d


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends