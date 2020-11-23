data70 <- read.csv("00004628_s003_t000.csv", header = F)
data57 <- read.csv("00003051_s002_t002.csv", header = F)
data24 <- read.csv("24.csv", header = F)
data43 <- read.csv("00010146_s001_t000.csv", header = F)
data59 <- read.csv("00001320_s003_t000.csv", header = F)
data35 <- read.csv("35sui_00007830_s002_t000.csv", header = F)
data51 <- read.csv("51.csv", header = F)

colnames(data70) <- data70[2,]
n70 <- length(colnames(data70))

colnames(data57) <- data57[2,]
n57 <- length(colnames(data57))

colnames(data24) <- data24[2,]
n24 <- length(colnames(data24))

colnames(data43) <- data43[2,]
n43 <- length(colnames(data43))

colnames(data59) <- data59[2,]
n59 <- length(colnames(data59))

colnames(data35) <- data35[2,]
n35 <- length(colnames(data35))

colnames(data51) <- data51[2,]
n51 <- length(colnames(data51))


data70 <- data70[c(-1,-2),]
data57 <- data57[c(-1,-2),]
data24 <- data24[c(-1,-2),]
data43 <- data43[c(-1,-2),]
data59 <- data59[c(-1,-2),]
data35 <- data35[c(-1,-2),]
data51 <- data51[c(-1,-2),]




data[,1] <- as.numeric(data[,1])
data[,2] <- as.numeric(data[,2])
data[,1]
plot(data[,1], type = "l")
plot(data[,2], type = "l")
typeof(data[,3])
data[,5] <- as.numeric(data[,5])
is.na(data[,5])
View(data)




data70 <- na.omit(data70)
data57 <- na.omit(data57)
data24 <- na.omit(data24)
data43 <- na.omit(data43)
data59 <- na.omit(data59)
data35 <- na.omit(data35)
data51 <- na.omit(data51)

sd <- matrix(NA, nrow = 36, ncol = 7)
mean <- matrix(NA, nrow = 36, ncol = 7)
min <- matrix(NA, nrow = 36, ncol = 7)
max <- matrix(NA, nrow = 36, ncol = 7)

for (i in 1:n70) {
  data70[,i] <- as.numeric(data70[,i])
}

for (i in 1:n57) {
  data57[,i] <- as.numeric(data57[,i])
}

for (i in 1:n24) {
  data24[,i] <- as.numeric(data24[,i])
}

for (i in 1:n43) {
  data43[,i] <- as.numeric(data43[,i])
}

for (i in 1:n59) {
  data59[,i] <- as.numeric(data59[,i])
}

for (i in 1:n35) {
  data35[,i] <- as.numeric(data35[,i])
}

for (i in 1:n51) {
  data51[,i] <- as.numeric(data51[,i])
}


head(data)


for (i in 1:n70) {
  sd[i,1] <- sd(data70[,i])
  mean[i,1] <- mean(data70[,i])
  min[i,1] <- range(data70[,i])[1]
  max[i,1] <- range(data70[,1])[2]
}

for (i in 1:n59) {
  sd[i,2] <- sd(data59[,i])
  mean[i,2] <- mean(data59[,i])
  min[i,2] <- range(data59[,i])[1]
  max[i,2] <- range(data59[,1])[2]
}

for (i in 1:n57) {
  sd[i,3] <- sd(data57[,i])
  mean[i,3] <- mean(data57[,i])
  min[i,3] <- range(data57[,i])[1]
  max[i,3] <- range(data57[,1])[2]
}

for (i in 1:n51) {
  sd[i,4] <- sd(data51[,i])
  mean[i,4] <- mean(data51[,i])
  min[i,4] <- range(data51[,i])[1]
  max[i,4] <- range(data51[,1])[2]
}

for (i in 1:n43) {
  sd[i,5] <- sd(data43[,i])
  mean[i,5] <- mean(data43[,i])
  min[i,5] <- range(data43[,i])[1]
  max[i,5] <- range(data43[,1])[2]
}

for (i in 1:n35) {
  sd[i,6] <- sd(data35[,i])
  mean[i,6] <- mean(data35[,i])
  min[i,6] <- range(data35[,i])[1]
  max[i,6] <- range(data35[,1])[2]
}

for (i in 1:n24) {
  sd[i,7] <- sd(data24[,i])
  mean[i,7] <- mean(data24[,i])
  min[i,7] <- range(data24[,i])[1]
  max[i,7] <- range(data24[,1])[2]
}

options(scipen=999)

colnames(sd) <- c("70", "59", "57", "51", "43", "35", "24")
colnames(mean) <- c("70", "59", "57", "51", "43", "35", "24")
colnames(min) <- c("70", "59", "57", "51", "43", "35", "24")
colnames(max) <- c("70", "59", "57", "51", "43", "35", "24")

write.csv(sd, "sd.csv")
write.csv(mean, "mean.csv")
write.csv(min, "min.csv")
write.csv(max, "max.csv")

