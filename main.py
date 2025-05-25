import requests
from db_manager import DB


def fetch_and_store():
    
    # Пользователи:
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()
    
    # for user in users:
    #     db_manager.add_user(user['id'], user['name'], user['username'], user['phone'])
    u = []
    for user in users:
        u.append({'id': user['id'],
                  'name': user['name'],
                  'username': user['username'],
                  'phone': user['phone'],
                  })
    db_manager.add_users(u)
        
    
    # Посты:
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = posts_response.json()
    
    for post in posts:
        db_manager.add_posts(post['id'], post['userId'], post['title'], post['body'])
    return
    # Комментарии:
    comments_response = requests.get('https://jsonplaceholder.typicode.com/comments')
    comments = comments_response.json()
    
    for comment in comments:
        cursor.execute('INSERT OR REPLACE INTO comments (postId, id, name, email, body) VALUES (?, ?, ?, ?, ?)',
                       (comment['postId'], comment['id'], comment['name'], comment['email'], comment['body']))
    
    # Альбомы:
    albums_response = requests.get('https://jsonplaceholder.typicode.com/albums')
    albums = albums_response.json()
    
    for album in albums:
        cursor.execute('INSERT OR REPLACE INTO albums (id, userId, title) VALUES (?, ?, ?)',
                       (album['id'], album['userId'], album['title']))
    
    # Фото:
    photos_response = requests.get('https://jsonplaceholder.typicode.com/photos')
    photos = photos_response.json()
    
    for photo in photos:
        cursor.execute('INSERT OR REPLACE INTO photos (albumId, id, title, url, thumbnailUrl) VALUES (?, ?, ?, ?, ?)',
                       (photo['albumId'], photo['id'], photo['title'], photo['url'], photo['thumbnailUrl']))
    




db_manager = DB('test.db')
db_manager.create_db()
fetch_store = fetch_and_store()
