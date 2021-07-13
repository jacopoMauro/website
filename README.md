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
apt update
apt install python3-pip
pip3 install academic --upgrade

cd <MY_WEBSITE_FOLDER>
academic import --bibtex mybib.bib --normalize
```

After this tool is run to remove the additional proceeding run the script
cd my_scripts
bash remove_proceedings.sh

