from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    # Assuming limited user types like 'Student', 'Faculty', etc.
    user_type = models.CharField(max_length=20)


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)


class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword_text = models.CharField(max_length=50)


class Research(models.Model):
    research_id = models.AutoField(primary_key=True)
    research_date = models.DateField()
    search_query = models.TextField()


class ResearchBook(models.Model):
    research_book_id = models.AutoField(primary_key=True)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class BookKeyword(models.Model):
    book_keyword_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)


class Conducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)


class Consults(models.Model):
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class AssociatesWith(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
