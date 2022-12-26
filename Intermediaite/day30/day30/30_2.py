facebook_posts = [
    {'Likes': 21, "Comments": 2},
    {'Likes': 13, "Comments": 2, 'Shares': 1},
    {'Likes': 33, "Comments": 2, 'Shares': 3},
    {'Comments': 4, "Shares": 2},
    {'Comments': 1, "Shares": 1},
    {'Likes': 19, "Comments": 3},
]

total_comments= 0
total_likes = 0
total_shares = 0

for post in facebook_posts:
    try:
        total_comments = total_comments + post['Comments']
    except KeyError as key_err_msg:
        pass

    try:
        total_likes = total_likes + post['Likes']
    except:
        pass

    try:
        total_shares = total_shares + post['Shares']
    except:
        pass

print(f" Likes {total_likes}")
print(f" Comments {total_comments}")
print(f" Shares {total_shares}")
