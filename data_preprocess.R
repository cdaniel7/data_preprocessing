data<-read.csv(file='~/Data.csv')



// Replacing empty with mean
data$Age=ifelse(is.na(data$Age),ave(data$Age,FUN = function(x) mean(x,na.rm = TRUE)),data$Age)
data$Salary=ifelse(is.na(data$Salary),ave(data$Salary,FUN = function(x) mean(x,na.rm = TRUE)),data$Salary)

// Adding Factors 
data$Country=factor(data$Country,levels = c('France','Spain','Germany'),labels = c(1,2,3))

data$Purchased=factor(data$Purchased,levels = c('No','Yes'),labels = c(0,1))
