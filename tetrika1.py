def search_pairs(array,k):
    answer = []
    for i in range(len(array)) :
        if array[i] < k :
            if array[i:].count(k-array[i]) > 0:
                if  not ((array[i],k-array[i]) in answer or (k-array[i],array[i]) in answer) :
                    answer.append((array[i],k-array[i]))
    return answer

print(search_pairs([1,2,6,5,3,4,7,8,3,2],5))
