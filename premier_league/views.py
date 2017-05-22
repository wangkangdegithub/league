from django.shortcuts import render
from .import models
import pandas as pd
from numpy import *
from sklearn.linear_model import LogisticRegression

def premier(request):
    articles = models.test.objects.all()
    return render(request, 'premier.html', {'articles': articles})

def article_page(request, article_id):
    article = models.test.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})

def edit_page(request):
    return render(request,'edit_page.html')

def edit_action(request):
    title=request.POST.get('title','TITLE')
    content=request.POST.get('content','CONTENT')
    models.test.objects.create(title=title,content=content)
    #pk = models.Article.objects.order_by('-id').first().id  # 获取最新的主键ID
    #articles=models.Article.objects.get(pk=pk)
    articles = models.test.objects.all()
    return render(request, 'prediction.html',{'articles': articles})

def prediction(request):
    articles = models.test.objects.all()
    home=request.POST.get('home','支持球队')
    away=request.POST.get('away','对阵球队')
    models.Premier.objects.create(home=home,away=away)
    pk=models.Premier.objects.order_by('-id').first().id  #获取最新的主键ID
    nn = models.Premier.objects.get(pk=pk)
    x=nn.home
    y=nn.away
    context= {'home':x,
              'result':Input_team(x,y),
              'away':y,
              'articles':articles,
              'avg_train':avg_train(x,y),
              }
    return render(request, 'prediction.html', context)


def Input_team(x,y):
    new_df = pd.read_csv('C:/Users/Bohemian/Desktop/new_df.csv')
    new_train = new_df.drop(['referee', 'away_goals', 'home_goals'], axis=1)
    col_all = new_train.columns
    col = [c for c in col_all if c not in ['test', 'home_team', 'away_home']]
    col_home = [c for c in col_all if c not in ['away_home', 'referee', 'test', 'assists_away_team', 'blocks_away_team',
                                                'clearances_away_team', 'corners_away_team', 'crosses_away_team',
                                                'fouls_away_team', 'free_kicks_away_team', 'handballs_away_team',
                                                'offsides_away_team', 'penalties_away_team', 'red_cards_away_team',
                                                'saves_away_team', 'shots_on_target_away_team', 'total_shots_away_team',
                                                'yellow_cards_away_team']]
    col_away = [c for c in col_all if c not in col_home]
    col_away.remove('test')
    target = ['test']
    new_train_home = new_train[col_home]
    new_train_away = new_train[col_away]
    new_train_home.loc[:, 'home_team'] == x
    avg_home=new_train_home.loc[(new_train_home.loc[:,'home_team']==x),col].mean()
    new_train_away.loc[:, 'away_home'] == y
    avg_away=new_train_away.loc[(new_train_away.loc[:,'away_home']==y),col].mean()
    avg_home_are_NaNs = isnan(avg_home)
    avg_home[avg_home_are_NaNs] = 0
    avg_away_are_NaNs = isnan(avg_away)
    avg_away[avg_away_are_NaNs]= 0
    avg_train = avg_home+avg_away
    X_train_data = new_train[col].as_matrix()
    y_train_target = new_train[target].as_matrix()
    clf = LogisticRegression()
    clf.fit(X_train_data, y_train_target)
    prediction = clf.predict(avg_train )
    if prediction == 1:
        return '胜'
    else: return '平/负'

def avg_train(x,y):
    new_df = pd.read_csv('C:/Users/Bohemian/Desktop/new_df.csv')
    new_train = new_df.drop(['referee', 'away_goals', 'home_goals'], axis=1)
    col_all = new_train.columns
    col = [c for c in col_all if c not in ['test', 'home_team', 'away_home']]
    col_home = [c for c in col_all if c not in ['away_home', 'referee', 'test', 'assists_away_team', 'blocks_away_team',
                                                'clearances_away_team', 'corners_away_team', 'crosses_away_team',
                                                'fouls_away_team', 'free_kicks_away_team', 'handballs_away_team',
                                                'offsides_away_team', 'penalties_away_team', 'red_cards_away_team',
                                                'saves_away_team', 'shots_on_target_away_team', 'total_shots_away_team',
                                                'yellow_cards_away_team']]
    col_away = [c for c in col_all if c not in col_home]
    col_away.remove('test')
    target = ['test']
    new_train_home = new_train[col_home]
    new_train_away = new_train[col_away]
    new_train_home.loc[:, 'home_team'] == x
    avg_home = new_train_home.loc[(new_train_home.loc[:, 'home_team'] == x), col].mean()
    new_train_away.loc[:, 'away_home'] == y
    avg_away = new_train_away.loc[(new_train_away.loc[:, 'away_home'] == y), col].mean()
    avg_home_are_NaNs = isnan(avg_home)
    avg_home[avg_home_are_NaNs] = 0
    avg_away_are_NaNs = isnan(avg_away)
    avg_away[avg_away_are_NaNs] = 0
    avg_train = avg_home + avg_away
    return  avg_train









