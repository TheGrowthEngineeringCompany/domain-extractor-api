
from fastapi import FastAPI, Response, status
import tldextract

app = FastAPI()

DOMAIN_PROVIDERS = [
    'herokuapp.com',
    'netlify.app'
]

FREEMAIL_PROVIDERS = [
    'gmail'
]


REGEX_URL = """(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/extract')
async def domain(url: str, response: Response):
    extraction = tldextract.extract(url)

    subdomain = extraction.subdomain
    domain = extraction.domain
    suffix = extraction.suffix

    freemail_provider = False

    if suffix == '':
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return


    if 'www.' in subdomain:
        subdomain = subdomain.split('www.', 1)[1]
    
    if domain in FREEMAIL_PROVIDERS:
        freemail_provider = True

    if extraction.registered_domain in DOMAIN_PROVIDERS:
        return {
            "url": f"{url}",
            "status": 200,
            "domain": f"{subdomain}.{domain}.{suffix}",
            "freemail_provider": freemail_provider

        }   
    
    return {
        "url": f"{url}",
        "status": 200,
        "domain": f"{extraction.registered_domain}",
        "freemail_provider": freemail_provider
    }