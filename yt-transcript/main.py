from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import sys


def get_video_id(url):
    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")

    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(parsed.query).get("v", [None])[0]

    raise ValueError("유효한 YouTube URL이 아닙니다.")

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("유튜브 링크: ")

video_id = get_video_id(url)

api = YouTubeTranscriptApi()

try:
    transcript = api.fetch(video_id, languages=["ko", "en"])

    print("\n===== TRANSCRIPT =====\n")

    for snippet in transcript:
        print(snippet.text)

except Exception as e:
    print(f"자막을 가져오지 못했습니다: {e}")