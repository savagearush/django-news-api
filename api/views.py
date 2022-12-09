from django.shortcuts import render
from newsapi import NewsApiClient
from pprint import pprint
import json

newsapi = NewsApiClient(api_key='54cfea0ea35f427396412fbc67d107ac')


def getNews(topic):
    top_headlines = newsapi.get_top_headlines(q=topic, language="en")

    return top_headlines.get('articles', [])


def index(request):
    return render(request, "index.html", {"newsData": getNews("tech")})


def sendNews(request, category):
    return render(request, "index.html", {"newsData": getNews(category)})
