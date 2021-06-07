from pytube import YouTube

class submit_link:
    def __init__(self, link):
        self.link = link
        self.link_ready = YouTube(self.link)

    def title_video(self):
        title = self.link_ready.title
        return title

    def view_video(self):
        view = self.link_ready.views
        return view

    def time_video(self):
        time = self.link_ready.length
        return time

    def download_video_lowest(self):
        download = self.link_ready.streams.get_lowest_resolution()
        download.download()

    def download_video_highest(self):
        download = self.link_ready.streams.get_highes_resolution()
        download.download()
    
   
        



# aa='https://www.youtube.com/watch?v=s50vvwTystA'

# submit=submit_link(aa)
# print(submit.title_video())


# link='https://www.youtube.com/watch?v=s50vvwTystA'
# y1=YouTube(link)

# print('title',y1.title)
#print('number of view: ',y1.views)
#print('len of video',y1.length)
#print('rating if video',y1.rating)
# print(y1.streams.filter(only_video=True))

# ys=y1.streams.get_lowest_resolution()
# ys.download()