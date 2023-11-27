library(httr)
library(rtoot)
library(readr)
args = commandArgs(trailingOnly=TRUE)
instance <- args[1]
x <- auth_setup(instance=instance,browser=FALSE,type="public")
stream_timeline_public(timeout=9999,file_name=paste('mastodon_data/',gsub('\\.','-',instance),'_stream_',as.integer(Sys.time()),'.txt',sep=""),instance=instance,token=x,verbose=TRUE)
