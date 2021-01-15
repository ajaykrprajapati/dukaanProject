import bleach


# Cleans text by making the Strings XSS safe
def sanitize_for_xss(input_text, tags=[]):
    return bleach.clean(input_text, tags=tags, strip_comments=True)
