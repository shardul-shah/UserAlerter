import xml.etree.ElementTree as ET

def parseKeyInformationFromXML(webhookAlert):
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
    webhookAlert = "<?xml version='1.0' encoding='UTF-8'?> \
<feed \
    xmlns:yt='http://www.youtube.com/xml/schemas/2015' \
    xmlns='http://www.w3.org/2005/Atom'> \
    <link rel='hub' href='https://pubsubhubbub.appspot.com'/> \
    <link rel='self' href='https://www.youtube.com/xml/feeds/videos.xml?channel_id=UCSN8HjojRhNwXkpT9dK5ZZQ'/> \
    <title>YouTube video feed</title> \
    <updated>2021-08-31T04:21:06.194582719+00:00</updated> \
    <entry> \
        <id>yt:video:quCZe_N6tyQ</id>\
        <yt:videoId>quCZe_N6tyQ</yt:videoId> \
        <yt:channelId>UCSN8HjojRhNwXkpT9dK5ZZQ</yt:channelId> \
        <title>test 133</title> \
        <link rel='alternate' href='https://www.youtube.com/watch?v=quCZe_N6tyQ'/> \
        <author> \
            <name>5hardul League</name> \
            <uri>https://www.youtube.com/channel/UCSN8HjojRhNwXkpT9dK5ZZQ</uri> \
        </author> \
        <published>2021-08-31T04:20:20+00:00</published> \
        <updated>2021-08-31T04:21:06.194582719+00:00</updated> \
    </entry> \
</feed> \
            \
<!-- from yt video id to link: --> \
<!-- https://www.youtube.com/watch?v=quCZe_N6tyQ --> \
<!-- you can make further requests to Youtube API to get more information -->   "

    #print(webhookAlert)
    parseKeyInformationFromXML(webhookAlert)

if __name__ == '__main__':
    main()