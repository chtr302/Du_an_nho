facebook_posts = eval(input())

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError as error:
        pass
print(total_likes)