############################
# Probability histogram 
# of binomial distribution 
############################

# Parameters of the distribution (feel free to modify)
n <- 100
p <- .25

# Possible values of Y ~ B(n,p)
y <- 0:n

## Corresponding probabilities 
## P(Y=y) = p(y) = C(n,y) * p^y * (1-p)^(n-y)
py <- dbinom(y,n,p)

## Visualize probability distribution of Y as bar plot
barplot(py, space=0) 
# set 'space = 0' is for no space between bars 
## Another visualization (vertical lines)
plot(y,py,type="h")


