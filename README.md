# RSS Feed Reader

RSS Feed Reader is Web Applicatioin build using Django Framework and 'feedparser'. This application also deployed on Heroku. [Visit](http://rss-reader-interface.herokuapp.com/).
To know more about 'feedparser' and their licenses [visit](https://pypi.org/project/feedparser/)

#### Follow below steps to setup and run application:
Note: Below instructions works for Mac OS.

To setup these application Python 3.6 must have install in your system

1. Clone the repository.

2. Create virtual environment:-
    
    If virtualenv not install then install it as well or you can use another virtual environment manager. To install virtualenv 
    <pre>pip install virtualenv</pre>
    and then,
    <pre> virtualenv venv </pre>
    Then, activate virtual environment using -
    <pre> source venv/bin/activate </pre>

3. Install all requirements:-
    <pre>pip install -r requirements.txt</pre>

4. Move into project root folder and run the application using:-
    <pre>python manage.py runserver</pre>
    
    or
    
    [Click here](http://rss-reader-interface.herokuapp.com/) (http://rss-reader-interface.herokuapp.com/)

After running application you must have to provide URL to get RSS Feeds. The example URL is: http://feeds.bbci.co.uk/news/rss.xml
