earthquake_data <- read_csv("~/Documents/github-workspace/Data_Mining/R/earthquake_data.csv")

#plot eathquakes magnitude using a histogram
library(ggplot2)
ggplot(earthquake_data, aes(Magnitude)) + geom_histogram()

