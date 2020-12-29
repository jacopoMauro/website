# Jacopo Mauro website

Theme https://github.com/wowchemy/starter-academic.git

To run the website locally run

```
docker run --rm -it -v $(pwd):/src -p 1313:1313 klakegg/hugo:ext-debian-ci hugo
```

or to get a shell

```
docker run --rm -it -v $(pwd):/src -p 1313:1313 klakegg/hugo:ext-debian-ci /bin/bash
```


To retreive the publication the [academic-admin](https://github.com/sourcethemes/academic-admin)
tool is used.

```
pip3 install -U academic
cd <MY_WEBSITE_FOLDER>
academic import --bibtex mybib.bib --normalize
```

After this tool is run to remove the additional proceeding run the script
/my_scripts/remove_proceedings.sh

