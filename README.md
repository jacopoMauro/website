# Jacopo Mauro website

To run the website locally run

```
docker run --rm -it -v $(pwd):/src -p 1313:1313 klakegg/hugo:ext-debian-ci hugo
```

or to get a shell

```
docker run --rm -it -v $(pwd):/src -p 1313:1313 --entrypoint /bin/bash klakegg/hugo:ext-debian-ci
```


### Generate publicaton 

You need to update the mybib.bib file.

Then to remove the proceedings not edited by me run
```
cd my_scripts
python3 filter_out_proceedings.py
```

This generates a file filteredbib.bib

Then, to generate the markdowns from the website folder:

```
docker run -v `pwd`:/mydir --rm -it --entrypoint /bin/bash python

apt update
apt install python3-pip
pip3 install academic --upgrade

cd /mydir
academic import --bibtex --normalize filteredbib.bib content/publication
```

Note that they introduce a breaking change in version v5.9.0 to define the publication type.
The current version 5.7 does not support the new types (strings instead of ints).
To avoid doing a big update if the publications are few consider changing the pub manually
after using the academic tool.
To change owner and group and change the publication type

```
sudo bash postAcademicProcessing.sh
```

Then add manually the pdfs and commit the files

# Hugo Academic Theme

https://github.com/wowchemy/starter-hugo-academic
Too effort to update since they introduce too many breaking changes.