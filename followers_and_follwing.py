import json

# Load the following.json file and extract usernames
with open('following.json', 'r') as f:
    following_data = json.load(f)
    # Assuming structure: {"relationships_following": [{"title": "username"}, ...]}
    following = set(item['title'] for item in following_data['relationships_following'])

# Load the followers_1.json file and extract usernames
with open('followers_1.json', 'r') as f:
    followers_data = json.load(f)
    # Assuming structure: [{"string_list_data": [{"value": "username", ...}]}, ...]
    followers = set(item['string_list_data'][0]['value'] for item in followers_data)

# People you follow but who don't follow you back
not_following_back = following - followers

# People who follow you but you don't follow back (vice versa)
you_dont_follow_back = followers - following

# Mutual follows (optional, for reference)
mutual = following & followers

# Print the results
print("You follow but they don't follow back ({} accounts):".format(len(not_following_back)))
for user in sorted(not_following_back):
    print(user)

print("\nThey follow you but you don't follow back ({} accounts):".format(len(you_dont_follow_back)))
for user in sorted(you_dont_follow_back):
    print(user)

# Optional: Print mutual follows
# print("\nMutual follows ({} accounts):".format(len(mutual)))
# for user in sorted(mutual):
#     print(user)