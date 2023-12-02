def extract_video_id(url):
    if 'https://www.youtube.com/watch?v=' in url:
        video_id = url.split('youtube.com/watch?v=')[-1]
    else:
        video_id = None
    return video_id