—ûK–â‘è5.1
—ûK–â‘è5.2
def countdown(n):
    if n == 0:
        print 'Blastoff'
    else:
        print n
        countdown(n-1)

def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n-1)
    
def do_n(f,n):
    if n<=0:
        return
    f()
    do_n(f,n-1)
    
def f():
    print "aaa"
 
print_n('Hello',2)   
#do_n(f,5)