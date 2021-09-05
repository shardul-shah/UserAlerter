import xml.etree.ElementTree as ET

def parseXML(webhookAlert):
    keyInformation = {}
    tree = ET.parse('results.xml')
    root = tree.getroot()
    elementContainingInfo = "entry"
    defaultNamespace = "atom"
    entrySearch = defaultNamespace + ":" + elementContainingInfo
    namespaces = {"atom": "http://www.w3.org/2005/Atom",
    "youtube": "http://www.youtube.com/xml/schemas/2015"} # add more as needed
    entryElement = root.find(entrySearch, namespaces=namespaces)
    print(entryElement)
    youtubeVideoId = entryElement.find("youtube:videoId", namespaces).text
    print(youtubeVideoId)
    # make dictionary, list of elements I am looking for in entry to make code cleaner
    return

    # key attributes of root object: tag, attrib, text (just like in HTML)

    
    for each in entryElement:
        print(each.tag, each.text)

    return

def main():
    #print(webhookAlert)
    parseXML(webhookAlert)

if __name__ == '__main__':
    main()