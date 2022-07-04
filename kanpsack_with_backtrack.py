import copy
 
# for checking if the next node id promising or not
def promising(i, profit, weight):
    # to calculate the weight of the current set of items
    total_weight = 0
    # to calculate the maximum profit a brach can achieve
    bound = 0
    # if weight is greater than W, then it is not promising
    if weight> W:
        return False
    else:
        # to check next item
        j = i+1
        # initial the bound with current node profit
        bound = profit
        # initial the total weight with current node weight
        total_weight = weight
        # calculate the bound until it reach weight limit
        while j< N and total_weight + w[j] <= W:
            total_weight = total_weight + w[j]
            bound = bound + val[j]
            j += 1
        k = j
        if k< N:
            # calculate franctional knapsack if there is space left in the knapsack
            bound = bound + (W - total_weight) * val[k]/w[k]
        # return true if the bound is greater than the current maximum profit
        return bound > Maxprofit

# solve knapsack problem using backtrack
def knapsack(i, profit, weight):
    global Maxprofit, numbest, bestset, include

    if weight <= W and profit > Maxprofit:
        Maxprofit = profit
        # set numbest to the number of current item
        numbest = i
        # make a shallow copy of include set to not change with every change of include set
        bestset = copy.copy(include)

    # if the next item is promising check if it should be included or not
    if promising(i, profit, weight):
        # if we haven't reached the end of the list
        if i < N:
            # include the next item
            include[i + 1] = 1
            knapsack(i+1 , profit + val[i+1], weight + w[i+1])
            # exclude the next item
            include[i + 1] = 0
            knapsack(i+1, profit, weight)





if __name__ == "__main__":

    
    val = [0, 60,100,120]
    w = [0,10, 20,30]
    W = 50

    #number of items
    N = len(val)
    # an array to store the items to be included in the knapsack
    include = [0 for i in range(N)]
    # an array to store the final items to be included in the knapsack
    bestset = [0 for i in range(N)]
    # maximum profit
    Maxprofit= 0
    # number of the best node so far
    numbest = 0
    knapsack(0,0,0)
    print(f'the maximum profit is : {Maxprofit}')
    print('the best set is : [',end= ' ')
    
    for j in range(N):
        if bestset[j] == 1:
            print(j, end =' ')

    print(']')