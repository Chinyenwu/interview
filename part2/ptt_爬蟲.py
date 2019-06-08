import requests

def fetch(url):
    response = requests.get(url)
    response = requests.get(url, cookies={'over18': '1'}) 
    return response

from requests_html import HTML

def parse_article_entries(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.r-ent')
    return post_entries

def parse_article_entriesb(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.topbar')
    return post_entries

def parse_article_meta(entry):

    return {
        'date': entry.find('div.date', first=True).text,
        'author': entry.find('div.author', first=True).text,
        'title': entry.find('div.title', first=True).text,
        'push': entry.find('div.nrec', first=True).text,
		'link': "https://www.ptt.cc"+entry.find('div.title > a', first=True).attrs['href'],
    }

def parse_article_metab(entry):

    return {
        '看版': entry.find('a.board', first=True).text,
    }


url = 'https://www.ptt.cc/bbs/Baseball/index.html'
resp = fetch(url)  
post_entries = parse_article_entries(resp.text)  
post_entriesb = parse_article_entriesb(resp.text) 
for entry in post_entriesb:
    meta = parse_article_metab(entry)
    print(meta) 
for entry in post_entries:
    meta = parse_article_meta(entry)
    print(meta) 
	
