from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """博客文章模型"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'blog posts'
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_text_preview(self):
        """获取文章预览（前150字）"""
        if len(self.text) > 150:
            return f"{self.text[:150]}..."
        return self.text