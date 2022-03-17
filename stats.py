def main():
        print('Please give 5 numbers to find the mean and mode of');
        n = list(map(int, input('Numbers: ').strip().split()))
        print('mode: ',mode(n))
        print('median: ',median(n))
        print('mean: ', mean(n))

def median(n):
        
        if(len(n)>0):
                
                n = sorted(n)
                
                if(len(n) % 2 == 0):
                        evenAMiddleIndex = int(len(n)/2)-1
                        evenBMiddleIndex = int(len(n)/2)
                        return (n[evenAMiddleIndex] + n[evenBMiddleIndex])/2
                else:
                        oddMiddleIndex = int(len(n)/2)
                        return n[oddMiddleIndex]
        else:
                return 0


def mode(n):
        if(len(n)>0):
            
                list2set = set(n)
                majority = 0
                mode = 0
               
                for i in list2set:
                        
                        if( n.count(i) > majority):
                                majority = n.count(i)
                                mode = i
                return mode
        
        else:
                return 0

def mean(n):


    if len(n) == 0:

        return 0

    total = 0

    for number in n:

        total += number

    return total / len(n)   



main()
