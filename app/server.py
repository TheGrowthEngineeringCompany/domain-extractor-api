
from fastapi import FastAPI, Request, Response, status
import tldextract
from app.utilities import sanitize_url
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

DOMAIN_PROVIDERS = [
    'herokuapp.com',
    'netlify.app'
]

FREEMAIL_PROVIDERS = [
    'gmail'
]


@app.get("/")
@limiter.limit("5/minute")
async def root(request: Request):
    return {"message": "Hello World"}


@app.get('/extract')
@limiter.limit("5/minute")
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
    
    if domain in FREEMAIL_PROVIDERS:
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