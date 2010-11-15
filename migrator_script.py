import os
import sys

def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'visaineri.settings'

setup_environment()

from home.models import Verse, Author
import simplejson as json

dumpjs = json.load(open('oldsite_dump.json','r'))
for dobj in dumpjs:
	if dobj["model"] == "visaineri.pa":
		dfields = dobj["fields"]
		try:
			author = Author.objects.get(name=dfields["author"])
		except Author.DoesNotExist:
			author = Author()
			author.name = dfields["author"]
			author.save()
		verse = Verse()
		verse.author = author
		verse.verse_text = dfields["pa"]
		verse.publishing_date = dfields["pubdate"]
		verse.save()
