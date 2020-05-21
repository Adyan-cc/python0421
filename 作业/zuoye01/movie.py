

import requests,json
url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
ret = requests.get(headers=headers,url=url).content.decode("utf-8")
movie_dict = json.loads(ret)