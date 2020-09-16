# Milestone Project 3


# Recipes Website

Dynamic RECIPES WEBSITE with an interctive design which contains from fron-end and back-end giving the ability to add, edit, update, delete the recipes simply and easy, just filling the form, or modifyieng the form. It ueses mongoDB and written using Flask Micro Framework, HTML5, CSS3, jQuery, Javascript
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

## The Aim.

 - The main aim was to create the recipes website with clearly desplayed and  - easily diegstible information. 

 - To create an easy menageble website with an functions such as add, edit and delete the recipes. 

 - Let the users to filter the result by clicking the navigation category.

 - Keep the recipes in sorted by the date when it was added so the users could see the newest recipes. 



## User Stories

User stories shaped my idea how to create this project. 

As a website owner,
I want to manage the recipes easily and quickly so that I would include the function like add, edit, or delete and opportunity to share the the new recipes in the social media with few clicks.  

As a visitor of the website, I am happy that the main information is displayed, and it easy to read.

As a person who is always thinking what to make for dinner,
I like to see what is possible to cook from the stuff in the fridge, so I would not need to run to the store. It is easy to navigate and find the recipe by the main ingredient: the type of the meat. 

As a user of the recipes websites, 
I do not like to read a lot, so big and clear picture gives me an impression what then dish would be like. 


---

## Dsign Proccess

1. **Strategy plane:** There are a  lot of recipes websites, but I wanted to create my own app which would be not overloaded with information, and have a unique design, because this project is B2C. And this a good opportunity to get more famiar with flask micro-framework. 
2. **Scope plane:** When I run through all ideas and user stories I started to realise how the website should look like and how the the recipes would have to be displayed for the users. It has to have a navigation bar at he top and which would have mobile responsive. The big picture of the main page and also big picture when the recipe would be seen in detail. The recipes would be displayed in the cards format, with sensitive information, such as how would it take to cook and how difficult it is, what ingredients will the user need in order to cook with add, edit and delete functions. The footer with the links to the social media about as and contact as form. I added the few more features in the end of project such as pagination and how old is the recipe in order to keep the newest visible first. 
3. **Structure plane:** So when the decision was made of what features I will need, started to group the features. The user will land in the main page or in one of the categories. Decided to have a header in in which would be navigation with the categories, the picture area in in the main page. The main picture with a lot of dishes on the table. Add button and share links beneath. And this part would stay the same all the time. Once clicked on of the categories the information from mongoDB would be pulled out and the results are displayed in the cards with appropriate information. In the cards they would be able go to add, edit, or dish pages.This type of design is ease learnable very easy to navigate no more than three click to reach the destination. 
4. **Skeleton plane:** Once the structure plane is in place,  started to put all together by using Figma. Added 5 categories of the main ingredients. The user can get the results only related to the category - the main ingredient. Add button takes the user to the add recipe page which consists of the header and a form, once filled up and meats all requirements can be submitted. When the visitor click on on the categories the cards appear( as you can see in the mock-up I changed the the size of the cards and how is the picture displayed). The user can see the picture on the left side of the card and the information on the right side. The name of the recipe ,the cooking time and the difficulty level is displayed and the majority of the ingredients required are also displayed. Down below three buttons delete, edit , and see the recipe in detail. Edit page will keep the same structure. The navigation, hero image add button and share links In place, but beneath there is a form which can be edited and the button update recipe. Once the button clicked the user will be taken to dish.html page to review the changes. In the dish page there is a float button with delete, edit, and add recipe functions to let the user do with the recipe what he wants straight way. 
5. **Surface plane:** When the skeleton plane was in place. Decided to do a research on what colours can make the people hungry? There were a lot of opinions, so narrowed down too much the colours. From Google fonts choose the fonts and finished the design. the footer took from materializesss and added the same color as navigatio. 

- **About Us** simple page with a picture and some text about the project.
- **Contact Us** the design of this page remains simple containing a form, and once it is filled up and meets the requirements can be submited and the user will get a feedback whether it was successfully sent or not.

* Colour scheme consists of few colours, was used website to blend the colors.
  ##############################################################################
  (https://meyerweb.com/eric/tools/color-blend/#:::hex)
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

- Fonts used throughout the website
font-family: "Permanent Marker", cursive
font-family: "Roboto", sans-serif

### Mockups

The website looks a litle bit deffrent than in the mockup. Does not contain the about us and contact us page as it is very simple and the struckture remained the same execp the form and a text in teh about us page.

- [Mockup](https://www.figma.com/file/qRXUafOtVvw52gEOa81RPL/Untitled?node-id=0%3A1)

## Features

Features planned, implemented and outlined for later development

### Planned Features

- Documentation - ReadMe File, Licence & Mockups
- Colour Scheme
- materializecss - HTML, CSS Framework
  - Grid System - Columns and Rows
- Responsive design - Mobile First
- Authentication
- Logo
- UX elements
- Accesibility
- Contact Form
- Git - Version Control System
- GitHub - Remote Repository
- Hosted - on Heroku
- Deployed - On Github. 

### Existing Features

- Documentation - ReadMe File, Licence & Mockups
- Displayes the period of time when the recipe was added
- Colour Scheme
- materializecss - HTML, CSS Framework
  - Grid System - Columns and Rows
- Responsive design - Mobile First
- UX elements
- Accesibility
- Gitpod - Version Control System
- GitHub - Remote Repository
- Hosted - on Heroku
- Deployed - On Github. 
- Age - tells how old is recipe.
- Pagination - added pagination for more convieant search and also it reduces page loading time.

### Features Left to Implement/fix

- Authentication
- custom logo

## Technologies Used 

This project makes use of:

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
  - **Google** was used for research, workm and testing responsiveness
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
- All the labraries including the flask micro Framework have to be installed. All of them is listed in the requirements.txt, how to install please see Deployment section.


### Manual Testing

- All the links work, tested by clicking manualy. 
- add button works, it once clicked it takes to Add Recipe page. 
- share links all works it is easy to share the website. 
- pagianton works, it desplays 4 recipes per page.
- The feature the time of period when the recipe was added works, and tested by adding a new recipe. 
- DELETE, EDIT, SEE buttons work on the card, tested manualy and takes to the correct page.
- links in footer work, takes to the correct pages.

### Code Validation

To validate my CSS and HTML code I used [https://validator.w3.org/](https://validator.w3.org/) 

To validate the PYTHON3 code [http://pep8online.com/ch/eckresult](http://pep8online.com/ch/eckresult) 


### Testing on Browsers

Tested on Google Chrome, Opera, Mozzilla firefox. No issues.

### Testing on Devices

Used Google Chrome, Opera, Mozila firefox browser to test the responsiveness, it flows good on any type of device.

## Deployment

The process involved:

- Host a git repository on GitHub. Explained [here](https://help.github.com/en/articles/create-a-repo).
- The root folder contains README.md and index.html files
- On GitHub repository settings page move to GitHub Pages section
- Change source to master branch. (Or any desired branch)
- Provided link will be your projects home (index) page.

To deploy your own version of the website:

- Open a terminal in your root directory
- Type 'git clone ' followed by the code taken from github repository
- `https://github.com/rimantascode/MS3-cookbook.git`
- You will need to install requirements.txt by typing in the terminal pip3 install -r requirements.txt

- When this completes you have your own version of the website
  - Feel free to make any changes to it
- The website can be run by opening one of the HTML files within a web browser
- Visit the link provided
- Your website with any made changes will appear
- Saved changes to the website will appear here after refreshing the page

The benefits of hosting your website on GitHub pages is that any pushed changes to your project will automatically update the website. Development branches can be created and merged to the master when complete.

It may take a moment for changes to appear on the hosted website.

## Credits

### Media


### Acknowledgements

Thank you inspiration, very usefull guidence and tips:

- Seun Owonikoko @seun_mentor
- Code Institute
