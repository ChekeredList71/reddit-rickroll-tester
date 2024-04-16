import ricklib

if ricklib.is_link_valid(""):
    comment = ricklib.extract_comment("")

    if ricklib.is_text_ricked(comment):
        print("van")
    else:
        print("nincs")
