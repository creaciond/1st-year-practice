# Digital collection of works by Leo Tolstoy
Link (in Russian): http://tolstoy.ru/creativity/90-volume-collection-of-the-works/

**links** — all the "find" code is searching for links to letters to S.A. Tolstaya and V.G. Chertkov in volumes 53-82 (in these, the files are empty, all the texts are in volumes 83-89)
* other code — finds letters according to the links in the .xml file

**mark draft, unsent letters** — all the letters marked as "черновое" (draft) or "неотправленное" (unsent) are to have a special attribute in tag `<correspAction>` (for instance, `<correspAction type="draft">` or `<correspAction type="unsent">`)

**rename files** — files named as Volume_N/letterQ.xml have to be renamed as VolumeN/letter_id.xml (retrieved from the letter itself: `<text xml:id="RektoruKazanskogouniversiteta._1">` means that letter ID is "RektoruKazanskogouniversiteta._1") 