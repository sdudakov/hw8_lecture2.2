news_files={
      "newsafr.json": "utf-8",
      "newscy.json": "koi8-r",
      # "newsfr.json": "iso8859_5", ? 
      # "newsit.json": "cp1251"
}


import json

#название страны к которой относится новость
def news_country(file_name, code_page):
	with open(file_name, encoding=code_page) as file:
		data = json.load(file)
		return data['rss']['channel']['title']

#из всех заголовков и новостей сделать один список news_list_6char из слов длиннее 6 символов
def news_list(file_name, code_page):
	with open(file_name, encoding=code_page) as file:
		data = json.load(file)
		news_list_all = [] #создаю пустой список для всех слов новостей
		news_list_6char = [] #создаю пустой список для слов более 6 символов
		for item in data['rss']['channel']['item']:
			title = item['title']['__cdata']
			description = item['description']['__cdata']
			title = title.split()
			description = description.split()
			news_list_all += title #на каждой итерации добавляю в список слова из title
			news_list_all += description #и description
			for _ in news_list_all:
				if len(_) > 6:
					news_list_6char.append(_)
		return news_list_6char
	
#создаем словарь из слов в котором подсчитаем сколько раз слово из списка встречается в этом списке
def analysis(news_list):
	words_count = {}
	for word in news_list:
		if word in words_count:
			words_count[word] += 1
		else:
			words_count[word] = 1
	return words_count

#print(news_country("newsafr.json", "utf-8"))
words_count = analysis(news_list("newsafr.json", "utf-8"))
#print(news_set(news_list("newsafr.json", "utf-8")))
words_sorted = sorted(words_count.items(),key=lambda x:x[1],reverse=True) #эту конструкцию подсмотрел в Интернете

print(words_sorted)
