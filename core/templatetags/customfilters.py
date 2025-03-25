# yourapp/templatetags/custom_filters.py

from django import template
from bs4 import BeautifulSoup
import re
register = template.Library()

@register.filter(name='strip_ul')
def strip_ul(value):
    soup = BeautifulSoup(value, 'html.parser')
    lis = soup.find_all('li')
    return ''.join(str(li) for li in lis)

@register.filter
def strip_p_tags(value):
    # Remove only the <p> and </p> tags
    return re.sub(r'</?p>', '', value)

@register.filter
def first_paragraph(value):
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(value, "html.parser")
    # Find the first <p> tag
    first_p = soup.find('p')
    # Return the content of the first <p> tag if it exists
    return str(first_p) if first_p else ''

@register.simple_tag
def increment_counter(counter):
    return counter + 1

@register.filter
def contains_p_tag(value):
    return bool(re.search(r'<p\b[^>]*>', value))  # checks for <p> or <p ...>

@register.filter
def split_p_and_ul(value):
    """Preserves the order and structure of <p> and <ul> elements."""


    soup = BeautifulSoup(value, "html.parser")
    output = ""

    # Process each child node in order
    for element in soup.children:
        if element.name == "p":
            # Keep <p> tags as-is
            output += str(element)
        elif element.name == "ul":
            # Add required classes to <ul> tags
            element["class"] = element.get("class", []) + ["list-unstyled", "list-check-circle-outline", "mt-4"]
            output += str(element)
        elif element.name is None and str(element).strip():
            # Include non-tag content (e.g., text nodes) as-is
            output += str(element)

    return output


@register.filter
def chunked_li(value, chunk_size=3):
    """
    Splits a string of <li> elements into chunks of a given size.
    """
    # Parse the HTML string
    soup = BeautifulSoup(value, 'html.parser')
    
    # Find all <li> elements
    li_elements = soup.find_all('li')

    # Split into chunks
    chunks = [li_elements[i:i + chunk_size] for i in range(0, len(li_elements), chunk_size)]
    print(chunks)
    return chunks


@register.filter
def split_list(value):
    """
    Splits the string into a list of items.
    Assume that each item is separated by a line break or comma.
    """
    return value.splitlines()  # or use split(',') for comma-separated values