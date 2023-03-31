LOCAL_WEATHER_URL = "http://192.168.0.12/json

if __name__ == '__main__':
    print(os.getcwd())
    url = 'http://192.168.0.12/json'
    filename = "data/weather.csv"
    while True:
        now = datetime.datetime.now()
        if now.minute % 30 == 0:
            data = get_json(url)
            save_to_csv(data, filename)
            print(f'Data saved to {filename} at {time.strftime("%H:%M:%S")}')
        time.sleep(60)