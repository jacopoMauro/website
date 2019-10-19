import os
import re

def slugify(s, lower=True):
    bad_symbols = ('.', '_', ':')  # Symbols to replace with hyphen delimiter.
    delimiter = '-'
    good_symbols = (delimiter,)  # Symbols to keep.
    for r in bad_symbols:
        s = s.replace(r, delimiter)

    s = re.sub(r'(\D+)(\d+)', r'\1\-\2', s)  # Delimit non-number, number.
    s = re.sub(r'(\d+)(\D+)', r'\1\-\2', s)  # Delimit number, non-number.
    s = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r'\-\1', s)  # Delimit camelcase.
    s = ''.join(c for c in s if c.isalnum() or c in good_symbols).strip()  # Strip non-alphanumeric and non-hyphen.
    s = re.sub('\-+', '-', s)  # Remove consecutive hyphens.

    if lower:
        s = s.lower()
    return s

dirs = [x[0].replace("../content/publication/","") for x in os.walk("../content/publication/")]

pdfs = {}
for f in os.listdir("../static/papers/"):
    if f.endswith(".pdf"):
        path = f.replace(".pdf","")
        path = slugify(path)
        path = path.replace("-","")
        pdfs[path] = f

for d in dirs:
    s = d.replace("-","")
    if s in pdfs:
        print("cp ../static/papers/{} ../content/publication/{}/{}.pdf".format(pdfs[s], d, d))
    else:
        print("# Warning. PDF not found for {}".format(d))

