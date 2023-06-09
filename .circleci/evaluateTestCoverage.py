from sys import argv
from bs4 import BeautifulSoup
from lxml import etree

print('executing test coverage calculation')

def load_html_report(file_path):
    """
    load the jacoco html output. This output includes the coverage percentage, but the XML and CSV output does not.
    """
    with open(file_path, 'r') as f:
        html = ''
        while line := f.readline():
            html = html.join(line)
        return html


def parse_coverage_from_doc(html_document):
    """
    Gets the coverage as a scalar, returns it
    """
    soup = BeautifulSoup(html_document, 'html.parser')
    # parsed = parser.feed(html_document)
    dom = etree.HTML(str(soup))
    xpathresult = dom.xpath('/table/tfoot/td[@class="ctr2"]')
    print(xpathresult)


def run_coverage(file_path):
    """
    """
    html_document = load_html_report(file_path)
    coverage_pct = parse_coverage_from_doc(html_document)
    # set environment variable?
    return coverage_pct


if __name__ == '__main__':
    filepath = argv[1]
    run_coverage(filepath)
