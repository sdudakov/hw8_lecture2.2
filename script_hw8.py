news_files={
      "newsafr.json": "utf-8",
      "newscy.json": "koi8-r",
      # "newsfr.json": "iso8859_5", #не разобрался какая у файла кодировка ?
      # "newsit.json": "cp1251",  #у этого файла немного другой формат 
}


import json

#название страны к которой относится новость
def news_country(file_name, code_page):
	with open(file_name, encoding=code_page) as file:
		data = json.load(file)
		country = data['rss']['channel']['title']
		return country

#из всех заголовков и новостей сделать один список news_list из слов длиннее 6 символов
def news_list(file_name, code_page):
	with open(file_name, encoding=code_page) as file:
		data = json.load(file)
		news_list_all = [] #создаю пустой список для всех слов новостей
		news_list = [] #создаю пустой список для слов более 6 символов
		for item in data['rss']['channel']['item']:
			title = item['title']['__cdata']
			description = item['description']['__cdata']
			title = title.split()
			description = description.split()
			news_list_all += title #на каждой итерации добавляю в список слова из title
			news_list_all += description #и description
			for _ in news_list_all:
				if len(_) > 6:
					news_list.append(_)
		return news_list
	
#создаем словарь из слов в котором подсчитаем сколько раз слово из списка встречается в этом списке
def analysis(news_list):
	words_count = {}
	for word in news_list:
		if word in words_count:
			words_count[word] += 1
		else:
			words_count[word] = 1
	return words_count


#сортируем словарь из слов, что бы первыми элементами были самые частовстречающиеся слова, печатаем 10 таких слов
def top_ten_words(words_count):
	words_sorted = sorted(words_count.items(),key=lambda x:x[1],reverse=True) #эту конструкцию подсмотрел в Интернете
	for _ in range(10):
		word, count = words_sorted[_]
		print(word)


#выводим название страны и топ 10 слов из новостей
def print_top_ten_words(news_files):
	for file in news_files:
		codepage = news_files[file]
		country = news_country(file, codepage)
		news = news_list(file, codepage)
		words_count = analysis(news)
		print("\n{}\nДесять наиболее часто встречающихся слов:" .format(country))
		top_ten_words(words_count)

print_top_ten_words(news_files)