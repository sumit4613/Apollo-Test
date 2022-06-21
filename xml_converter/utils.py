import re
import xml.etree.ElementTree as ET
from typing import List, Dict
from xml.etree.ElementTree import Element


def xml_parser(xml) -> Dict:
    """
    Parse XML file and return a dictionary
    """
    tree: ET = ET.parse(xml)

    # get the root element
    root: Element = tree.getroot()
    if not list(root):
        # if the root element has no children, return the root element's text
        return {f"{root.tag}": root.text or ""}

    elements_list: List = []
    # iterate through the root element's children
    for item in root:
        # remove space and newline characters from the text
        item_text = re.sub(r"\s+", "", item.text)

        # create a dictionary for each child element
        item_dict: Dict[str, List[Dict[str, str]]] = {f"{item.tag}": item_text or []}
        for elem in item:
            # add the child element's tag and text to the dictionary
            item_dict[f"{item.tag}"].append({f"{elem.tag}": f"{elem.text}"})
        # add the dictionary to the list
        elements_list.append(item_dict)
    # return the generated dictionary
    return {f"{root.tag}": elements_list}
