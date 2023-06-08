import json
from hot_scraper import scrape_games, scrape_hot_apps,scrape_hot_games,scrape_games_updates,scrape_apps_updates,scrape_games_new_release,scrape_apps_new_release,scrape_apps_treanding_search,scrape_games_treanding_search,scrape_games,scrape_apps,scrape_see_more

def save_file(path,data):
    with open(path,"w") as file:
        file.write(data)
        
def get_html_content(path):
    with open(path,'r',encoding="utf8") as html_file:
        return html_file.read()
    
def main():
    html=get_html_content('./index.html')
    hot_apps=scrape_hot_apps(html)
    hot_games=scrape_hot_games(html)
    games_updates=scrape_games_updates(html)
    apps_updates=scrape_apps_updates(html)
    games_new_release=scrape_games_new_release(html)
    apps_new_release=scrape_apps_new_release(html)
    apps_treanding_search=scrape_apps_treanding_search(html)
    games_treanding_search=scrape_games_treanding_search(html)
    games=scrape_games(html)
    apps=scrape_apps(html)
    see_more=scrape_see_more(html)
    
    
    save_file('./hot_apps.json',json.dumps(hot_apps))
    save_file('./hot_games.json',json.dumps(hot_games))
    save_file('./games_updates.json',json.dumps(games_updates))
    save_file('./apps_update.json',json.dumps(apps_updates))
    save_file('./games_new_release.json',json.dumps(games_new_release))
    save_file('./apps_new_release.json',json.dumps(apps_new_release))
    save_file('./apps_treanding_search.json',json.dumps(apps_treanding_search))
    save_file('./games_treanding_search.json',json.dumps(games_treanding_search))
    save_file('./games.json',json.dumps(games))
    save_file('./apps.json',json.dumps(apps))
    save_file('./see_more',json.dumps(see_more))

main()