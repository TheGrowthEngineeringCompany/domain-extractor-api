import csv

def sanitize_url(url: str):
    result = url.lstrip()
    result = result.rstrip()
    result = result.lower()

    return result


def load_freemail_blacklist():
    blacklist = []
    with open('./app/freemails.csv', 'r') as sheet:
        reader = csv.DictReader(sheet)
        for row in reader:
            blacklist.append(row['domain'])
        

    return blacklist
