import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader, select_autoescape

def parseXML(webhookAlert):
    tree = ET.parse('results.xml')
    root = tree.getroot()
    elementContainingInfo = "entry"
    defaultNamespace = "atom"
    youtubeNamespace = "youtube"
    keyElements = {youtubeNamespace+":videoId": None, youtubeNamespace+":channelId": None,
    defaultNamespace+":title": None, defaultNamespace+":author": None, 
    defaultNamespace+":published": None, defaultNamespace+":updated": None}
    entrySearch = defaultNamespace + ":" + elementContainingInfo
    nameSearch = defaultNamespace + ":" + "name"
    namespaces = {"atom": "http://www.w3.org/2005/Atom",
    "youtube": "http://www.youtube.com/xml/schemas/2015"} # add more as needed

    entryElement = root.find(entrySearch, namespaces=namespaces)
    # print(entryElement)

    for key in keyElements:
        if key == defaultNamespace+":author":
            keyElements[key] = entryElement.find(key, namespaces).find(nameSearch, namespaces).text
        else:
            keyElements[key] = entryElement.find(key, namespaces).text

    # for key in keyElements:
    #     if key == defaultNamespace+":author":
    #         keyElements[key] = entryElement.find(key,namespaces).find(nameSearch, namespaces).text

        
    print(keyElements)
    return keyElements

    # fxn for reaching youtube api if needed, forming email from above info
    # key attributes of root object: tag, attrib, text (just like in HTML)

def generateHTMLForEmail():
    templateLoader = FileSystemLoader(searchpath="./templates")
    templateEnv = Environment(loader=templateLoader, autoescape = select_autoescape())
    templateFile = "email.html"
    template = templateEnv.get_template(templateFile)

    youtubeData = parseXML(parseXML)

    # must check if published is the publication date or updated is
    # replace placeholder names
    # also get image thumbnail from youtube API
    # timezone = ? of youtube time zone
    templateParameters = {"username": "Shardul", "youtubeChannelName": youtubeData["atom:author"], "youtubeVideoTitle":  youtubeData["atom:title"],
    "youtubeChannelId": youtubeData["youtube:channelId"], "youtubeVideoId": youtubeData["youtube:videoId"],
    "vidLengthInMinutes": "2 ", "vidLengthInSeconds": "13",
    "youtubeVideoReleaseDate": youtubeData["atom:published"], "youtubeVideoDescription": "placeHolderNeedFromAPI"}

    outputText = template.render(templateParameters) # this is where to put args to the template renderer

    # print ("Content-type: text/html\r\n\r\n")
    print(outputText)
    return outputText

def main():
    #print(webhookAlert)
    generateHTMLForEmail()

if __name__ == "__main__":
    main()