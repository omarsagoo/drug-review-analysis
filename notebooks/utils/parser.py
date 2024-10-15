import re
import urllib.parse
import html

def parse_string(input):
    # Decode HTML entities and URL-encoded characters in a single pass
    input = html.unescape(urllib.parse.unquote(input))

    # remove excess white space and convert hyphens to spaces
    input = re.sub(r'[\-]+|\s+', ' ', input).strip()

    # remove any special characters
    input = re.sub(r'[^a-zA-Z0-9 ]+', '', input)

    return input.lower()

def find_first_occurence(key, arr):
    if key == '':
        return -1

    for (i, item) in enumerate(arr):
        # if the item is 3 characters or less, skip.
        # else if there is a match found
        if len(item) <= 3:
            continue
        elif item in key or key in item:
            return i

    return -1
