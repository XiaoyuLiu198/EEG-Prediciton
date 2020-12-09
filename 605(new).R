rm(list=ls())

args = (commandArgs(trailingOnly=TRUE))
if(length(args) == 1){
  template = args
} else {
  cat('usage: Rscript myscript.R <template spectrum> \n', file=stderr())
  stop()
}


frequency_extract <- function(x,sample_frequency,sample_size){
  Fs=sample_frequency
  L=sample_size
  
  Y=fft(as.numeric(x))
  p=abs(Y)/L
  p=p[1:(L/2+1)]
  p[2:(L/2)]=2*p[2:(L/2)]
  f=Fs/L*c(0:(L/2))
  return(list(frequency_amplitude=p,frequency=f))
  
}


delta<-c(1,2,3)
theta<-c(4:7)
alpha<-c(8:13)
beta<-c(14:30)


power_calculate<-function(s,sample_size,delta=delta,theta=theta,alpha=alpha,beta=beta){
  x<-s$amp
  f<-s$freq
  x<-x^2/sample_size
  p_delta<-sum(x[f>=delta[1]&f<=delta[length(delta)]])
  p_theta<-sum(x[f>=theta[1]&f<=theta[length(theta)]])
  p_alpha<-sum(x[f>=alpha[1]&f<=alpha[length(alpha)]])
  p_beta<-sum(x[f>=beta[1]&f<=beta[length(beta)]])
  all<-p_delta+p_theta+p_alpha+p_beta
  #return(c(p_delta,p_theta,p_alpha,p_beta))
  return(c(p_delta,p_theta,p_alpha,p_beta)/all)
  
}

# f<-function(data){
#   q<-data[1:3]
#   delta<-sum(abs(q)^2)/length(q)
#   q<-data[4:7]
#   theta<-sum(abs(q)^2)/length(q)
#   q<-data[8:13]
#   alpha<-sum(abs(q)^2)/length(q)
#   q<-data[14:25]
#   beta<-sum(abs(q)^2)/length(q)
#   q<-data[26:30]
#   gamma<-sum(abs(q)^2)/length(q)
#   sum_data<-delta+theta+alpha+beta+gamma
#   weight<-rep(0,5)
#   qq<-c(delta, theta, alpha, beta, gamma)
#   for (i in 1:5){
#     weight[i]=qq[i]/sum_data
#   }
#   return(weight)
# }

info_s<-function(data){
 sum=0
   for (i in 1:length(data)){
    sum=sum-data[i]*log(data[i])
   }
 return(sum)
}

file_name<- paste0('./',template)
data<-read.csv(file_name,header = F)
age=data[1,1]
name<-data[2,]
name<-as.character(name)[1:length(name)]
name[1]<-strsplit(name[1],"# ")[[1]][2]
name<-c("age",name)
age=as.numeric(strsplit(age," ")[[1]][4])
data<-na.omit(data)
data<-data[3:dim(data)[1],]
kk<-dim(data)[2]
f_data<-list()
f_amplitude_data<-list()

for (i in 1:kk){
data_pre<-as.numeric(data[,i])
data_pre<-na.omit(data_pre)
p<-frequency_extract(data_pre,250,length(data_pre))
k<-list(amp=p$frequency_amplitude,freq=p$frequency)
f_amplitude_data[[i]]<-k

}



data_after<-lapply(f_amplitude_data,power_calculate,sample_size=dim(data)[1],delta=delta,theta=theta,alpha=alpha,beta=beta)
data_sum<-lapply(data_after,info_s)
for (i in 1:kk){
data_sum[[i]]<-c(data_sum[[i]],data_after[[i]])
}
final<-c(age,data_sum)
final<-as.list(final)
names(final)<-name
output<-paste("new_",template,sep="")
write.csv(final,file=output,row.names=F)
#sink(file = output)
#print(final)
#sink()
