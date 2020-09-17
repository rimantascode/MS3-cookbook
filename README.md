# Milestone Project 3


# No-Hunger  

Dynamic recipes with an interactive design that consists of front-end and back-end with the abilities to add, edit, update, delete the recipes simple and easy, just filling the form, or modifying the form. It uses MongoDB and written using Flask Micro Framework, HTML5, CSS3, jQuery, Javascript
Hosted on [Heroku](https://cookbook-ms3.herokuapp.com/)
Repository on [GitHub](https://github.com/rimantascode/MS3-cookbook)

## License

The project is shared for use with the [GNU General Public License v3](https://github.com/Pattern-Projects/oireachtas-ifd-project/blob/master/LICENSE)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

# UX

![Responsive Views of Home Page](source/responsive.png)


## User Stories

User stories shaped my idea of how to create this project. 

As a website owner,
I want to manage the recipes easily and quickly so that I would include the function like add, edit, or delete and opportunity to share the new recipes in the social media with few clicks.  

As a visitor of the website, I am happy that the main information is displayed, and it easy to read.

As a person who is always thinking about what to make for dinner,
I like to see what is possible to cook from the stuff in the fridge, so I would not need to run to the store. It is easy to navigate and find the recipe by the main ingredient: the type of meat. 

As a user of the recipes websites, 
I do not like to read a lot, so a big and clear picture gives me an impression of what then the dish would be like. 


---

## Design Process

1. **Strategy plane:** There are a  lot of recipes websites, but I wanted to create my own app which would be not overloaded with information, and have a unique design. This project is B2C. Plus that was a good opportunity to get more familiar with the flask micro-framework. 
2. **Scope plane:** When I run through all ideas and user stories I began to realize how the website should look and how the recipes would have to be displayed for the users. It has to have a navigation bar at the top and which would have mobile responsive. The big picture in the main page and also the big picture when the recipe will be seen in detail. The recipes would be displayed in the format of the cards, with sensitive information, such as how long would it take to cook and how difficult it is, what the ingredients will the user need in order to cook. And the buttons with add, edit, and delete functions. The footer with the links to the social media about as and contact us form. I added a few more features at the end of the project such as pagination and how old is the recipe in order to keep the newest visible first. 
3. **Structure plane:** So when the decision was made of what features I will need, started to group the features. The user will land on the main page or in one of the categories. Decided to have a header in which would be navigation with the categories, the picture area on the main page. The main picture with a lot of dishes on the table. Add button and share links beneath. This part would stay the same all the time. Once clicked on of the categories the information from MongoDB would be pulled out and displayed in the cards with appropriate information. In the cards, they would be able to go to add, edit, or dish pages. This type of design is very easy to navigate no more than three clicks to reach the destination, and it easy learnable.
4. **Skeleton plane:** Once the structure plane was in place started to put all together using Figma. Added 5 categories of the main ingredients. The user can get the results only related to the category - the main ingredient. Add button takes the user to the add recipe page which consists of the header and a form, once filled up and meats all requirements can be submitted. When the visitor clicks on the categories the cards appear( as you can see in the mock-up I changed the size of the cards and how is the picture displayed). The user can see the picture on the left side of the card and the information on the right side. The name of the recipe, the cooking time, and the difficulty level is displayed and the majority of the ingredients required are also displayed. Down below three buttons delete, edit, and see the recipe in detail. The Edit page will keep the same structure - the navigation, hero image add button, and share links In place, but beneath there is a form that can be edited and the button update recipe. Once the button clicked the user will be taken to the dish.html page to review the changes. In the dish page there is a floating button with delete, edit, and add recipe functions to let the user do with the recipe what he wants straightway. 
5. **Surface plane:** When the skeleton plane was in place. Decided to do a research on what colors can make the people hungry? There were a lot of opinions, so narrowed down too much the colors. From Google fonts choice the fonts and finished the design. the footer took from materializecss and made the same color as navigation. 

- **About Us** simple page with a picture and some text about the project.
- **Contact Us** the design of this page remains simple containing a form, and once it is filled up and meets the requirements can be submitted and the user will get feedback whether it was successfully sent or not.

## color Scheme

- ![#f7f7f7](https://placehold.it/15/f7f7f7/000000?text=+) `#f7f7f7`
- ![#964600](https://placehold.it/15/964600/000000?text=+) `#964600`
- ![#666666](https://placehold.it/15/666666/000000?text=+) `#666666`
- ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff`
- ![#f5f5dc](https://placehold.it/15/f5f5dc/000000?text=+) `#f5f5dc`
- ![#ff9900](https://placehold.it/15/ff9900/000000?text=+) `#ff9900`
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) `red`
- ![#edebeb](https://placehold.it/15/edebeb/000000?text=+) `#edebeb`
- ![#000000](https://placehold.it/15/000000/000000?text=+) `black`
- ![#008464 ](https://placehold.it/15/008464/000000?text=+) `#008464`
- ![#0761afb3](https://placehold.it/15/0761afb3/000000?text=+) `#0761afb3`
- ![#ec373780](https://placehold.it/15/ec373780/000000?text=+) `#ec373780`
- ![#6aa6ed](https://placehold.it/15/6aa6ed/000000?text=+) `#6aa6ed`
- ![#f44336](https://placehold.it/15/f44336/000000?text=+) `materializecss red class`
- ![#26a69a](https://placehold.it/15/26a69a/000000?text=+) `materializecss lighten-2 class`
- ![#4CAF50](https://placehold.it/15/4CAF50/000000?text=+) `materializecss green class`

## Typography

- Fonts used throughout the website.
font-family: "Permanent Marker", cursive.
font-family: "Roboto", sans-serif.

### Mockup

The website is a little bit different than in the mockup. Does not contain the about us and contact us pages as it is very simple, and the structure remained the same except the form and a text.

- [Mockup](https://www.figma.com/file/qRXUafOtVvw52gEOa81RPL/Untitled?node-id=0%3A1)

## Features

Features planned, implemented, and outlined for later development.

### Planned Features

- Documentation - ReadMe File, Licence & Mockups.
- Colour Scheme.
- materializecss - HTML, CSS Framework.
  - Grid System - Columns and Rows.
- Responsive design - Mobile First.
- Authentication.
- Logo.
- UX elements.
- Accessibility.
- Contact Form
- Git - Version Control System
- GitHub - Remote Repository
- Hosted - on Heroku
- Deployed - On Github. 

### Existing Features

- Documentation - ReadMe File, Licence & Mockups.
- Display the period of time when the recipe was added.
- Colour Scheme.
- materializecss - HTML, CSS Framework.
  - Grid System - Columns and Rows.
- Responsive design - Mobile First.
- UX elements.
- Accessibility.
- Gitpod - Version Control System.
- GitHub - Remote Repository.
- Hosted - on Heroku.
- Deployed - On Github. 
- Pagination - added pagination for more convenient search and also it reduces the loading time of the page.- Counts the letters in the title to make sure the people enter more descriptive titles. - Sweet Alert - it asks for confirmation to delete the recipe.  

### Features Left to Implement/fix

- Authentication
- custom logo

## Technologies Used.

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - **HTML** for strucutre
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - **CSS** for Styling
- [JavaScript](https://simple.wikipedia.org/wiki/JavaScript)
  - **JS** for creating dynamic functions, manipulating google places api.
- [jQuery](https://en.wikipedia.org/wiki/JQuery)
  - **jQuery** very usefull for traversing and events handeling
- [Google Chrome](https://www.google.com/chrome/)
  - Used for browsing and dev tools
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new)
  - Used for browsing and testing responsiveness.
- [Google](https://www.google.com/)
  - **Google** was used for research, work and testing responsiveness
- [materializecss.com](https://materializecss.com/)
  - HTML and CSS Framework from **materializecss.com v1.0.0 ** and **jQuery code**
- [Gitpod](https://www.gitpod.io/)
  - **Git** used for Version Control
- [GitHub](https://github.com/)
  - Repository hosted on **GitHub**
- [Heroku](https://dashboard.heroku.com/apps)
  - Website hosted on **Github Pages**
- [Am I Responsive](http://ami.responsivedesign.is)
  - Testing responsiveness of the website **Am I Responsive**
- [Figma](https://www.figma.com/)
  - used to make a mockup
- All the libraries including the flask micro Framework have to be installed. All of them are listed in the requirements.txt, how to install please see the **Deployment** section.


### Manual Testing

- All the links work, tested by clicking manually. 
- add button works, it once clicked it takes to the Add Recipe page. 
- share links all work, it is easy to share the website. 
- pagination works, it displays 4 recipes per page.
- The feature the time of period when the recipe was added works and tested by adding a new recipe. 
- DELETE, EDIT, SEE buttons work on the card, tested manually, and takes to the correct page, plus adds edits, and deletes.
- links in footer work, take to the correct pages.
- The contact form works, please see what time the screenshots were taken.
- [before-sent](source/before-sent.png)
- [after-sent](source/before-sent.png)
- [mail-box](source/mail-box.png)

### Code Validation

To validate my CSS and HTML code I used [https://validator.w3.org/](https://validator.w3.org/) 

To validate the PYTHON3 code [http://pep8online.com/ch/eckresult](http://pep8online.com/ch/eckresult) 


### Testing on Browsers

Tested on Google Chrome, Opera, Mozilla firefox. No issues.

### Testing on Devices

Used Google Chrome, Opera, Mozilla Firefox browser to test the responsiveness, it flows well on any type of device.

## Deployment

The process involved:

- In this project, you have to use Code institute template [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Click the green button "use this template" 
- How to create a new repository [here](https://docs.github.com/en/enterprise/2.15/user/articles/create-a-repo) , but in this case enter the title of the project, the description, choose privet or poblic, and click create repository from template. 
- On the GitHub repository settings page move to GitHub Pages section
- Change source to master branch. (Or any desired branch)

- Once the workspace is ready:
- In the terminal, in your root directory
- Type 'git clone ' followed by the code taken from the GitHub repository
- `https://github.com/rimantascode/MS3-cookbook.git`
- for example `git clone https://github.com/rimantascode/MS3-cookbook.git`
- Select all files and move out of the folder MS3-cookbook into the root directory. 
- Install requirements.txt by typing in the terminal 
- `pip3 install -r requirements.txt`

- create the database in [mongoDB](https://www.mongodb.com/) as it shown in the picture. cook_book is a database, and categories, difficulty, prep_time, recipe are the collections.
- ![mongoDB structure](source/mongoDB.png)

- create an enviroment variable in gitpod settings,[gitod settings](https://gitpod.io/settings/)

- ![Environment Variable](source/MONGO_URI.jpg)
- value is equel:
mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority
- Organization/Repository: is your GitHub **username**
- Also you need to create the **SECRET_KEY** environment variables value can be anything just do **not** do simple, like 1234 
- ![SECRET_KEY](source/SECRET_KEY.jpg)

#### IMPORT COLLECTIONS INTO mongoDB

- Now we need to import the data into the collections.
- Type in the terminal

- `mongoimport --uri mongodb+srv://<USERNAME>:<PASSWORD>@<cluster_name>/<DATABASE> --collection categories --type json --file categories.json`

- `mongoimport --uri mongodb+srv://<USERNAME>:<PASSWORD>@<cluster_name>/<DATABASE> --collection difficulty --type json --file difficulty.json`

- `mongoimport --uri mongodb+srv://<USERNAME>:<PASSWORD>@<cluster_name>/<DATABASE> --collection prep_time --type json --file prep_time.json`

- `mongoimport --uri mongodb+srv://<USERNAME>:<PASSWORD>@<cluster_name>/<DATABASE> --collection recipe --type json --file recipes.json`

- Type in the terminal
- `python3 app.py`
- click on the blue button to open in the browser.
- It is ready to use. 

- Feel free to make any changes to it.
- Your website with any made changes will appear.
- Saved changes in gitpod and to the website will appear after refreshing the page.


## Deploy to Heroku

- You have to create a new app in [Heroku](https://dashboard.heroku.com/new-app)
- give a unique name and choose a region to Europe.
- a gave the name of the app "testing-deploymenta" for testing porpuse.
- Click on Settings, and then the button "Reveal Config Vars".
- Enter MONGU_URI with the value you used to create environment variable.
- Enter SECRET_key with value you used to create environment variable.
- PORT value is 5000.
- IP value is 0.0.0.0.
- in the terminal
- `heroku login -i` , and enter the credentials.
- In the terminal, go to deploy section you will see the line similar to this.
- `heroku git:remote -a testing-deploymenta`
- create requirements.txt
- `pip3 freeze > requirements.txt`
- create Prockfile with a capital "P" this is a requirement.
- ` echo web: python app.py > Procfile`- and then `git add . ` and `git commit -m"added requirements.txt and Prock files" `
- `git push heroku master`
- once it has been pushed, in the terminal.
- `heroku ps:scale web=1`
- ready to use.
- ` heroku open`


## Credits
- Thank you.
- [Waitrose.com](https://www.waitrose.com/content/waitrose/en/home/recipes/recipe_directory/b/breaded_chicken_andwatercresssalad.html#_) - used the recipes, and the pictures for learnign and demonstrative porposes only. Once the project will be assested all data will be deleted.

- Thank you.
- [css tricks](https://css-tricks.com/line-clampin/) for a piece of code made to look my text very nice faded out.
Thank you.
- [photo](https://www.flickr.com/photos/dennis/102679650
https://live.staticflickr.com/32/102679650_cd10235c8f_k_d.jpg) for very nice picture.)


### Acknowledgements

Thank you inspiration, very usefull guidence and tips:

- Seun Owonikoko @seun_mentor
- Code Institute