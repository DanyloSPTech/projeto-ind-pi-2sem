#!/usr/bin/env Rscript --vanilla

library(tm)
library(wordcloud2)

#install webshot
library(webshot)
webshot::install_phantomjs()

words_scraper <- read.csv("words_scraper.csv")

palavras <- Corpus(VectorSource(words_scraper$Palavra))

dtm <- TermDocumentMatrix(palavras)
matrizPalavras <- as.matrix(dtm)
words <- sort(rowSums(matrizPalavras), decreasing = TRUE)

dfFreqPalavras <- data.frame(word = names(words), freq = words)

plotWordCloud <- wordcloud2(data=dfFreqPalavras, size=1, color='random-light', backgroundColor = 'black', rotateRatio = 0, shape = 'circle')

## save it in html
library("htmlwidgets")
saveWidget(plotWordCloud,"CLOUD.html",selfcontained = F)
webshot("CLOUD.html","CLOUD_1.png", delay = 5)