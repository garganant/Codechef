test=int(input())
k=0
while k<test:
    N = int(input())
    semi = 0
    u = 2
    temp = 0
    temp1 = 0
    while u<N:
        v=N-u
        i = 2
        while i<u:
            j=2
            count=0
            count2=0
            if u%i==0 and u!=i*i:
                a=u/i
                while j<a:
                    if a%j==0:
                        count+=1
                    j+=1
                j=2
                while j<i:
                    if i%j==0:
                        count2+=1
                    j+=1
                if count == 0 and count2 == 0:
                    temp += 1
                    break
            i+=1
        while i < v:
            j = 2
            count = 0
            count2 = 0
            if v % i == 0 and v != i * i:
                a = v / i
                while j < a:
                    if a % j == 0:
                        count += 1
                    j += 1
                j = 2
                while j < i:
                    if i % j == 0:
                        count2 += 1
                    j += 1
                if count == 0 and count2 == 0:
                    temp1 += 1
                    break
            i+=1
        if temp > 0 and temp1 > 0:
            semi+=1
            break
        else:
            temp=0
            temp1=0
        u+=1
    if semi == 1:
        print('YES')
    else:
        print('NO')
    k+=1