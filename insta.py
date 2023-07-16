from instaloader import Instaloader, Profile 
L = Instaloader()

def download(PROFILE,num):
    profile = Profile.from_username(L.context, PROFILE)
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)
    selected_range = posts_sorted_by_likes[0:num]
    for post in selected_range:
        L.download_post(post, PROFILE)




PROFILE = input("profile name:") #get profile name
# num     = int(input("how much post you wan't: ")) #get post count
if PROFILE =="":
    print('Please enter a valid username')
elif PROFILE==" ":
    print ('hey idiot, enter any username') 
else :
    num = int(input("how much post you wan't: ")) #get post count
    if num == 0:
        print("please enter a number abow 0")
    elif num == '':
        print("please enter any number")
    else:
        download(PROFILE,num)






