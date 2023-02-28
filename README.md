# Job Bot

A bot to automately apply job for you. Work on indeed, angel.co, ... incoming monster

## Getting Started

Download the project and run the python script.

Example: run angel.py for angel.co website

### Prerequisites

chromedriver: For running Chrome(already included)

[geckodriver](https://github.com/mozilla/geckodriver/releases): For running Firefox

```
For Firefox:
Copy geckodirver into Project Folder

Change this line:
driver = webdriver.Chrome(options = options)

To:
driver = webdriver.Firefox()

```
Update cv.txt to your desire cover letter



## Authors

* **Huey Phan** - [ichomchom](https://github.com/ichomchom)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

# indeed.py: 
 on mac: 
1. open terminal

2. run: 

open -na "Google Chrome" --args --remote-debugging-port=9222

3. navigate to indeed.com 

4. log in 

5. clear job title and location 

6. run program