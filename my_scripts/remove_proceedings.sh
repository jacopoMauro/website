#!/bin/bash

# This script remove the publication that are only proceeding in bib and
# are automatically added by academic import --bibtex mybib.bib --normalize

cd ../content/publication/
for d in */ ; do
	if grep -q "Jacopo Mauro" "$d/index.md"; then
	  if [[ -n $(find "$d" -maxdepth 1 -type f -name '*.pdf') ]]; then
	    # remove all lines starting with "url_pdf"
	    sed -i '/^url_pdf/ d' "$d/index.md"
	  else
	    echo "Warning. Directory $d has no pdf file"
	  fi
	else
		echo "Removing directory $d"
		rm -rf $d
	fi
done

