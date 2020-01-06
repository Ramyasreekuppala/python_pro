s1=set([0,1,2,3,4])
print(s1)
s2=set([4,7,8,2,8,3,1])
print(s2)
s3=set(['190','string',98,'A'])
print(s3)
s4=set([])
print(s4)
print('built-in set functions')

#len(set)returns lenght of the set
print(len(s1))
print(len(s2))
print(len(s3))

#max(set) returns an item from the set with maximum value
print(max(s1))
print(max(s2))
#print(max(s3)) gives TypeError: '>' not supported between instances of 'int' and 'str'

#min(set) returns an item from the set with minimum value
print(min(s1))
print(min(s2))
#print(min(s3)) gives TypeError: '>' not supported between instances of 'int' and 'str'

#sum(set) returns sum of all the items in the set
print(sum(s1))
print(sum(s2))
#print(sum(s3)) gives TypeError: unsupported operand type(s) for +: 'int' and 'str'

#sorted(set) returns a set with a proper sort.
print(sorted(s1))
print(sorted(s2))
#print(sorted(s3)) gives TypeError: '<' not supported between instances of 'int' and 'str'

#enumerate(set) returns enumerate object.it contains the index and the value of all the items of set as a pair
print(enumerate(s1))
print(enumerate(s2))
print(enumerate(s3))

#any(set) returns true if the set contains at least one item,false otherwise
print(any(s1))
print(any(s2))
print(any(s3))
print(any(s4))

#all(set) returns true if all the elements are true or the set is empty
print(all(s1))
print(all(s2))
print(all(s3))
print(all(s4))

print('built-in set methods')

#set.add(obj) adds an element object to a set
s1.add(9)
print('set 1:',s1)
s2.add('ramya')
print('set 2:',s2)
s3.add(9.8680)
print('set 3:',s3)
s4.add('jdnksjnbkjdnkj')
print('set 4:',s4)

#set.remove(obj) removes an element object from the set
s1.remove(2)
print('set 1:',s1)
s2.remove('ramya')
print('set 2:',s2)
s3.remove('string')
print('set 3:',s3)
s4.remove('jdnksjnbkjdnkj')
print('set 4:',s4)

#set.discard(obj) removes an element object from the set.nothing happens if the element to be deleted is not in the set.
s1.discard(5)
print('set 1:',s1)
s2.discard('ramya')
print('set 2:',s2)
s3.discard('string')
print('set 3:',s3)
s4.discard('jdnksjnbkjdnkj')
print('set 4:',s4)

#set.pop() removes and returns an arbitary set element.raises key error if the set is empty.
s1.pop()
print('set 1:',s1)
s2.pop()
print('set 2:',s2)
s3.pop()
print('set 3:',s3)
#s4.pop()
#print('set 4:',s4) gives the error KeyError: 'pop from an empty set' 

#setA.union(setB) returns the union of two sets as a new set.
setA=s1.union(s2)
print('set A: ',setA)
setB=s2.union(s1)
print('set B: ',setB)

#setA.update(setB) updates a set with the union of itself and others.the result will be stored in the setA.
s1.update(s3)
print(s1)

#setA.intersection(setB) returns the intersection of two sets as a new set.
setx=s1.intersection(s3)
sety=s2.intersection(s3)
print('setx:',setx)
print('sety:',sety)

#set1.intersection_update() returns the updated set with the intersection of itself and another.the result will be stored in set1.
s1.intersection_update(s3)
s2.intersection_update(s3)
print('set 1:',s1)
print('set 2:',s2)
print('set 3:',s3)

#set1.symmetric_difference 




