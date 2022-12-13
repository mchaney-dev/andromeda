import textblob
import requests_cache
import random
from bs4 import BeautifulSoup

class Extractor:
    def __init__(self, urls: list, plaintext: list = []):
        self.urls = urls
        self.plaintext = plaintext
        self.text = []
        self.session = requests_cache.CachedSession('cache')
        self.results = []

    def extract(self, get_random=True):
        if self.plaintext != []:
            self.text.append(self.plaintext)
        for url in self.urls:
            response = self.session.get(url)
            if not get_random:
                self.text.append(response.text)
            else:
                soup = BeautifulSoup(response.text, 'html.parser')
                child_urls = []
                for item in soup.find_all('a'):
                    children = item.get('href')
                    child_urls.append(children)
                random_url = f'{url}/{str(random.choice(child_urls))}'
                response = self.session.get(random_url)
                self.text.append(response.text)
        for text in self.text:
            blob = textblob.TextBlob(text)
            for sentence in blob.sentences:
                sentence = str(sentence)
                sentence = sentence.replace('\n', ' ')
                sentence = sentence.replace('\r', ' ')
                sentence = sentence.replace('\t', ' ')
                sentence = sentence.replace('  ', ' ')
                sentence = sentence.replace('`', "'")
                sentence = sentence.replace('“', '"')
                sentence = sentence.replace('”', '"')
                sentence = sentence.replace("''", '"')
                sentence = sentence.strip()
                self.results.append(sentence)
        return self.results

class Dataset:
    def __init__(self, sentences: list):
        self.sentences = sentences
        self.data = []

    def clean(self):
        random.shuffle(self.sentences)
        for sentence in self.sentences:
            index = random.randint(0, len(sentence) - 1)
            before = sentence[:index]
            before = before.strip()
            after = sentence[index:]
            after = after.strip()
            self.data.append(f'INPUT: {before}\n')
            self.data.append(f'OUTPUT: {after}\n')

    def export(self, train_split=True, val_split=True):
        if train_split:
            self.data = self.data[:int(len(self.data) * 0.8)]
            with open('training.txt', 'w') as file:
                file.writelines(self.data)
            file.close()
        if val_split:
            self.data = self.data[int(len(self.data) * 0.8):]
            with open('validation.txt', 'w') as file:
                file.writelines(self.data)
            file.close()