import os
import requests
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

API_URL = "https://api.vachana.ai/stt/v3"

@require_http_methods(["GET", "POST"])
def home(request):
    transcript = ""
    error = ""

    if request.method == "POST":
        audio = request.FILES.get("audio")

        if not audio:
            error = "please select an audio file to upload."

        elif audio.size > 10 * 1024 * 1024:
            error = "File size exceeds the limit of 10MB."

        else:
            api_key = os.getenv("GNANI_API_KEY")
            print("gnani API key loaded:", bool(api_key))

            if not api_key or api_key == "YOUR_ACTUAL_API_KEY":
                error = "API key missing. check your .env file."

            else:      
                try:
                    response = requests.post(
                     API_URL,
                     headers={"X-API-Key-ID": api_key},
                     data={
                        "language_code": "hi-IN",
                        "preferred_language": "hi-IN",
                        "format": "transcribe",
                        "itn_native_numerals": "true",

                    },
                    files={
                        "audio_file":(audio.name, audio.file, audio.content_type or "application/octet-stream"),
                    },
                    timeout=90,
                    )

                    if not response.ok:
                    #     error = (
                    #     f"API request failed with status code ({response.status_code})."
                    #     "check api access, file format and usage limits."
                    # )
                      print("GNANI STATUS:", response.status_code)
                      print("GNANI RESPONSE:", response.text)
                      error = f"Gnani API error({response.status_code}). check terminal."

                    else:
                        data = response.json()
                        transcript = data.get("transcript", "")

                        if not transcript:
                            error = (
                            "No transcript found in the API response."
                            "check the api response and audio file format."
                        )
                except requests.exceptions.RequestException:
                    error = (
                    "could not connect to the  gnani API." 
                    "error check your internet connection and api access."
                    )          
                except ValueError:
                    error = (
                    "Invalid response from the API."
                    "check the api response and audio file format."
                    )


    return render(
        request, 
         "assistant/home.html",
         {"transcript": transcript, "error": error},
      )
     
