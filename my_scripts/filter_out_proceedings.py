import re

def filter_bib_file(input_file, output_file, editor_name):
    with open(input_file, 'r', encoding='utf-8') as file:
        bib_data = file.read()

    # Regular expression to match individual bibitems
    bibitem_pattern = re.compile(r'@(\w+){(.*?),\n(.*?)}\n', re.DOTALL)

    # Extract bibitems
    bibitems = bibitem_pattern.findall(bib_data)

    # Filter bibitems
    filtered_bibitems = []
    for bibitem in bibitems:
        entry_type, citation_key, entry_body = bibitem
        if entry_type.lower() == 'proceedings':
            if re.search(r'editor\s*=\s*[{"]?Jacopo Mauro[}"]?', entry_body):
                filtered_bibitems.append(bibitem)
        if entry_type.lower() == 'book':
            if re.search(r'author\s*=\s*[{"]?Jacopo Mauro[}"]?', entry_body):
                filtered_bibitems.append(bibitem)
        else:
            filtered_bibitems.append(bibitem)

    # Write filtered bibitems to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for entry_type, citation_key, entry_body in filtered_bibitems:
            file.write(f'@{entry_type}{{{citation_key},\n{entry_body}}}\n\n')

# Usage
input_file = '../mybib.bib'
output_file = '../filteredbib.bib'
editor_name = 'Jacopo Mauro'
filter_bib_file(input_file, output_file, editor_name)
