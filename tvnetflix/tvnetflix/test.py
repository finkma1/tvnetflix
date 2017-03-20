from models import Video
v = Video(name='Humans Are Awesome',
          url = "https://www.youtube.com/embed/videoseries?list=PLUJnnrQ11_kAP-8Qm4c6mUb4LGuByQ3D4",
          cat1 = "action sports",
          cat1_score = 5)

v.save()
