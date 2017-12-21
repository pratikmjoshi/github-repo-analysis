import requests
jsons=[]
"""
r = requests.get('https://api.github.com/search/repositories?q=machine+learning+language:java&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=neural+language:java&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=language:java&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=db+language:java&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=engine+language:c++&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=language:shell&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=android+language:java&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=video+language:javascript&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=ios+language:objective-c&sort=stars&order=desc')
jsons.append(r)
r = requests.get('https://api.github.com/search/repositories?q=vr+language:c++&sort=stars&order=desc')
jsons.append(r)
"""
r = requests.get("https://api.github.com/search/repositories?q=language:java&page=1&per_page=100", headers={'Accept': 'application/vnd.github.mercy-preview+json'})
print('got 100')
jsons.append(r)
r = requests.get("https://api.github.com/search/repositories?q=language:java&page=2&per_page=100", headers={'Accept': 'application/vnd.github.mercy-preview+json'})
print('got 200')
jsons.append(r)
r = requests.get("https://api.github.com/search/repositories?q=language:java&page=3&per_page=100", headers={'Accept': 'application/vnd.github.mercy-preview+json'})
print('got 300')
jsons.append(r)
r = requests.get("https://api.github.com/search/repositories?q=language:java&page=4&per_page=100", headers={'Accept': 'application/vnd.github.mercy-preview+json'})
print('got 400')
jsons.append(r)
r = requests.get("https://api.github.com/search/repositories?q=language:java&page=5&per_page=100", headers={'Accept': 'application/vnd.github.mercy-preview+json'})
print('got 500')
jsons.append(r)


import unicodedata
import csv

with open("urls.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for x in range(5):
        itemdict = jsons[x].json().get('items')
        for i in itemdict:
            row = []
            row.append(i['id'])#(unicodedata.normalize('NFKD',i.get('id')).encode('ascii','ignore'))
            row.append(unicodedata.normalize('NFKD',i.get('url')).encode('ascii','ignore'))
            row.append(unicodedata.normalize('NFKD',i.get('name')).encode('ascii','ignore'))
            full_name = unicodedata.normalize('NFKD',i.get('full_name')).encode('ascii','ignore')
            row.append(full_name[0:full_name.index('/')])
            row.append(i['has_wiki'])#(unicodedata.normalize('NFKD',i.get('has_wiki')).encode('ascii','ignore'))
            row.append(i['open_issues'])#(unicodedata.normalize('NFKD',i.get('open_issues')).encode('ascii','ignore'))
            row.append(i['stargazers_count'])#(unicodedata.normalize('NFKD',i.get('stargazers')).encode('ascii','ignore'))
            row.append(i['size'])#(unicodedata.normalize('NFKD',i.get('size')).encode('ascii','ignore'))
            row.append(i['forks'])#(unicodedata.normalize('NFKD',i.get('forks')).encode('ascii','ignore'))
            if i.get('description') != None:
                row.append(unicodedata.normalize('NFKD',i.get('description')).encode('ascii','ignore'))
            else:
                row.append("")
            top = i['topics']
            topics = ' '
            for j in top:
                topics += str(unicodedata.normalize('NFKD',j).encode('ascii','ignore'))
                topics += ' '
            row.append(topics.strip())#(unicodedata.normalize('NFKD',i.get('topics')).encode('ascii','ignore'))
            wr.writerow(row)

"""
final_url_lists=[]

for x in range(5):
    url_list=[unicodedata.normalize('NFKD',jsons[x].json().get('items')[i].get('url')).encode('ascii','ignore') for i in range(len(r.json().get('items')))]
    final_url_lists.append(url_list)


final_list=[]
for i in range(len(final_url_lists)):
    temp_list=final_url_lists[i]
    for j in range(len(temp_list)):
        final_list.append(temp_list[j])
final_list


with open("urls.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in range(5):
        wr.writerow(str(final_url_lists[i]))
"""
