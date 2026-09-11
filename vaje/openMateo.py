import requests
#https://hackmd.io/@lukac/api1
# izpiši trenutno temperaturo
def trenutne_temperatura(lat, long):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m&timezone=auto&forecast_days=1"
    call = requests.get(base_url).json()
    print(call["current"]["temperature_2m"])


    print("-----------------------------------------------------")

trenutne_temperatura(45.12, 14.5)


#izpiši za nasledne 7 dni
#https://hackmd.io/@lukac/api1
def dnevna_temp(lat, long):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=temperature_2m_max&timezone=auto"
    call = requests.get(base_url).json()
    dates = call["daily"]["time"]
    temperatures = call["daily"]["temperature_2m_max"]

    for date, temperature in zip(dates, temperatures):
        print(f"{date}: {temperature}°C")

    print("-----------------------------------------------------")

dnevna_temp(45.12, 14.5)

#Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.

def najtoplejšinajhladnejši(lat, long):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=temperature_2m_max&timezone=auto"
    call = requests.get(base_url).json()

    temperatures = call["daily"]["temperature_2m_max"]
    dates = call["daily"]["time"]

    max_index = max(range(len(temperatures)), key=lambda i: temperatures[i])
    min_index = min(range(len(temperatures)), key=lambda i: temperatures[i])

    print(f"Najtoplejši dan: {dates[max_index]} - {temperatures[max_index]}°C")
    print(f"Najhladnejši dan: {dates[min_index]} - {temperatures[min_index]}°C")

    print("-----------------------------------------------------")

najtoplejšinajhladnejši(45.12, 14.5)


#Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.

def največja_razlika(lat, long):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    call = requests.get(base_url).json()

    dates = call["daily"]["time"]
    max_temps = call["daily"]["temperature_2m_max"]
    min_temps = call["daily"]["temperature_2m_min"]

    najvecja_razlika = 0
    dan = dates[0]

    for i in range(len(dates)):
        razlika = max_temps[i] - min_temps[i]
        if razlika > najvecja_razlika:
            najvecja_razlika = razlika
            dan = dates[i]

    print(f"Dan z največjo razliko: {dan} - Razlika: {najvecja_razlika}°C")
    print("-----------------------------------------------------")

največja_razlika(45.12, 14.5)



