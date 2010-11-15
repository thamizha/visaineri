# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from parsers import tamil_parser

class Author(models.Model): #ஆசிரியர்
    name = models.CharField(max_length=100, verbose_name='பெயர்')
    user = models.ForeignKey(User, null=True, blank=True, unique=True, related_name='author_profile')
    biography = models.TextField(verbose_name='வாழ்க்கை சரித்திரம்', blank=True)
    
    def __unicode__(self):
        return self.name

PARSING_STATUS_OPTIONS = ( # பகுப்பாய்வு_குறிப்பு_தேர்வுகள்
   ('N', 'ஆராயப்படவில்லை'),
   ('Y', 'தகவல் இருக்கிறது'),
   ('E', 'பிழையுள்ளது'),
)

class Verse(models.Model): #பா
    author = models.ForeignKey(Author, null=True, blank=True, verbose_name='ஆசிரியர்', related_name='verses')
    publishing_date = models.DateTimeField(null=True, auto_now_add = True, verbose_name='பதிப்பு_நேரம்')
    revision_date = models.DateTimeField(null=True, auto_now = True, verbose_name='திருத்தப்பட்ட நேரம்')
    verse_text = models.TextField(verbose_name='பா_செய்யுள்')
    parsing_status = models.CharField(max_length=2, choices=PARSING_STATUS_OPTIONS, default='N', verbose_name='பகுப்பாய்வு_குறிப்பு')
    result = models.XMLField(blank=True, verbose_name='முடிவுகள்')
    
    def __unicode__(self):
        return self.verse_text[:15] + '...'
    
    def save(self, *args, **kwargs):
        result = tamil_parser.analyzeVerse(self.verse_text.replace('\r','\n'))
        if result is None:
            self.result = ''
            self.parsing_status = 'E'
        else:
            self.result = result
            self.parsing_status = 'Y'
        super(Verse, self).save(args, kwargs)
