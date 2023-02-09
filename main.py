# List all Amazon Invoices in Folder
# Open PDF Invoice find Name and Item Value

import os
import re

import unicodedata
from pdfreader import SimplePDFViewer


# Invoice Date:
# Invoice Value:
# Total + 3
# Press the green button in the gutter to run the script.


def provide_filename(file_name):
    print("Working on:")
    print(file_name)
    with open(file_name, "rb") as fd:
        viewer = SimplePDFViewer(fd)
        all_words_of_doc = []
        for canvas in viewer:
            page_strings = canvas.strings
            # print("Line 1")
            print(page_strings)
            for word in page_strings:
                all_words_of_doc.append(word)
    fd.close()
    if any("a replacement" in s for s in all_words_of_doc):
        invoice_total_value = ""
        invoice_date_value = "replacement"
    elif any("Credit Note" in s for s in all_words_of_doc):
        invoice_total_value = ""
        invoice_date_value = "return"
    else:
        invoice_date_index = all_words_of_doc.index("Order Date:") + 1
        invoice_date_value = all_words_of_doc[invoice_date_index].replace('.', '-')
        invoice_total_value_index = all_words_of_doc.index("TOTAL:") + 2
        invoice_total_value = all_words_of_doc[invoice_total_value_index]

    product_desc_index = all_words_of_doc.index("Total") + 3

    invoice_filename = invoice_date_value + "_" + invoice_total_value[:-2] + \
                       "_" + all_words_of_doc[product_desc_index]

    invoice_filename = slugify(invoice_filename)
    print("File Name: " + invoice_filename)
    return invoice_filename


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def do_multiple_files(dir_path):

    dir_list = os.listdir(dir_path)
    for current_file_name in dir_list:
        new_filename = provide_filename(dir_path + current_file_name)
        os.rename(dir_path + current_file_name, dir_path + new_filename+'.pdf')
        print("Renamed File: " + new_filename)


if __name__ == '__main__':
    single_filename = r"C:\Users\jayam\OneDrive\Desktop\Amazon_new\2023\invoice - 2023-02-08T210720.999.pdf"
    folder_path = r'C:\\Users\\jayam\\OneDrive\\Desktop\\Amazon_new\\2023' + '\\'
    # provide_filename(single_filename)
    do_multiple_files(folder_path)
