from flask import Blueprint, render_template

views = Blueprint('views', __name__)

videos = [
  {
    "kind": "youtube#searchResult",
    "etag": "aDoRS8LTUtUSYVG9AFZ-O0I3vMc",
    "id": {
      "kind": "youtube#video",
      "videoId": "aI-vHFfGwM8"
    },
    "snippet": {
      "publishedAt": "2019-08-26T14:58:45Z",
      "channelId": "UC3kbAe8BguiZFnsVYY1oW0w",
      "title": "The PERFECT LEG Workout || To Build Strength &amp; Power",
      "description": "LEGDAY #Bodybuilder #Workout Download the fitness culture app below \u200d♂️ ----------------- ▷Fitness Culture Programming: ...",
      "thumbnails": {
        "default": {
          "url": "https://i.ytimg.com/vi/aI-vHFfGwM8/default.jpg",
          "width": 120,
          "height": 90
        },
        "medium": {
          "url": "https://i.ytimg.com/vi/aI-vHFfGwM8/mqdefault.jpg",
          "width": 320,
          "height": 180
        },
        "high": {
          "url": "https://i.ytimg.com/vi/aI-vHFfGwM8/hqdefault.jpg",
          "width": 480,
          "height": 360
        }
      },
      "channelTitle": "Steve Cook",
      "liveBroadcastContent": "none",
      "publishTime": "2019-08-26T14:58:45Z"
    }
  },
  {
    "kind": "youtube#searchResult",
    "etag": "DG-XTn8KE_oQBUn7Ln42FWaYkXk",
    "id": {
      "kind": "youtube#video",
      "videoId": "eemRXHKsGIc"
    },
    "snippet": {
      "publishedAt": "2021-01-10T15:00:11Z",
      "channelId": "UCOpsZxrmeDARilha1uq4slA",
      "title": "Killer LEG DAY!! // Lower Body STRENGTH WORKOUT",
      "description": "Get Your Nutrition Guide Here: https://heatherrobertson.com/shop/ It's LEG DAY!!! Working on lower body strength today and focusing on power and proper form.",
      "thumbnails": {
        "default": {
          "url": "https://i.ytimg.com/vi/eemRXHKsGIc/default.jpg",
          "width": 120,
          "height": 90
        },
        "medium": {
          "url": "https://i.ytimg.com/vi/eemRXHKsGIc/mqdefault.jpg",
          "width": 320,
          "height": 180
        },
        "high": {
          "url": "https://i.ytimg.com/vi/eemRXHKsGIc/hqdefault.jpg",
          "width": 480,
          "height": 360
        }
      },
      "channelTitle": "Heather Robertson",
      "liveBroadcastContent": "none",
      "publishTime": "2021-01-10T15:00:11Z"
    }
  },
  {
    "kind": "youtube#searchResult",
    "etag": "qFz9B5HTpx1J34jhEiYID2mrsS8",
    "id": {
      "kind": "youtube#video",
      "videoId": "NbTKGS0uHVk"
    },
    "snippet": {
      "publishedAt": "2020-06-22T20:31:18Z",
      "channelId": "UCOpsZxrmeDARilha1uq4slA",
      "title": "Leg Day STRENGTH Workout // For LEAN Legs",
      "description": "It's leg day!! In today's leg day strength workout we are going to lean out those legs with a series of lower body exercises designed to build strength, power and ...",
      "thumbnails": {
        "default": {
          "url": "https://i.ytimg.com/vi/NbTKGS0uHVk/default.jpg",
          "width": 120,
          "height": 90
        },
        "medium": {
          "url": "https://i.ytimg.com/vi/NbTKGS0uHVk/mqdefault.jpg",
          "width": 320,
          "height": 180
        },
        "high": {
          "url": "https://i.ytimg.com/vi/NbTKGS0uHVk/hqdefault.jpg",
          "width": 480,
          "height": 360
        }
      },
      "channelTitle": "Heather Robertson",
      "liveBroadcastContent": "none",
      "publishTime": "2020-06-22T20:31:18Z"
    }
  }
]

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/results')
def results():
    return render_template("results.html", len=len(videos), videos=videos)
