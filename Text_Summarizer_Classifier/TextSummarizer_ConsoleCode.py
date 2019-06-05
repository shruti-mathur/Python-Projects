Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.tokenize import word_tokenize, sent_tokenize
>>> from nltk.corpus import stopwords
>>> from nltk.stem import WordNetLemmatizer, PorterStemmer
>>> text = """
I’ve been asked by a few friends to develop a feature for a
WhatsApp chatbot of mine, that summarizes articles based on
URL inputs. So when a friend sends an article to a WhatsApp
group, the bot will reply with a summary of the given URL
article. I like this feature because from my personal
research, 65% of group users don’t even click the shared URLs,
but 97% of them will read a few lines of the articles summary.
As part of being a Fullstack developer, it is important to
know how to choose the right stack for each product you
develop, depending on the requirements and limitations.
For web crawling, I love using Python. The Python community
is filled with efficient, easy to implement open source
libraries both for web crawling and text summarization.
Once you’re done with this tutorial, you won’t believe how
simple it is to implement the task.
"""
>>> words = word_tokenize(text)
>>> sentences = sent_tokenize(text)
>>> stopwords = set(stopwords.words("english"))
>>> w_net = WordNetLemmatizer()
>>> freq_table = dict()
>>> for word in words:
	word = word.lower()
	if word in stopwords:
		continue
	word = w_net.lemmatize(word, pos ='v')
	if word in freq_table:
		freq_table[word] += 1
	else:
		freq_table[word] = 1

		
>>> print(freq_table)
{'’': 4, 'ask': 1, 'friends': 1, 'develop': 2, 'feature': 2, 'whatsapp': 2, 'chatbot': 1, 'mine': 1, ',': 9, 'summarize': 1, 'article': 4, 'base': 1, 'url': 2, 'input': 1, '.': 7, 'friend': 1, 'send': 1, 'group': 2, 'bot': 1, 'reply': 1, 'summary': 2, 'give': 1, 'like': 1, 'personal': 1, 'research': 1, '65': 1, '%': 2, 'users': 1, 'even': 1, 'click': 1, 'share': 1, 'urls': 1, '97': 1, 'read': 1, 'line': 1, 'part': 1, 'fullstack': 1, 'developer': 1, 'important': 1, 'know': 1, 'choose': 1, 'right': 1, 'stack': 1, 'product': 1, 'depend': 1, 'requirements': 1, 'limitations': 1, 'web': 2, 'crawl': 2, 'love': 1, 'use': 1, 'python': 2, 'community': 1, 'fill': 1, 'efficient': 1, 'easy': 1, 'implement': 2, 'open': 1, 'source': 1, 'libraries': 1, 'text': 1, 'summarization': 1, 'do': 1, 'tutorial': 1, 'believe': 1, 'simple': 1, 'task': 1}
>>> sent_table = dict()
>>> for sentence in sentences:
	for word, freq_table.items():
		
SyntaxError: invalid syntax
>>> for sentence in sentences:
	for word, freq in freq_table.items():
		if word in sentence:
			if sentence in sent_table:
				sent_table[sentence] += freq
			else:
				sent_table[sentence] = freq

				
>>> print(sent_table)
{'\nI’ve been asked by a few friends to develop a feature for a\nWhatsApp chatbot of mine, that summarizes articles based on\nURL inputs.': 37, 'So when a friend sends an article to a WhatsApp\ngroup, the bot will reply with a summary of the given URL\narticle.': 29, 'I like this feature because from my personal\nresearch, 65% of group users don’t even click the shared URLs,\nbut 97% of them will read a few lines of the articles summary.': 45, 'As part of being a Fullstack developer, it is important to\nknow how to choose the right stack for each product you\ndevelop, depending on the requirements and limitations.': 29, 'For web crawling, I love using Python.': 21, 'The Python community\nis filled with efficient, easy to implement open source\nlibraries both for web crawling and text summarization.': 32, 'Once you’re done with this tutorial, you won’t believe how\nsimple it is to implement the task.': 28}
>>> summary = ""
>>> for sentence in sentences:
	if sent_table[sentence] > 30 and sentence in sent_table:
		summary += sentence

		
>>> print(summary)

I’ve been asked by a few friends to develop a feature for a
WhatsApp chatbot of mine, that summarizes articles based on
URL inputs.I like this feature because from my personal
research, 65% of group users don’t even click the shared URLs,
but 97% of them will read a few lines of the articles summary.The Python community
is filled with efficient, easy to implement open source
libraries both for web crawling and text summarization.
>>> 
