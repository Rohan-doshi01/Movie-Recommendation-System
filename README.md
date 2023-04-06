# MOVIE RECOMMENDATION SYSTEM

This application provides all the details of the requested movie such as overview, genre, release date, rating, runtime, top cast, reviews, recommended movies, etc.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using `beautifulsoup4` and performed sentiment analysis on those reviews.

### IMPLEMENTATION
![ezgif com-video-to-gif](https://user-images.githubusercontent.com/107804985/230385726-fb95797a-e596-44d8-a1a4-29e273235f93.gif)


<!-- 
Don't worry if the movie that you are looking for is not auto-suggested. Just type the movie name and click on "enter". You will be good to go even though if you made some typo errors. -->

## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the `API` link in your account settings and fill all the details to apply for API key. You will see the API key in your `API` sidebar once your request is approved.

## How to run the project?

1. Install all the libraries mentioned in the [requirements.txt] with the command `pip install -r requirements.txt`.
2. Replace YOUR_API_KEY in **both** the places (line no. 23 and 43) of `static/recommend.js` file.
3. Open your terminal/command prompt from your project directory and run the following lines of codes
  a.  `py -m venv env`
  b.  `env/Scripts/activate`
  c.  `py main.py`
4. The project should now be running at `http://127.0.0.1:5000/` in the browser.

### Sources of the datasets 

1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)
