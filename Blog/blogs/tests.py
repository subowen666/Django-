from django.test import TestCase

# Create your tests here.
# 在这里编写你的测试用例

# 示例测试：
# class BlogPostTests(TestCase):
#     def test_blogpost_creation(self):
#         from django.contrib.auth.models import User
#         user = User.objects.create_user(username='testuser', password='testpass')
#         post = BlogPost.objects.create(
#             title="测试标题",
#             text="测试内容",
#             owner=user
#         )
#         self.assertEqual(post.title, "测试标题")