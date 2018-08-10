from django.db import models

class Post(models.Model):
    title           = models.CharField(max_length = 60)
    headerTitle     = models.CharField(max_length = 300)
    author          = models.CharField(max_length = 30)
    bannerURL       = models.ImageField(upload_to = 'blog/static/blog/images/banner_url')
    categories      = models.CharField(max_length = 60)
    content         = models.TextField()
    date            = models.DateTimeField()
    likes           = models.IntegerField(default = 0)
    comments        = models.IntegerField(default = 0)
    liked           = models.TextField(blank = True)

    def __str__(self):
        return self.title

    def get_short_title(self):
        return self.title[0:26]

    def get_categories(self):
        category = self.categories.split(',')
        return category

    def get_date(self):
        return self.date.strftime("%m %b %Y")

    def get_full_date(self):
        return self.date.strftime("%m %b %Y, %H:%M %p")

    def get_banner_url(self):
        new_url = self.bannerURL.url.replace('blog/s', 's')
        return new_url

    def get_liked(self):
        liked_ips = self.liked.split(',')
        return liked_ips

    def get_likes_count(self):
        return self.likes

    def get_comments_count(self):
        return self.comments

    def update_likes(self, value):
        self.likes += value
        return True

    def get_facebook_share(self):
        shareTitle = self.title.replace(' ', '%2520')
        return "https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fdeniszpop.co.uk%2Fpost%2F" + shareTitle

    def get_twitter_share(self):
        shareTitle = self.title.replace(' ', '%2520')
        return "https://twitter.com/intent/tweet?url=http%3A%2F%2Fdeniszpop.co.uk%2Fpost%2F" + shareTitle + "&text="

    def get_linkedin_share(self):
        shareTitle = self.title.replace(' ', '%2520')
        return "http://www.linkedin.com/shareArticle?mini=true&url=http%3A%2F%2Fdeniszpop.co.uk%2Fpost%2F" + shareTitle + "&title="

    def get_googlep_share(self):
        shareTitle = self.title.replace(' ', '%2520')
        return "https://plus.google.com/share?url=http%3A%2F%2Fdeniszpop.co.uk%2Fpost%2F" + shareTitle


class Comment(models.Model):
    post        = models.ForeignKey(Post, on_delete = models.CASCADE)
    username    = models.CharField(max_length = 30)
    email       = models.EmailField()
    message     = models.TextField()
    reply_id    = models.IntegerField()
    date        = models.DateTimeField()

    def __str__(self):
        return self.username

    def get_full_date(self):
        return self.date.strftime("%m %b %Y, %H:%M %p")
