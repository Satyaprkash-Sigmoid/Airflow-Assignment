import csv
import http.client
def write_csv():

    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "6de699b1d8mshd8bd55d7354877cp1e4523jsn27d1f547437f"
    }

    conn.request("GET", "/weather?q=London%2Cuk&lat=0&lon=0&callback=test&id=2172797&lang=null&units=imperial&mode=xml",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    header = ['name', 'area', 'country_code2', 'country_code3']
    data = [
        ['Albania', 28748, 'AL', 'ALB'],
        ['Algeria', 2381741, 'DZ', 'DZA'],
        ['American Samoa', 199, 'AS', 'ASM'],
        ['Andorra', 468, 'AD', 'AND'],
        ['Angola', 1246700, 'AO', 'AGO']
    ]
    try:
        with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)

        print("Done Successfully")
    except:
        print("connection error...")

write_csv()