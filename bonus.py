from bs4 import BeautifulSoup as bs
import pandas as pd

# with open('Личный кабинет - GamersBase Plus.htm', 'r', encoding='UTF-8') as htm:
#     with open('text.txt', '+a', encoding='UTF-8') as text:
#         for line in htm:
#             text.write(line)
tempArray = []
with open('text.txt', 'r', encoding='UTF-8') as text:
    for line in text:
        if '<div class="game-info--title"' in line:
            tempArray.append(line)
newTempArray = []
for item in tempArray:
    newTempArray.append(item[49:-29])
anoterArray = []
for item in newTempArray:
    anoterArray.append(item.split('">'))
with open('gamelist.txt', 'a+', encoding='UTF-8') as gl:
    for item in anoterArray:
        gl.write(item[0] + ' \n')