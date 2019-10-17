#binomail distribution of throwing a double 6 in two dice rolls

n <- 100
p <- .25
y <- 0:n
x <- 1 - dbinom(0, 24, (1/36))
Y <- function(p,n) n * p * (1-p)
curve(Y(x,100), from=0, to=1, xlab="p")