#
sum_squares = 0
product_chain = 10

#sum_squares redefined outside the for loop
#therefore only adding the final square rather than summing over each result from the iteration
#should be redefined within the for loop instead
for i in range(10):
    i_sqaure = i**2
sum_squares += i_sqaure

#iteration over a range until 10
#range not defined to start at 1 rather than 0
#product is initially 10*0 = 0
#each subsequent product is then multiplying 0
#giving 0 as each result rather than the sum of each product
for i in range(10):
    print(product_chain)
    product_chain = product_chain*i
    print(product_chain)


print(sum_squares + product_chain)
