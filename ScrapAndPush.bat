:loop
cd E:\Dokumente\workspace\PWP\SimpleWebcrawler
scrapy runspider .\WebCrawler.py

git add $(git ls-files -o --exclude-standard)
git commit -m "scraping ... :)"
git push

timeout 60
goto loop