import requests
import json
from datetime import datetime
from sense_hat import SenseHat


def main():
    sense = SenseHat()
    sense.set_rotation(180)
    
    stops = {"buschallee": 900140519,
             "weisser see": 900140006,
             "hackescher markt": 900100002,
             "am kupfergraben": 900100038,
             "virchow-klinikum": 900010251,
             "warschauerstr": 900120011
            }
            
    url = "https://v6.bvg.transport.rest/stops/{}/departures?direction={}&duration=10" # all incoming traffic within 10 mins
    
    ### M4
    response = requests.get(url.format(stops["buschallee"], stops["hackescher markt"]))
    
    if response.status_code == 200:
        data = response.json()
        #print(json.dumps(response.json(), indent=2))
    else:
        print("Request failed:", response.status_code)
        return

    if len(data["departures"]) > 0:
        print("M4: Buschallee->Hackescher Markt. There are", len(data["departures"]), "departures.")
        when_str = data["departures"][0]["when"]
        departure_time = datetime.fromisoformat(when_str)
        now = datetime.now(departure_time.tzinfo)
        minutes_until = (departure_time - now).total_seconds() / 60
        print(f"Train arrives in {minutes_until:.1f} minutes")
        
        # display in sensehat:
        sense.show_message(f"M4: Buschallee->Hackescher Markt {minutes_until:.1f} mins")
    return


if __name__ == "__main__":
    main()