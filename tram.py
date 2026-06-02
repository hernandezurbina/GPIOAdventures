import requests
import json
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

def call_and_display(_from, _to):
    stops = {"Buschallee": 900140519,
             "Weisser See": 900140006,
             "Hackescher Markt": 900100002,
             "Am Kupfergraben": 900100038,
             "Virchow-Klinikum": 900010251,
             "Warschauerstr": 900120011
            }    
    
    url = "https://v6.bvg.transport.rest/stops/{}/departures?direction={}&duration=10" # all incoming traffic within 10 mins
    response = requests.get(url.format(stops[_from], stops[_to]))
    
    if response.status_code == 200:
        data = response.json()
        #print(json.dumps(response.json(), indent=2))
    else:
        print(f"({_from} -> {_to}) Request failed:", response.status_code)
        return

    if len(data["departures"]) > 0:        
        line = data["departures"][0]["line"]["name"]
        print(f"{line}: ({_from} -> {_to}) There are", len(data["departures"]), "departures.")        
        when_str = data["departures"][0]["when"]
        departure_time = datetime.fromisoformat(when_str)
        now = datetime.now(departure_time.tzinfo)
        minutes_until = (departure_time - now).total_seconds() / 60
        print(f"Train arrives in {minutes_until:.1f} minutes")
        
        # display in sensehat:
        sense.show_message(f"{line}: {_from}->{_to} {minutes_until:.1f} mins")
    return

def main():
    
    
    ### M4
    call_and_display("Buschallee", "Hackescher Markt")

    ### M12
    call_and_display("Weisser See", "Am Kupfergraben")

    ### M13
    call_and_display("Weisser See", "Warschauerstr")
    
    
    return


if __name__ == "__main__":
    main()