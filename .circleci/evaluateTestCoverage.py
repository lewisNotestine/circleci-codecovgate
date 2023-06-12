from sys import argv
from bs4 import BeautifulSoup
from lxml import etree
import os

print('executing test coverage calculation')

def load_html_report(file_path):
    """
    load the jacoco html output. This output includes the coverage percentage, but the XML and CSV output does not.
    return the html as a string
    """
    with open(file_path, 'r') as f:

        html_lines = f.readlines()
        html = ''.join(html_lines)
        return html


def parse_coverage_from_doc(html_document):
    """
    Gets the coverage as a scalar, returns it
    """
    print('getting code coverage pctage')
    soup = BeautifulSoup(html_document, 'html.parser')
    # the HTML file is the only file that has jacoco's computed percent
    # NOTE: it may be better to compute the percentage from the raw csv instead, to decouple it from the presentation/markup
    dom = etree.HTML(str(soup).encode())
    xpathresult = dom.xpath('/html/body/table/tfoot//td[@class="ctr2"]')

    print(xpathresult[0])
    pctage: str = xpathresult[0].text
    return pctage.replace('%','')



def run_coverage(source_coverage_file_path,
                 output_dir,
                 circleci_branch_cachekeyname):
    """
    Writes the gathered coverage pct metric to a file
    """
    html_document = load_html_report(source_coverage_file_path)
    coverage_pct = parse_coverage_from_doc(html_document)

    # save pctage in file

    output_file = os.path.join(output_dir, f'{circleci_branch_cachekeyname}.txt')
    with open(output_file, 'w') as wf:
        wf.writelines(coverage_pct)
        wf.flush()
        wf.close()


if __name__ == '__main__':
    filepath = argv[1]
    circleci_branch_cachekeyname = argv[2]
    run_coverage(filepath, circleci_branch_cachekeyname)
