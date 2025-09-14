import requests
from django.shortcuts import render

def home(request):
    word = None
    meaning = []
    synonyms = []
    antonyms = []
    error = None

    if request.method == "POST":
        word = request.POST.get("word")
        print("WORD RECEIVED:", word)

        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        try:
            response = requests.get(url, timeout=5)  
            print("API STATUS:", response.status_code)

            if response.status_code == 200:
                data = response.json()
                print("API RESPONSE:", data)  

                # Extract meanings
                for m in data[0]["meanings"]:
                    part_of_speech = m.get("partOfSpeech", "")
                    definitions = [d.get("definition", "") for d in m["definitions"]]
                    meaning.append({
                        "part_of_speech": part_of_speech,
                        "definitions": definitions
                    })

                    
                    for d in m["definitions"]:
                        synonyms.extend(d.get("synonyms", []))
                        antonyms.extend(d.get("antonyms", []))

            else:
                error = "⚠️ Word not found in dictionary."
        except Exception as e:
            error = f"❌ Error fetching data: {str(e)}"

    return render(request, "dictionary_app/home.html", {
        "word": word,
        "meaning": meaning,
        "synonyms": list(set(synonyms)),
        "antonyms": list(set(antonyms)),
        "error": error,
    })
