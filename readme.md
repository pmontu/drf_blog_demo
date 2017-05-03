blog
===

1. View Users

    curl -X GET \
      http://127.0.0.1:8000/api/users/

2. Create Post

    curl -X POST \
      http://127.0.0.1:8000/api/posts/ \
      -u 'username: password' \
      -H 'content-type: application/x-www-form-urlencoded' \
      -d 'title=post_title&text=post_body'

3. Create Comment

    curl -X POST \
      http://127.0.0.1:8000/api/comments/ \
      -u 'username: password' \
      -H 'content-type: application/x-www-form-urlencoded' \
      -d 'parent_post=http%3A%2F%2F127.0.0.1%3A8000%2Fapi%2Fposts%2F7%2F&text=comment_text'

parent_post is set to the url of the post to which the comment is added to. for example {"parent_post":"http://127.0.0.1:8000/api/posts/7/"}

4. View All Posts

    curl -X GET \
      'http://127.0.0.1:8000/api/posts/'

5. View Post Number #id with its Comments

    curl -X GET \
      'http://127.0.0.1:8000/api/posts/?author_id=9'

6. View Posts of Author with #id

    curl -X GET \
      'http://127.0.0.1:8000/api/posts/?author_id=2'


Setup Instructions
===========

    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py shell_plus
    User.objects.create_user("jhon", password="123")
    User.objects.create_user("adam", password="123")
    exit
    ./manage.py runserver
