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


def get_transcript(url):
    video_id = get_video_id(url)

    api = YouTubeTranscriptApi()

    transcript = api.fetch(
        video_id,
        languages=["ko", "en", "en-US"]
    )

    return "\n".join(snippet.text for snippet in transcript)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("유튜브 링크: ")

    try:
        transcript = get_transcript(url)

        print("\n===== TRANSCRIPT =====\n")
        print(transcript)

    except Exception as e:
        print(f"자막을 가져오지 못했습니다: {e}")
