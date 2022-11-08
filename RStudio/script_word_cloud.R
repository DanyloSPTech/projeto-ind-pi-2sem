library(tm)
library(wordcloud)
library(RColorBrewer)
library(wordcloud2)

palavras <- Corpus(VectorSource(words_scraper$Palavra))

dtm <- TermDocumentMatrix(palavras)
matrizPalavras <- as.matrix(dtm)
words <- sort(rowSums(matrizPalavras), decreasing = TRUE)

dfFreqPalavras <- data.frame(word = names(words), freq = words)

wordcloud2(data=dfFreqPalavras, size=0.7, color='random-light', backgroundColor = 'black', rotateRatio = 0, shape = 'circle')