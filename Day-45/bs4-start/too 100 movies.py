import requests
import lxml
from bs4 import BeautifulSoup

link = "https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(link)
content = res.text
soup = BeautifulSoup(content,"lxml")

#selector = "div.jsx-3821216435 listicle-item>*"
#selector ='div > h3 ~ div'
#found = soup.select(selector)
#movie = [x.text.split(";")[-1].strip() for x in found]
#fo#r x in movie:
#    print(x)

movie = soup.find(name="h3", class_="jsx-2692754980")
print(movie)