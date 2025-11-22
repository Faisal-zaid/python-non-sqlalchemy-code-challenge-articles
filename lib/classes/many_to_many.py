class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise TypeError("name should be a string and longer than zero characters")

        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Author name should NOT change after initialization
        pass

    # Relationship methods
    def articles(self):
        return [article for article in Article.all if article.author == self] 

    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        unique = {mag.category for mag in self.magazines()}
        return list(unique) if unique else None



class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
     if isinstance(value, str) and (2 <= len(value) <= 16):
        self._name = value


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
       if isinstance(value, str) and len(value) > 0:
        self._category = value


    # Relationship methods
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})
    
    def article_titles(self):  # list of titles in the magazine 
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):  # infor for authors with more than 2 articles
        authors = [article.author for article in self.articles()]
        result = [articles for articles in set(authors) if authors.count(articles) > 2]
        return result if result else None

    # Bonus 
    @classmethod
    def top_publisher(cls): #return magazine with the most publisher
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))


class Article:
    all = []

    def __init__(self, author, magazine, title):

        # title validation
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise TypeError("title must be a string between 5 and 50 characters")

       
        self._title = title
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # title cannot change after initialization
        pass
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an Author instance")

        self._author = value

    # Magazine property 
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be a Magazine instance")
        self._magazine = value

