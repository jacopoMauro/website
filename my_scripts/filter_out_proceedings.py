import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def filter_bibtex_entries(bib_database, editor_name):
    filtered = []
    for entry in bib_database.entries:
        entry_type = entry.get('type', '').lower()  # In newer versions of bibtexparser, the key is "ENTRYTYPE".
        if not entry_type:
            # Some old versions store the type under 'ENTRYTYPE', so we might need:
            entry_type = entry.get('ENTRYTYPE', '').lower()

        if entry_type == 'proceedings':
            # Keep only if 'editor' contains the desired name
            editor_field = entry.get('editor', '')
            if editor_name in editor_field:
                filtered.append(entry)

        elif entry_type == 'book':
            # Keep only if 'author' contains the desired name
            author_field = entry.get('author', '')
            if editor_name in author_field:
                filtered.append(entry)

        else:
            # For any other entry types, keep them as is
            filtered.append(entry)
    return filtered

def filter_bib_file(input_file, output_file, editor_name):
    # 1. Parse the .bib file
    with open(input_file, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    # 2. Filter entries
    filtered_entries = filter_bibtex_entries(bib_database, editor_name)

    # 3. Put filtered entries into a new database
    new_db = BibDatabase()
    new_db.entries = filtered_entries

    # 4. Write the filtered database back to a .bib file
    writer = BibTexWriter()
    # You can customize writer settings, e.g.:
    # writer.indent = '  '
    # writer.comma_first = True
    with open(output_file, 'w', encoding='utf-8') as bibtex_out:
        bibtex_out.write(writer.write(new_db))

# Usage
if __name__ == "__main__":
    input_file = '../mybib.bib'
    output_file = '../filteredbib.bib'
    editor_name = 'Jacopo Mauro'
    filter_bib_file(input_file, output_file, editor_name)
