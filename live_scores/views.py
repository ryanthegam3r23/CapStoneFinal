import requests
from django.shortcuts import render



HEADERS = {
    "x-rapidapi-key": "dec80da01bmshf75e0f03720d3cbp1c6d73jsn4d3b46330aac",
    "x-rapidapi-host": "nfl-api-data.p.rapidapi.com"
}
def live_scores(request):
    url = "https://nfl-api-data.p.rapidapi.com/nfl-livescores"
    headers = {
        "X-RapidAPI-Host": "nfl-api-data.p.rapidapi.com",
        "X-RapidAPI-Key": "dec80da01bmshf75e0f03720d3cbp1c6d73jsn4d3b46330aac"  # Replace with your RapidAPI key
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(response.status_code)
        print(response.text)
       

    except Exception as e:
        games = []
        print("Error fetching live scores:", e)

    return render(request, 'scores/live_scores.html', {'live': data.get("live")})



import requests
from django.shortcuts import render

def game_detail(request, game_id):
    print("details for: " + str(game_id))
    url = "https://nfl-api-data.p.rapidapi.com/nfl-livescores"

    headers = {
        "x-rapidapi-key": "dec80da01bmshf75e0f03720d3cbp1c6d73jsn4d3b46330aac",  # your API key
        "x-rapidapi-host": "nfl-api-data.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        # find the specific game
        game_data = None
        for g in data.get("live", []):
            if str(g.get("id")) == str(game_id):
                game_data = g
                break

        if not game_data:
            return render(request, "scores/game_detail.html", {
                "error": f"No game found for ID {game_id}."
            })

        homeCompetitor = game_data.get("homeCompetitor", {})
        awayCompetitor = game_data.get("awayCompetitor", {})
        status = game_data.get("statusText", "No status")
        time = game_data.get("gameTimeDisplay", "")

        # ✅ Map symbolicName → abbreviation (for logo filenames)
        home_abbr = homeCompetitor.get("symbolicName", "unknown")
        away_abbr = awayCompetitor.get("symbolicName", "unknown")
        homeCompetitor["abbreviation"] = home_abbr
        awayCompetitor["abbreviation"] = away_abbr

    except Exception as e:
        print("Error fetching game:", e)
        return render(request, "scores/game_detail.html", {
            "error": "Unable to fetch live game data right now."
        })

    context = {
        "homeCompetitor": homeCompetitor,
        "awayCompetitor": awayCompetitor,
        "gameTimeDisplay": time,
        "status": status,
    }

    return render(request, "scores/game_detail.html", context)






