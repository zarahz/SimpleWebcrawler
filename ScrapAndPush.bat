:loop
cd E:\Dokumente\workspace\PWP\SimpleWebcrawler
echo dir
scrapy runspider .\WebCrawler.py

git add -A
git commit -m "made changes"
git push

timeout 60
goto loop