# Jacopo Mauro website

To run the website locally run

```
docker run --rm -it -v $(pwd):/src -p 1313:1313 klakegg/hugo:ext-debian-ci hugo serve
```

or to get a shell

```
docker run --rm -it -v $(pwd):/src -p 1313:1313 --entrypoint /bin/bash klakegg/hugo:ext-debian-ci
```

Note that you can run hugo serve also with option --ignoreCache

### Generate publicaton 

You need to update the mybib.bib file.

Then to remove the proceedings not edited by me run
```
cd my_scripts
python3 filter_out_proceedings.py
```

This generates a file filteredbib.bib
Then you can create the page by running

```
academic import --bibtex --normalize filteredbib.bib content/publication
```

academic can be installe with `pipx install academic`

Then you can add the pdf to the new publications.
To find out the publications without pdf you can run

```
cd my_scripts
python3 has_no_pdfs.py 
```

Note that they introduce a breaking change in version v5.9.0 to define the publication type.
The current version 5.7 does not support the new types (strings instead of ints).
I change the template (see files in layout to support both numbers and new type of publication codes)

Then add manually the pdfs and commit the files

# Hugo Academic Theme

https://github.com/wowchemy/starter-hugo-academic
Too effort to update since they introduce too many breaking changes.