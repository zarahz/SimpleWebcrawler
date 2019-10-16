:loop
cd E:\Dokumente\workspace\PWP\SimpleWebcrawler
scrapy runspider .\WebCrawler.py

git add -A
git commit -m "scraping ... :)"
git push

timeout 60
goto loop