class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author_param):
        if(isinstance(author_param, Author)):
            self._author = author_param

    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine_param):
        if(isinstance(magazine_param, Magazine)):
            self._magazine = magazine_param

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title_param):
        if(not hasattr(self, 'title')) and (isinstance(title_param, str)) and ( 5 <= len(title_param) <= 50):
            self._title = title_param
        
class Author:

    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_param):
        if(not hasattr(self, 'name')) and (isinstance(name_param, str)) and (len(name_param) > 0):
            self._name = name_param

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))
        # return list(set([article.magazine for article in self.articles()])) {This is the shorter way to solve this problem, it calls the articles() function and returns the information that the ( Article.all if article.author == self ) provides.}
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title) 
            # This function takes in the parameters that it wants to pass in order to create a new Article instance, We have to pass the same amount of arguments as the __init__ function for the Article class, otherwise it won't allow us to create the new article object. The reason why the author parameter is not passed here is because the self IS the author since we're creating this function inside the Author class. That's why it looks like we're missing a parameter but in all actuality all parameters are there.    

    def topic_areas(self):
        if(len(self.articles()) == 0):
            return None
        else:
            return [magazine.category for magazine in self.magazines()]
        # Here we're checking the contents of the result from the articles() function. The self.articles() is referencing the Author instance. The reason why we don't use Author here is because we need to access the articles written by the author that are bieng stored in the Article.all list. If this returns false or 0 the we return None. However, if this returns true then we return the category for the magazine stored in the Article.all list.
        
        

class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_param):
        if(isinstance(name_param, str)) and ( 2 <= len(name_param) <= 16):
            self._name = name_param

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category_param):
        if(isinstance(category_param, str)) and (len(category_param) > 0):
            self._category = category_param

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))
       
    def article_titles(self):
        if(len(self.articles()) == 0):
            return None
        else:
            return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors_list = [author for author in self.contributors() if len([article for article in author.articles() if article.magazine is self]) > 2]
        if(len(authors_list) == 0):
            return None
        else:
            return authors_list