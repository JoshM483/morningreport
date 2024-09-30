# Your Daily AI Morning Report
> **Note:** This project is actively under construction!!

This is the source code and hosting location for a simple summarized morning report. 

I originally hosted and ran the site off my local machine but I recently decided to migrate it to a GitHub project page and updated daily with GitHub actions. 

## Works Thanks To:
- [Bootstrap for github pages][1]<br>
- [duckduckgo_search][2]<br>
- GitHub Actions to update the Static Site Generator with new data each day

## Features:
- Searches and aggregates a number of news articles related to AI over the past day
- Summarizes the articles while providing links back to the source.


## ToDo:
- Aggregate similar articles based on title and body, generate one summary and attribute specific summary points to the respective source. (In some cases, 80% of the retrieved articles were about the same news item...)
- Archive past summaries
- Tag summaries for archival review.

## To Clone this Repo:
1. `git clone https://github.com/JoshM483/morningreport`
2. `git branch -a`
3. `git checkout <branch name>`

## To run the repo locally:
1. Install Ruby by using [this link][3] and follow the instructions for your system.
2. With Ruby installed you should be able to run `bundle` in your local project terminal.
3. If you get a message saying 'Bundle complete!' then you are good to go!
4. You can run `bundle exec jekyll serve` to run the Static Site Generator locally.
<br>

- If you make changes to the code and save the file, the SSG will rebuild the site and you can refresh the page to see the changes!
- You may occasionally need to clear the cache of the web page if the changes don't show up.


## Thanks for stopping by!

Feel free to reach out or contribute!


[1]: https://nicolas-van.github.io/bootstrap-4-github-pages/
[2]: https://github.com/deedy5/duckduckgo_search
[3]: https://www.ruby-lang.org/en/documentation/installation/