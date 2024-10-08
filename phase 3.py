#------------def---------------#
def L(mat):
    Mscore=[]
    for i in range(n):
        for j in range(1,n):
            if  mat[i][j]!='0' and mat[i][j-1]=='0':
                mat[i][j-1]=mat[i][j]
                mat[i][j]='0'
                Mscore+=[0]
                
            elif mat[i][j]=='1':
                if mat[i][j-1]!='2':
                    flag=False
                    Mscore+=[0]
                    #no change
                elif mat[i][j-1]=='2':
                    mat[i][j-1]='3'
                    mat[i][j]='0'
                    Mscore+=[3]
                
            elif mat[i][j]=='2':
                if mat[i][j-1]!='1':
                    flag=False
                    Mscore+=[0]
                    #no change
                elif mat[i][j-1]=='1':
                    mat[i][j-1]='3'
                    mat[i][j]='0'
                    Mscore+=[3]
            else:
                if mat[i][j-1]==mat[i][j]:
                    mat[i][j-1]=str(2*int(mat[i][j-1]))
                    mat[i][j]='0'
                    Mscore+=[int(mat[i][j-1])]

            
    max=0
    for b in Mscore:
       if b>max:
           max=b
    
    return mat,max

def D(mat1):
    Mscore=[]
    for i in range(n-2,-1,-1):
        for j in range(n):
            if  mat1[i][j]!='0' and mat1[i+1][j]=='0' :
                mat1[i+1][j]=mat1[i][j]
                mat1[i][j]='0'
                Mscore+=[0]
                
            elif mat1[i+1][j]=='1':
                if mat1[i][j]!='2':
                    flag=False
                    Mscore+=[0]
                    #no change
                elif mat1[i][j]=='2':
                    mat1[i+1][j]='3'
                    mat1[i][j]='0'
                    Mscore+=[3]
                     
            elif mat1[i+1][j]=='2':
                if mat1[i][j]!='1':
                    flag=False
                    Mscore+=[0]
                    #no change
                elif mat1[i][j]=='1':
                    mat1[i+1][j]='3'
                    mat1[i][j]='0'
                    Mscore+=[3]
                    
            else:
                if mat1[i+1][j]==mat1[i][j]:
                    mat1[i+1][j]=str(2*int(mat1[i][j]))
                    mat1[i][j]='0'
                    Mscore+=[int(mat1[i+1][j])]
    max=0
    for b in Mscore:
       if b>max:
           max=b
    
    return mat1,max

def R(mat):
    Mscore=[]
    for i in range(n):
        for j in range(n-2,-1,-1):
            if  mat[i][j]!=0 and mat[i][j+1]=='0':
                mat[i][j+1]=mat[i][j]
                mat[i][j]='0'
                Mscore+=[0]
                
            elif mat[i][j]=='1':
                if mat[i][j+1]!='2':
                    flag=False
                    Mscore+=[0]
                    #no change
                elif mat[i][j+1]=='2':
                    mat[i][j+1]='3'
                    mat[i][j]='0'
                    Mscore+=[3]
                
            elif mat[i][j]=='2':
                if mat[i][j+1]!='1':
                    flag=False
                    Mscore+=[0]
                    #no change
                elif mat[i][j+1]=='1':
                    mat[i][j+1]='3'
                    mat[i][j]='0'
                    Mscore+=[3]
            else:
                if mat[i][j+1]==mat[i][j]:
                    mat[i][j+1]=str(2*int(mat[i][j]))
                    mat[i][j]='0'
                    Mscore+=[int(mat[i][j])]
    max=0
    for b in Mscore:
       if b>max:
           max=b
    
    return mat,max              

def U(mat2):
    Mscore=[]
    for i in range(1,n):
        for j in range(n):
            if  mat2[i][j]!='0' and mat2[i-1][j]=='0' :
                mat2[i-1][j]=mat2[i][j]
                mat2[i][j]='0'
                Mscore+=[0]
                #break
                
            elif mat2[i-1][j]=='1':
                if mat2[i][j]!='2':
                    flag=False
                    Mscore+=[0]
                    #no change
                elif mat2[i][j]=='2':
                    mat2[i-1][j]='3'
                    mat2[i][j]='0'
                    Mscore+=[3]
                     
            elif mat2[i-1][j]=='2':
                if mat2[i][j]!='1':
                    flag=False
                    Mscore+=[0]
                    #no change
                elif mat2[i][j]=='1':
                    mat2[i-1][j]='3'
                    mat2[i][j]='0'
                    Mscore+=[3]
                    
            else:
                if mat2[i][j]==mat2[i-1][j]:
                    mat2[i-1][j]=str(2*int(mat2[i-1][j]))
                    mat2[i][j]='0'
                    Mscore+=[int(mat2[i-1][j])]
    
    max=0
    for b in Mscore:
       if b>max:
           max=b
    
    return mat2,max

#=========
def final(mat):
    flag=False
    matL=[j[:] for j in mat]
    matD=[j[:] for j in mat]
    matR=[j[:] for j in mat]
    matU=[j[:] for j in mat]
    if L(matL)==D(matD)==R(matR)==U(matU):
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
#-------------end def--------------#
def matMscore(mat):
    matL=[j[:] for j in mat]
    matD=[j[:] for j in mat]
    matR=[j[:] for j in mat]
    matU=[j[:] for j in mat]
    matemp=[j[:] for j in mat]
    maxscorelist=[L(matL)[1],D(matD)[1],R(matR)[1],U(matU)[1]]
    maxscore=0
    index=0
    for i in range(len(maxscorelist)):
        if maxscorelist[i]>maxscore:
            maxscore=maxscorelist[i]
            index=i
    move=''
    countH=0
    if index==0:
        matempf=[j[:] for j in matemp]
        matmove=L(matemp)[0]
        if matempf!=matmove:
            m=0
            for j in range(n):
                if matmove[j][-1]=='0':
                    m+=1
            num0=0
            for e in range(n):
                if matmove[e][-1]=='0':
                    num0+=1
                    if num0==(int(math[countH][0])%m)+1:
                        matmove[e][-1]=math[countH][1]
            matemp=[j[:] for j in matmove]
            countH+=1
        move+='L'
        
    elif index==1:
        matempf=[j[:] for j in matemp]
        matmove=D(matemp)[0]
        if matempf!=matmove:
            #m
            m=0
            for j in range(n):
                if matmove[0][j]=='0':
                    m+=1
            num0=0
            for e in range(n):
                if matmove[0][e]=='0':
                    num0+=1
                    if num0==(int(math[countH][0])%m)+1:
                        matmove[0][e]=math[countH][1]
            matemp=[j[:] for j in matmove]
            countH+=1
        move+='D'
    elif index==2:
        matempf=[j[:] for j in matemp]
        matmove=R(matemp)[0]
        if matempf!=matmove:
            #m
            m=0
            for j in range(n):
                if matmove[j][0]=='0':
                    m+=1
            num0=0
            for e in range(n):
                if matmove[e][0]=='0':
                    num0+=1
                    if num0==(int(math[countH][0])%m)+1:
                        matmove[e][0]=math[countH][1]
            matemp=[j[:] for j in matmove]
        countH+=1
        move+='R'
    elif index==3:
        matempf=[j[:] for j in matemp]
        matempf=[j[:] for j in matempi]
        matmove=U(matemp)[0]
        if matempf!=matmove:
            #m
            m=0
            for j in range(n):
                if matmove[-1][j]=='0':
                    m+=1
            num0=0
            for e in range(n):
                if matmove[-1][e]=='0':
                    num0+=1
                    if num0==(int(math[countH][0])%m)+1:
                        matmove[-1][e]=math[countH][1]
            matemp=[j[:] for j in matmove]
            countH+=1
        move+='U'
    
    return matmove,move


########## IN PUT ##########
n=int(input())
mat=[]
for i in range(n):
    m=input().split()
    mat+=[m]

numharkat=int(input())
math=[]
for w in range(numharkat):
    x=input().split()
    math+=[x]
#########output##########
move=''
q=0
for i in range(numharkat):
    move+=matMscore(mat)[1]
    mat=[j[:] for j in matMscore(mat)[0]]
print(move)

for i in range(n):
    matFinal=''
    for j in range(n):
        matFinal+= matMscore(mat)[0][i][j]+'	'
    print(matFinal)


if final(mat):
    print('The final score is '+score(mat)+'.')
elif final(mat)==False:
    print('The partial score is '+score(mat)+'.')
    
