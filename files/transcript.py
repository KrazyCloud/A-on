from youtube_transcript_api import YouTubeTranscriptApi

def transcript_generator(video_id):
    # Fetch the transcript for the video
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    # Convert the transcript into a readable format
    transcript_text = ''
    for transcript in transcript_list:
        transcript_text += transcript['text'] + ' '
    return transcript_text