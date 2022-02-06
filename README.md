# Export your LiveJournal blog data

[Livejournal provides a method to export your posts as 
XML](http://www.livejournal.com/export.bml). However 
this has to be done manually for every month of your blog. 
Also [comments are exported separately](http://www.livejournal.com/developer/exporting.bml).
I wrote this tool to make exporting more convenient.

You will need Python 3 to use it.

## Usage:

Usage: export.py [OPTIONS] COMMAND [ARGS]...

Options:
+    --help  Show this message and exit.

Commands:
+ **export**    
  + Login, Download comments and posts, and Export data to markdown/html
  + Options:   
    + -ys, --year_start first 4 digit year to include entries from. e.g.
                             1998
    + -ye, --year_end   first 4 digit year to exclude entries from. e.g.
                             2023
    + -s, --skip_download        Do not download from livejournal, process already
                             downloaded files.
+ **download comments**
  + Login and Download all comments.
+ **download posts**
  + Login and Download all posts. 
  + Options:   
    + -ys, --year_start first 4 digit year to include entries from. e.g.
                             1998
    + -ye, --year_end   first 4 digit year to exclude entries from. e.g. 2023

+ **logout** 
  + Delete saved login session

download subcommands:


## export

This command is the main entry point, see commands above. If you are not logged in, 
it will prompt you for username and password and save the session cookies (in lj.cookies) if
login succeeds. Session cookies will be reused until deleted (with **logout**)

After running **export.py export** You will end up with full blog contents in several 
formats. `posts-html` folder will contain basic HTML
of posts and comments. `posts-markdown` will contain
posts in Markdown format with HTML comments and metadata 
necessary to [generate a static blog with Pelican](http://docs.getpelican.com/).
`posts-json` will contain posts with nested comments 
in JSON format should you want to process them further.

## download posts

This command will download your posts in XML into `posts-xml` 
folder. Also it will create `posts-json/all.json` file with all 
the same data in JSON format for convenient processing.

## download comments

This command will download comments from your blog as `comments-xml/*.xml`
files. Also it will create `comments-json/all.json` with all the 
comments data in JSON format for convenient processing.

## logout

This command will delete the saved session login information in lj.cookies.

## Requirements

* `click`
* `html2text`
* `markdown`
* `beautifulsoup4`
* `requests`

## Processing exported data separately

Use the **-skip_download** option of **export** to skip the downloading step and go
directly to the processing of already downloaded data.

