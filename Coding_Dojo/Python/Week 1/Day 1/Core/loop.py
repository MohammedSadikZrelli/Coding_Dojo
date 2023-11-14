# Basic - Print all integers from 0 to 150.


for i in range (0,159,1):
    print(i)


#Multiples of Five - Print all the multiples of 5 from 5 to 1,000


for index in range (5,1001,1):
    if (index%5==0):
        print(index)




#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for codo in range(1, 101, 1):
    if codo % 10 == 0:
        print("Coding Dojo")
    elif codo % 5 == 0:
        print("Coding")
    else:
        print(codo)



# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.


sum=0
for x in range(0,500001):
    sum+=x
print(sum)





# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.


for j in range (2018,0,-4):
    print(j)




# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=2
highNum=9
mult=3


for i in range (lowNum,highNum+1):
    if i%mult==0 :
        print(i)