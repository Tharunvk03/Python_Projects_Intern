from decouple import config
from instapy import InstaPy
from instapy import smart_run

username = config("IGUSER")
password = config("PASSWORD")

session = InstaPy(username=username, 
            password=password)

with smart_run(session):
    session.login()

    session.set_do_follow(True,percentage=20)
   
    session.set_do_comment(True,percentage=20,comment_liked_photo=True)
  
    session.set_do_like(True,percentage=20)
  
    session.set_comments(["COOL @{},Keep the good work"])
  
    session.like_by_tags(['pythonmemes','collegelifememes'])
  
    session.end()