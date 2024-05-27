class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            return TypeError("Author should be instance of Author")
        if not isinstance(magazine, Magazine):
            return TypeError("Magazine must be an instance of Magazine")
        if not isinstance(title, str):
            return TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            return ValueError("Title must be between 5 and 50 characters")
        if hasattr(self, '_title'):
            return AttributeError("Title cannot be changed once set")
        self.author = author
        self.magazine = magazine
        self.title = title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    def title(self):
        return self._title

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            return TypeError("Name should be a str")
        if len(name) == 0:
            return TypeError("Name characters must be longer than 0")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed once set")
        self._name = name
        self._articles =[]

    def name(self):
        return self._name

    def articles(self):
        return self._articles
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)
        return article
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        if not (2 <= len(name) <= 16):
            return ValueError("Name must be between 2 and 16 characters")
        if len(category) == 0:
            return ValueError("Category must be longer than 0 characters")
        self._name = name
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

author = Author("Carry Bradshaw")
    