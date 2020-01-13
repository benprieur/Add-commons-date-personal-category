import sys
import pywikibot
from pywikibot import pagegenerators
siteC = pywikibot.Site(u'commons', u'commons')
siteC.login()

category = pywikibot.Category(siteC, u'Videos by Benoît Prieur')
print("this category is analysed...")

gen = pagegenerators.CategorizedPageGenerator(category)

for page in gen:
  #text = page.text
  for (template, params) in page.templatesWithParams():
    if template.title() == 'Template:Information':
      for param in params:
        param.replace(" ", "")
        if param[0: 5] == 'Date=':
          date = param[5:]
          print(date)
          index = date.index('-')
          year = date[0: index]
          print(year)

          if len(year) == 4:
            nameCategory = "[[Category:" + str(year) + " videos by Benoît Prieur]]"
            print(nameCategory)
            if page.text.find(nameCategory) == - 1:
              page.text = page.text + "\r\n" + nameCategory
              page.save(u"add personal date category: " + nameCategory)
              print("save")

      break