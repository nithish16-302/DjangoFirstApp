from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(requests):
    return render(requests,"wcount/home.html")
def about(requests):
    return render(requests,"wcount/about.html")
def count(requests):
    fulltext =requests.GET['text']
    wordcount=len(fulltext.split())
    words={}
    for w in fulltext.split():
        if w in words:
            words[w]+=1
        else:
            words[w]=1
    word_count_list=[(w,words[w]) for w in list(words.keys())]
    return render(requests,"wcount/count.html",{'fulltext':fulltext,'wordcount':wordcount,'wordslist':word_count_list})
