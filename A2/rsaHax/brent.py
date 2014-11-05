from random import randint

def gcd(a,b):
    """ the euclidean algorithm """
    while a:
        a, b = b%a, a
    return b

def brent(N):
    if N%2==0:
            return 2
    y,c,m = randint(1, N-1),randint(1, N-1),randint(1, N-1)
    g,r,q = 1,1,1
    while g==1:            
        x = y
        for i in range(r):
                y = ((y*y)%N    +c)%N
        k = 0
        while (k<r and g==1):
            ys = y
            for i in range(min(m,r-k)):
                    y = ((y*y)%N+c)%N
                    q = q*(abs(x-y))%N
            g = gcd(q,N)
            k = k + m
        r = r*2
    if g==N:
        while True:
            ys = ((ys*ys)%N+c)%N
            g = gcd(abs(x-ys),N)
            if g>1:
                break
 
    return g

if __name__ == '__main__':
    factor = brent(127364267597139493540723331204339211194586014817451203830799795925196194691202462897905850883866904868892415046580817569176239367692303288839770474652109700848358432405752683726342528889678012214522325274056903064820951043366005591893083764579470069805619180603771671383915933692672583275832310594117217293261)
    print factor;