import uvicorn as uvicorn
from fastapi import FastAPI
import json
app = FastAPI()
from fastapi.responses import PlainTextResponse
#@app.get("/")
@app.get("/", response_class=PlainTextResponse)
def extract_data():
    #return {"Hello": "Wooooorld"}
    # Read data from CSV

    f = open('/code/app/name.json')
    name = json.load(f)
    f = open('/code/app/description.json')
    description = json.load(f)
    f = open('/code/app/logo_url.json')
    logo_url = json.load(f)
    f = open('/code/app/hq_city.json')
    hq_city = json.load(f)
    f = open('/code/app/hq_country.json')
    hq_country = json.load(f)
    f = open('/code/app/linkedin_url.json')
    linkedin_url = json.load(f)
    f = open('/code/app/twitter_url.json')
    twitter_url = json.load(f)
    f = open('/code/app/startup_partners_count.json')
    startup_partners_count = json.load(f)
    f = open('/code/app/startup_partners.json')
    startup_partners = json.load(f)
    f = open('/code/app/website_url.json')
    website_url = json.load(f)

    string = ""
    for i in range(len(name)):
        string = string + str(i + 1) + " - " + name[i] + "\n"
        if description[i]:
            string = string + "Description: " + description[i] + "\n"
        if logo_url[i]:
            string = string + "logo url: " + logo_url[i] + "\n"
        if hq_city[i]:
            string = string + "hq_city: " + hq_city[i]
        if hq_country[i]:
            string = string + " - hq_country: " + hq_country[i] + "\n"
        if twitter_url[i]:
            string = string + "twitter_url: " + twitter_url[i]
        if linkedin_url[i]:
            string = string + "  -  linkedin_url: " + linkedin_url[i]
        if website_url[i]:
            string = string + "  -  website_url: " + website_url[i] + "\n"
        if startup_partners_count[i]:
            string = string + "startup_partners_count: " + str(startup_partners_count[i]) + "\n"
        if startup_partners[i]:
            string = string + "startup_partners: " + str(startup_partners[i]) + "\n" + "\n"

    return string

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, port=8000)