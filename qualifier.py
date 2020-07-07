"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    articles = []
    """The `Article` class you need to write for the qualifier."""
    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date= publication_date
        self._content = content
        self.last_edited = None
        self.id = len(self.articles)
        self.articles.append(self)

    def __repr__(self):
        return '<{} title="{}" '.format(type(self).__name__, self.title) + "author='{}' publication_date='{}'>".format(self.author, self.publication_date.isoformat())

    def __len__(self):
        return len(self.content)

    def short_introduction(self, n_characters: int):
        if self.content[n_characters].isspace() or self.content[n_characters] == '\n':
            return f"{self.content[:n_characters]}"
        else:
            for a in range(n_characters, 0, -1):
                if self.content[a].isspace() or self.content[a] == '\n':
                    return f"{self.content[:a]}"
                    break

    def most_common_words(self, n_words: int):
        words = {}
        temp = ''.join([i if i.isalpha() else ' ' for i in self.content])
        for word in temp.split():
            word = word.lower()
            if word in words:
                words[word] = words[word] + 1
            else:
                words[word] = 1
        return {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)[:n_words]}


fairytale = Article("Ayaya", "Ayaya", datetime.datetime(1837, 4, 7, 12, 15, 0), "Io sono Mungari Io faccio sono faccio sono sono faccio Mungari hentai")
print(repr(fairytale))
len(fairytale)
print(fairytale.short_introduction(4))
print(fairytale.most_common_words(3))