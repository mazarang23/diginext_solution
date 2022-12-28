#!/usr/bin/env python
# coding: utf-8

# In[5]:


def question1 (string, length):
    new_string = (string * (int(length/len(string))+1))[:length];
    print(new_string)
    return new_string.count("a")

print(question1('abdaf',23))


# In[17]:


def question2 (str):
    counter = 0;
    for i in range(len(str)-1):
        if (str[i] == str[i+1]):
            counter+=1;
    return counter

print('AABAAB --> ' ,question2('AABAAB'))
print('AAAA --> ' ,question2('AAAA'))
print('BBBBB --> ' ,question2('BBBBB'))
print('ABABABAB --> ' ,question2('ABABABAB'))
print('BABABA --> ' ,question2('BABABA'))
print('AAABBB --> ' ,question2('AAABBB'))


# In[19]:


def question3 (arr):
    n = len(arr)
 
    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]
 
    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    arrpos.sort(key=lambda it: it[1])
 
    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k: False for k in range(n)}
 
    # Initialize result
    ans = 0
    for i in range(n):
 
        # already swapped or
        # already present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue
 
        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
 
        while not vis[j]:
 
            # mark node as visited
            vis[j] = True
 
            # move to next node
            j = arrpos[j][0]
            cycle_size += 1
 
        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
 
    return ans

arr = [7,1,3,2,4,5,6]
print(question3(arr))
 


# In[ ]:




