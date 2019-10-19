# Jacopo Mauro website

To run the website locally run
```
docker run --rm -it \
  -v $(pwd):/src \
  -p 1313:1313 \
  hugo
```

To retreive the publication the [academic-admin](https://github.com/sourcethemes/academic-admin)
tool is used.

```
pip3 install -U academic
cd <MY_WEBSITE_FOLDER>
academic import --bibtex mybib.bib --normalize
```




## Ecosystem

* **[Academic Admin](https://github.com/sourcethemes/academic-admin):** An admin tool to import publications from BibTeX or import assets for an offline site


