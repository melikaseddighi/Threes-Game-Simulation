n=int(input())
mat=[]
for i in range(n):
    m=input().split()
    mat+=[m]

matemp=[j[:] for j in mat]
    
harkat=input()
math=[]
for j in range(len(harkat)):
    x=input().split()
    math+=[x]
    
    
def D(mat1):
    for i in range(n-2,-1,-1):
        for j in range(n):
            if  mat1[i][j]!='0' and mat1[i+1][j]=='0' :
                mat1[i+1][j]=mat1[i][j]
                mat1[i][j]='0'
                #break
                
            elif mat1[i+1][j]=='1':
                if mat1[i][j]!='2':
                    flag=False
                    #no change
                elif mat1[i][j]=='2':
                    mat1[i+1][j]='3'
                    mat1[i][j]='0'
                     
            elif mat1[i+1][j]=='2':
                if mat1[i][j]!='1':
                    flag=False
                    #no change
                elif mat1[i][j]=='1':
                    mat1[i+1][j]='3'
                    mat1[i][j]='0'
                    
            else:
                if mat1[i+1][j]==mat1[i][j]:
                    mat1[i+1][j]=str(2*int(mat1[i][j]))
                    mat1[i][j]='0'
    return mat1

def U(mat2):
    for i in range(1,n):
        for j in range(n):
            if  mat2[i][j]!='0' and mat2[i-1][j]=='0' :
                mat2[i-1][j]=mat2[i][j]
                mat2[i][j]='0'
                #break
                
            elif mat2[i-1][j]=='1':
                if mat2[i][j]!='2':
                    flag=False
                    #no change
                elif mat2[i][j]=='2':
                    mat2[i-1][j]='3'
                    mat2[i][j]='0'
                     
            elif mat2[i-1][j]=='2':
                if mat2[i][j]!='1':
                    flag=False
                    #no change
                elif mat2[i][j]=='1':
                    mat2[i-1][j]='3'
                    mat2[i][j]='0'
                    
            else:
                if mat2[i][j]==mat2[i-1][j]:
                    mat2[i-1][j]=str(2*int(mat2[i-1][j]))
                    mat2[i][j]='0'
    return mat2

def R(mat):
    for i in range(n):
        for j in range(n-2,-1,-1):
            if  mat[i][j]!=0 and mat[i][j+1]=='0':
                mat[i][j+1]=mat[i][j]
                mat[i][j]='0'
                
            elif mat[i][j]=='1':
                if mat[i][j+1]!='2':
                    flag=False
                    #no change
                elif mat[i][j+1]=='2':
                    mat[i][j+1]='3'
                    mat[i][j]='0'
                
            elif mat[i][j]=='2':
                if mat[i][j+1]!='1':
                    flag=False
                    #no change
                elif mat[i][j+1]=='1':
                    mat[i][j+1]='3'
                    mat[i][j]='0'
            else:
                if mat[i][j+1]==mat[i][j]:
                    mat[i][j+1]=str(2*int(mat[i][j]))
                    mat[i][j]='0'
    return mat                
    
def l(mat):
    for i in range(n):
        for j in range(1,n):
            if  mat[i][j]!='0' and mat[i][j-1]=='0':
                mat[i][j-1]=mat[i][j]
                mat[i][j]='0'
                
            elif mat[i][j]=='1':
                if mat[i][j-1]!='2':
                    flag=False
                    #no change
                elif mat[i][j-1]=='2':
                    mat[i][j-1]='3'
                    mat[i][j]='0'
                
            elif mat[i][j]=='2':
                if mat[i][j-1]!='1':
                    flag=False
                    #no change
                elif mat[i][j-1]=='1':
                    mat[i][j-1]='3'
                    mat[i][j]='0'
            else:
                if mat[i][j-1]==mat[i][j]:
                    mat[i][j-1]=str(2*int(mat[i][j-1]))
                    mat[i][j]='0'
    return mat


def final(mat):
    flag=False
    matL=[j[:] for j in mat]
    matD=[j[:] for j in mat]
    matR=[j[:] for j in mat]
    matU=[j[:] for j in mat]
    if l(matL)==D(matD)==R(matR)==U(matU):
        flag=True#final ast
    return flag
 
def score(mat):
    score=0
    for i in range(n):
        for j in range(n):
            if mat[i][j]=='0' or mat[i][j]=='1' or mat[i][j]=='2':
                score+=0
            else:
                k=0
                A=int(mat[i][j])/3
                while  A>=2 :
                    k+=1
                    A=A/2
                score+=3**(k+1)
    return str(score)





countH=0
for h in harkat:
    #int(math[countH][0])
    #d=math[countH][1]
    test=False
    if h=='D':
        mat=D(mat)
        if matemp!=mat:
            #movement has been done
            m=0
            for j in range(n):
                if mat[0][j]=='0':
                    m+=1
            num0=0
            for e in range(n):
                if mat[0][e]=='0':
                    num0+=1
                    if num0==(int(math[countH][0])%m)+1:
                        mat[0][e]=math[countH][1]
            matemp=[j[:] for j in mat]
            countH+=1
            
    elif h=='U':
        mat=U(mat)
        if matemp!=mat:
            #movement has been done
            m=0
            for j in range(n):
                if mat[-1][j]=='0':
                    m+=1
            num0=0
            for e in range(n):
                if mat[-1][e]=='0':
                    num0+=1
                    if num0==(int(math[countH][0])%m)+1:
                        mat[-1][e]=math[countH][1]
            matemp=[j[:] for j in mat]
            countH+=1
    elif h=='R':
        mat=R(mat)
        if matemp!=mat:
            #movement has been done
            m=0
            for j in range(n):
                if mat[j][0]=='0':
                    m+=1
            num0=0
            for e in range(n):
                if mat[e][0]=='0':
                    num0+=1
                    if num0==(int(math[countH][0])%m)+1:
                        mat[e][0]=math[countH][1]
            matemp=[j[:] for j in mat]
            countH+=1
            
    elif h=='L':
        mat=l(mat)
        if matemp!=mat:
            #movement has been done 
            m=0
            for j in range(n):
                if mat[j][-1]=='0':
                    m+=1
            num0=0
            for e in range(n):
                if mat[e][-1]=='0':
                    num0+=1
                    if num0==(int(math[countH][0])%m)+1:
                        mat[e][-1]=math[countH][1]
            matemp=[j[:] for j in mat]
            countH+=1

for i in range(n):
    matFinal=''
    for j in range(n):
        matFinal+=mat[i][j]+'	'
    print(matFinal)
        
        
        
if final(mat):
    print('The final score is '+score(mat)+'.')
elif final(mat)==False:
    print('The partial score is '+score(mat)+'.')
    
    
    
    
