from django.shortcuts import render, redirect
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from django.views.generic import DetailView, ListView
from bs4 import BeautifulSoup
import requests
from .models import *
import code




def fetch_top_news():
    try:
        url="https://kathmandupost.com"    
        r=requests.get(url)
        htmlContent=r.content
        soup=BeautifulSoup(htmlContent,'html.parser')

        news_topic=soup.find('article',class_='1')
        topic=news_topic.find('h2').text
        text = news_topic.find('p').text
        news_link= url + news_topic.find('figure').find('a').get('href')
       
        news_image= news_topic.find('figure').find('img').get('data-src')

        category_top_news=news_link.split('/')[3]
        category_exist=Category.objects.filter(category=category_top_news).exists()
        cat_object=None
        # code.interact(local = dict(globals(), **locals()))
        if category_exist:
            cat_object=Category.objects.get(category=category_top_news)
        else:
            cat_obj=Category(category=category_top_news)
            cat_obj.save()
            cat_object=cat_obj


        top_news=Data.objects.filter(
                                    headline=topic,
                                    url=news_link,
                                    text=text,
                                    image_link=news_image,
                                    ).exists()

        if not top_news:
            tn=Data(category=cat_object, headline=topic,url=news_link,text=text,image_link=news_image)
            tn.save()
        
        context={
            'news_topic':topic,
            'news_link': news_link,
            'news_image': news_image,
            'news_text':text,
        }

        return context

    except:
        context = {'error_message':"Failed to connect to server.Please check your connection"}
        return render(request,'index.html',context=context)



def index_view(request):
    try:
        url="https://kathmandupost.com"    
        r=requests.get(url)
        htmlContent=r.content
        soup=BeautifulSoup(htmlContent,'html.parser')

        user=request.user
        news_list=[]
        articles=soup.find('div',class_='col-xs-12 col-sm-6 col-md-4 grid-first divider-right order-2--sm').find_all('article')
        for article in articles:
            article_dict={}
            article_dict['heading']=article.find('h3').get_text()
            article_dict['link']=url + article.find('h3').find('a').get('href')
            article_dict['image']=article.find('div').find('figure').find('img').get('data-src')
            article_dict['discription']=article.find('p').get_text()
            news_list.append(article_dict)

            category=article_dict['link'].split('/')[3]
            category_exist=Category.objects.filter(category=category).exists()
            category_object=None
            if category_exist:
                category_object=Category.objects.get(category=category)
            else:
                cat_obj=Category(category=category)
                cat_obj.save()
                category_object=cat_obj

            news_exists=Data.objects.filter(
                                headline=article_dict['heading'],
                                url=article_dict['link'],
                                text=article_dict['discription'],
                                image_link=article_dict['image']
                                ).exists()
            if not news_exists:
                news=Data(category=category_object,
                            headline=article_dict['heading'],
                            url=article_dict['link'],
                            text=article_dict['discription'],
                            image_link=article_dict['image']
                            )
                news.save()

        top_news=fetch_top_news()

        context={
            'news_topic':top_news['news_topic'],
            'news_link': top_news['news_link'],
            'news_image': top_news['news_image'],
            'news_text': top_news['news_text'],

            'news_list':news_list,
            'logo':soup.find_all('img')[2].get('src'),
            'user':user,

            'channels':Category.objects.all()
        }

        return render(request,'index.html',context=context)

    except:
        context = {'error_message':"Failed to connect to server.Please check your connection. "}
        return render(request,'index.html',context=context)


def news_list(request):
    news_list=Data.objects.all()
    context={'news_list':news_list}
    return render(request,'web_scrap/news_list.html',context=context)

def topic_news(request,id):
    news_list=Data.objects.filter(category__id=id)
    context={
        'news_list':news_list,
    }
    return render(request,'web_scrap/news_list.html',context=context)
    

    # category=Category.objects.get(id=id)
    # category.user=request.user
    # category.suscribe=True
    # category.save()

    # return redirect("index")

