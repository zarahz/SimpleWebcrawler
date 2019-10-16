#!/bin/sh

:loop

scrapy runspider E:\Dokumente\workspace\PWP\SimpleWebcrawler\WebCrawler.py;

git add -A
git commit -m "made changes"
git push

sleep 60
goto loop