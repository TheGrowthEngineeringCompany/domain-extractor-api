
from fastapi import FastAPI, Request, Response, status
import tldextract
from app.utilities import sanitize_url, load_freemail_blacklist
from fastapi.responses import PlainTextResponse


app = FastAPI()

DOMAIN_PROVIDERS = [
    'herokuapp.com',
    'netlify.app',
    'web.app',
    'firebaseapp.com',
    'heroku.com',
    'hey.com',
    'netlify.com',
    'netlify.app',
    'mail.ru',
    'vk.com',
    'carrd.co'
]

FREEMAIL_PROVIDERS = load_freemail_blacklist()


@app.get("/")
async def root(request: Request):
    return {"message": "Hello World"}

@app.get("/loaderio-e018bfba64138d4ebe381481dc8af392.txt", response_class=PlainTextResponse)
def loaderio_verify():
    return 'loaderio-e018bfba64138d4ebe381481dc8af392'


@app.get('/extract')
async def domain(url: str, request: Request,response: Response):
    url = sanitize_url(url)

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

    if extraction.registered_domain in FREEMAIL_PROVIDERS:
        freemail_provider = True

    if extraction.registered_domain in DOMAIN_PROVIDERS:
        return {
            "url": f"{url}",
            "domain": f"{subdomain}.{domain}.{suffix}",
            "freemail_provider": freemail_provider

        }

    return {
        "url": f"{url}",
        "domain": f"{extraction.registered_domain}",
        "freemail_provider": freemail_provider
    }
