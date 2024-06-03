class Author:
    def __init__(self, name):
        # Initialize Author object with a non-empty string name and an empty list of articles
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        # method for the name property
        return self._name

    def articles(self):
        # Method to return the list of articles authored by the author
        return self._articles

    def magazines(self):
        # Method to return the list of unique magazines the author has contributed to
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Method to add a new article authored by the author to a specified magazine
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        # Method to return the list of unique categories of magazines the author has contributed to
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    _magazines = []

    def __init__(self, name, category):
        # Initialize Magazine object with a name 
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._magazines.append(self)

    @property
    def name(self):
        #  method for the name property
        return self._name

    @name.setter
    def name(self, value):
        # Setter method for the name property
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        #  method for the category property
        return self._category

    @category.setter
    def category(self, value):
        # Setter method for the category property
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        # Method to return the list of articles in the magazine
        return self._articles

    def contributors(self):
        # Method to return the list of unique authors who have contributed to the magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # Method to return the list of titles of articles in the magazine
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # Method to return the list of authors who have contributed more than 2 articles to the magazine
        author_count = {}
        for article in self._articles:
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        # Class method to return the magazine with the most articles
        if not cls._magazines:
            return None
        return max(cls._magazines, key=lambda mag: len(mag.articles()))

class Article:
    all = []

    def __init__(self, author, magazine, title):
        # Initialize Article object with an author, a magazine, and a title
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.articles().append(self)
        Article.all.append(self)

    @property
    def title(self):
        #  method for the title property
        return self._title

    @property
    def author(self):
        #  method for the author property
        return self._author

    @author.setter
    def author(self, value):
        # Setter method for the author property
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        # method for the magazine property
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Setter method for the magazine property
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self._magazine = value
