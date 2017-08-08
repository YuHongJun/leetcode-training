
How will I complete this project?
This project is connected to the Programming Foundations with Python course, but depending on your background knowledge you may not need the entirety of the course to complete this project. Here's what you should do:

1. Install [Python](https://www.python.org/)

2. Create a data structure (i.e. a Python Class) to store your favorite movies, including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.

3. Create multiple instances of that Python Class to represent your favorite movies; group all the instances together in a list.

4. To help you generate a website that displays these movies, we have provided a starter code repository that contains a Python module called `fresh_tomatoes.py`.
 To get started, `fork` this [repository](https://github.com/udacity/ud036_StarterCode/blob/master/fresh_tomatoes.py) to create your own copy in GitHub.
 Then `clone` your `ud036_StarterCode` repository to work on this project locally on your computer.
 The `fresh_tomatoes.py` module has a function called `open_movies_page` that takes in one argument, which is a list of movies, and creates an HTML file which will display all of your favorite movies.
Ensure your website renders correctly when you attempt to load it in a browser.
Notes

The file `fresh_tomatoes.py` contains the `open_movies_page()` function that will take in your list of movies and generate an HTML file including this content, producing a website to showcase your favorite movies.

Your task is to write a movie class in `media.py`.
To do this, think about what the properties of a movie are that need to be encapsulated in a movie object such as movie titles, box art, poster images, and movie trailer URLs.
 Look at what `open_movies_page()` does with a list of movie objects for hints on how to design your movie class.

You’ll want to write a constructor for the movie class so that you can create instances of movie.
You can now create a list of these movie objects in `entertainment_center.py` by calling the constructor `media.Movie()` to instantiate movie objects. You’ve given movies their own custom data structure by defining the movie class and constructor, and now these objects can be stored in a list data structure. This list of movies is what the open_movies_page() function needs as input in order to build the HTML file, so you can display your website.
Project Evaluation
The project will be evaluated as either Meets Specifications or Does Not Meet Specifications scale. The rubric is broken into four major categories:

Functionality
Does your project work the way it's supposed to? Are movies and their poster images being displayed on the web page? Is there a trailer link? Does it open from the Python file error free?

Code Quality
Is your code organized and professional? If you need an idea of how to format and style your code to look organized and professional, check out the Google [Python Style Guide](https://google.github.io/styleguide/pyguide.html) and the [PEP-8 site](https://www.python.org/dev/peps/pep-0008/).

Because Python is sensitive to white space and indents, make sure that you follow the formatting rules found here.

Comments
Do you use comments to describe what is going on in your code? Would other developers be able to take a look at your code and easily be able to understand what your code is trying to do? A good starting point to see how to comment code would be to take a look at the comments section of the Google Python Style Guide.

Documentation
When submitting your project, be sure to include a README file detailing how a user is to run your project (how to open the movie trailer website).

Include information, such as, how do they get your code (download, etc.), are there any requirements? Are there any commands that need to be run in order to run your application?
If you've never written a README before, Udacity has produced a [short course](https://cn.udacity.com/course/writing-readmes--ud777) on how to write one effectively.