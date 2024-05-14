# scraper
Python pipeline to scrape text from websites and process the output.

This pipeline takes in a specified url, a desired depth, and an html object, and scrapes the content corresponding to that html content from all linked sites, up to the desired depth, and saves the content and link structure in a graph. The scraping is done through a BFS graph traversal algorithm. 

You can run an example of this pipeline by running `bash scripts/pipeline.sh`, which scrapes the website [The Good Research Handbook](https://goodresearch.dev/) (which was a major inspiration to start this project), to a depth of 3 links, saving the output of every 'p' html element.
