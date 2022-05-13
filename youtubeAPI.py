from dotenv import load_dotenv

def 



def main():
	# load .env variables from local .env file (using .env and dotenv to not expose credentials and other key information)
	load_dotenv()

	# get .env variables from local .env file
	youtubeAPIKey = os.getenv("youtubeAPIKey") # youtube API Key
	return

if __name__ == '__main__':
	main()



For reference: https://developers.google.com/youtube/v3/getting-started#quota
Current URL: https://www.googleapis.com/youtube/v3/videos?part=id,statistics,contentDetails,snippet,recordingDetails,status,topicDetails&id=quCZe_N6tyQ&key=AIzaSyAKeZcVPgV-lZ6Xdq9HPbm1Wzv6SuDc_WY
Remove keys from part where needed to reduce latency, to only get information you need.
I only need: snippet (for thumbnail, description), content details(duration, caption maybe,, maybe content rating, status for maybe
	embeddeable, publicStatsvieawable (in case a video doesnt have that turned on) - a check), statistics. 
	topicdetails and recordingDetails are bonusses, may not be needed but seem useful to have - especially topicdetails.
	this contains all the info I need. 

{
  "kind": "youtube#videoListResponse",
  "etag": "y1ecB5GZ_b4bDVgwrU-e8ZAPTuQ",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "bb3BmwtoAmfq7Gb8Ksfgjxkmg4c",
      "id": "quCZe_N6tyQ",
      "snippet": {
        "publishedAt": "2021-08-31T04:20:20Z",
        "channelId": "UCSN8HjojRhNwXkpT9dK5ZZQ",
        "title": "test 133",
        "description": "13245",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/quCZe_N6tyQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/quCZe_N6tyQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/quCZe_N6tyQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/quCZe_N6tyQ/sddefault.jpg",
            "width": 640,
            "height": 480
          }
        },
        "channelTitle": "5hardul League",
        "categoryId": "22",
        "liveBroadcastContent": "none",
        "localized": {
          "title": "test 133",
          "description": "13245"
        }
      },
      "contentDetails": {
        "duration": "PT6S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "false",
        "licensedContent": false,
        "contentRating": {},
        "projection": "rectangular"
      },
      "status": {
        "uploadStatus": "processed",
        "privacyStatus": "public",
        "license": "youtube",
        "embeddable": true,
        "publicStatsViewable": true,
        "madeForKids": false
      },
      "statistics": {
        "viewCount": "3",
        "likeCount": "0",
        "dislikeCount": "0",
        "favoriteCount": "0",
        "commentCount": "0"
      },
      "topicDetails": {
        "topicCategories": [
          "https://en.wikipedia.org/wiki/Video_game_culture"
        ]
      },
      "recordingDetails": {}
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}