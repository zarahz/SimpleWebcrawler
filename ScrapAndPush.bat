#!/bin/sh

:loop

scrapy runspider ./WebCrawler.py;

git add -A
git commit -m "made changes"
git push

sleep 60
goto loop