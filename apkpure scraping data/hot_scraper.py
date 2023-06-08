from bs4 import BeautifulSoup

def scrape_hot(soup):
    hot_items=[]
    for item in soup.find_all('a'):
        title=item["title"]
        link=item["href"]
        image_link=item.figure.img["src"]
        hot_items.append({
            "title":title,
            "link":link,
            "image_link":image_link
        })
    return hot_items

def treanding_search(soup):
    hot_items=[]
    for item in soup.find_all('a'):
        title=item["title"]
        link=item["href"]
        image_link=item.img["src"]
        hot_items.append({
            "title":title,
            "link":link,
            "image_link":image_link
        })
    return hot_items

def categorys(soup):
    games=[]
    for item in soup.findAll('a'):
        title = item.getText()
        link =item["href"]
        games.append({
             "title":title,
             "link":link,
            })
    return games


def scrape_games(html):
    soup=BeautifulSoup(html,'html.parser')
    games=soup.findAll("ul",{'class':"index-category"})[0]
    return categorys(games)

def scrape_apps(html):
    soup=BeautifulSoup(html,'html.parser')
    apps=soup.findAll("ul",{'class':"index-category"})[1]
    return categorys(apps)
   
      
def scrape_hot_games(html):
    soup=BeautifulSoup(html,'html.parser')
    hot_games_html=soup.findAll("div",{'class':"content-apps"})[0]
    return scrape_hot(hot_games_html)

def scrape_hot_apps(html):
    soup=BeautifulSoup(html,'html.parser')
    apps_hots_html=soup.findAll("div",{'class':"content-apps"})[1]
    return scrape_hot(apps_hots_html)

def scrape_games_updates(html):
    soup=BeautifulSoup(html,'html.parser')
    games_updates_html=soup.findAll("div",{'class':"content-apps"})[2]
    return scrape_hot(games_updates_html)

def scrape_apps_updates(html):
    soup=BeautifulSoup(html,'html.parser')
    apps_updates_html=soup.findAll("div",{'class':"content-apps"})[3]
    return scrape_hot(apps_updates_html)

def scrape_games_new_release(html):
    soup=BeautifulSoup(html,'html.parser')
    games_new_release_html=soup.findAll("div",{'class':"content-apps"})[4]
    return scrape_hot(games_new_release_html)

def scrape_apps_new_release(html):
    soup=BeautifulSoup(html,'html.parser')
    apps_new_release_html=soup.findAll("div",{'class':"content-apps"})[5]
    return scrape_hot(apps_new_release_html)

def scrape_apps_treanding_search(html):
    soup=BeautifulSoup(html,'html.parser')
    apps_treanding_search=soup.findAll("div",{'class':"content"})[7]
    return treanding_search(apps_treanding_search)

def scrape_games_treanding_search(html):
    soup=BeautifulSoup(html,'html.parser')
    games_treanding_search=soup.findAll("div",{'class':"content"})[8]
    return treanding_search(games_treanding_search)

#for see_more section
def scrape_see_more(html):
    soup=BeautifulSoup(html,'html.parser')
    see_more=soup.findAll("div",{'class':"content-apps"})[0]
    return scrape_hot(see_more)