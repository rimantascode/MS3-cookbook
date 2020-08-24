# Recipes Website

Dynamic RECIPES WEBSITE with an interctive design which contains from fron-end and back-end giving the ability to add, edit, update, delete the recipes simply and easy, just filling the form, or modifyieng the form. It ueses mongoDB and written using Flask Micro Framework.
Hosted on [Heroku](https://rimantascode.github.io/Milestone-Project-2/)
Repository on [GitHub](https://github.com/rimantascode/Milestone-Project-2)

## License

The project is shared for use with the [GNU General Public License v3](https://github.com/Pattern-Projects/oireachtas-ifd-project/blob/master/LICENSE)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

# UX

![Responsive Views of Home Page](documents/responsiveness.png)

## User Stories

When the user lands in the page he sees all of the recipies added.

The user can use the navigation to filter the search results.

the search results are displayed in cards and contains two buttons - View The Recipe - and - Edit.

when the users click on View The Recipe in another page in detail. The requireded and the cooking instruktion will be desplayed. In the right bottom corner us a float button giving an apportunity ti delete, edit, or add a new recipe.

The users also are able to edit the existing recipe by clickig edit button straight on the card.

---

## Design

- The navigation was used from materialize website, as it functioning well on smaller devices and bigger screens.
- The layout of the main page consist of the picture area, in landing page it displayes the general picture with a lot of recipes on the page. When the recipee is viewed than the appropriate picture takes the place. The design like this is consistant and the user do not need to learn how to use it. Down below is a float botton to add the recipe and on the appoiste side share button to allow the user share the recipe in the Social Media.
- The next pannel has "Search Results", and this write uup channges in the name of the recipe, when the recipe is view in details. It keeps the information tidy for the user convieniance.
- Down below the recipes are displayed in the cards as search results. First I designed to be displayed a bit differently, but when I was looking through the **https://materializecss.com/** My attention atracted the cards, and I wanted to her used to **materialzess** features desiced to take the apportunitya and redisign it in my way. Also I believe that the picture is worth hundred of words, the size it is displayed make a good cence of the dish, and even the user might even feel hungry. The card it self contains easy diegestible, and usefull information in first glance which might lever the dicision to click the particular recipe.
- At the end of the page we have a footer with links to social media, about us page and contact us page.

- **About Us** simple page with a picture and some text about the cocmpany.
- **Contact Us** again the design of this page remains simple containing a form, and once it is filled up and meets the requirements can be submited and the user will get a feedback whether it was successfully sent or not.

* Colour scheme consists of few colours, was used website to blend the colors.
  ##############################################################################
  (https://meyerweb.com/eric/tools/color-blend/#:::hex)
  - ![#f7f7f7](https://placehold.it/15/f7f7f7/000000?text=+) `#f7f7f7`
  - ![#29a5e2](https://placehold.it/15/29a5e2/000000?text=+) `#29a5e2`
  - ![#666666](https://placehold.it/15/666666/000000?text=+) `#666666`
  - ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff`

## Typography

##############################################

- fonts used throughout the website
  - font-family: 'Oswald', sans-serif;

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
- Deployed - Hosted on Github Pages

### Existing Features

- Documentation - ReadMe File, Licence & Mockups
- Colour Scheme
- materializecss - HTML, CSS Framework
  - Grid System - Columns and Rows
- Responsive design - Mobile First
- UX elements
- Accesibility
- Gitpod - Version Control System
- GitHub - Remote Repository
- Deployed - Hosted on Github Pages

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

## Testing

### Manual Testing

- The first part of the page website choose your journey.

  1.  Hover over it has to apply the showdown underneath, by giving clear separation the section, all three sections behave that way.
  2.  click on hovered over a section, it will take to the map section and the markers will be dropped on the map accordingly. All. three sections behave the same.

- The second part is a map.

1 If the selection was not selected in choose your journey the map will load automatically Kingston with hotels. click on radio buttons and the map will be displaying selected city, also if you will click on Choose The Place "Restaurants", "Hotels", "Beaches" the markers will be displayed accordingly. If you will click on the marker the info window will appear with the information about the place, some places will display how much time left until it closes, if it is closed, the day when it will be open again will be displayed. Some of the places have not provided the relevant information so will be displayed some of information such as picture, place name, rating, phone number address, or "open/close time is not specified might appear on the window".
The information accuracy was tested by sending website links to my friend living in different countries no matter what country the information was displayed correctly, we could see the same closing in time or is closed or open.

- The third part is about us a brief description of the service.

- The third part id contacts us.

1. If you will try to submit the form by missing any of the inputs, a message will be displayed, telling what section has to be filled in, it also checks the inputted email address to make sure it has the "@" symbol.
2. Click submit, than the owner will recieve an email with all the details inputted, also "SUCCESS! 200 OK" will be logged out in th console telling the email was sent successfully. The email is sent by using Emailjs service.

- Fifth is a footer containing social links all of them opens in a new tab and are working, tested manually.

### Code Validation

To validate the my CSS and HTML code I used [https://validator.w3.org/](https://validator.w3.org/)

### Testing on Browsers

Tested on Google Chrome, Opera, Mozzilla firefox. No issues.

### Testing on Devices

Used Google Chrome, Opera, Mozila firefox browser to test the responsiveness, it flows good on any type of device.

## Deployment

The project is hosted on [GitHub Pages](https://rimantascode.github.io/Milestone-Project-2/)

The process involved:

- Host a git repository on GitHub. Explained [here](https://help.github.com/en/articles/create-a-repo).
- The root folder contains README.md and index.html files
- On GitHub repository settings page move to GitHub Pages section
- Change source to master branch. (Or any desired branch)
- Provided link will be your projects home (index) page.

To deploy your own version of the website:

- Have git installed
- Visit the [repository](https://github.com/rimantascode/Milestone-Project-2)
- Click 'Clone or download' and copy the code for http
- Open a terminal in your root directory
- Type 'git clone ' followed by the code taken from github repository
  - `https://github.com/rimantascode/Milestone-Project-2.git`
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

#### Thank you very much for all the source of high-quality quality pictures.

- Thank you [https://fshoq.com](https://fshoq.com/free-photos/p/167/woman-on-swing-caribbean-beach-and-sea) for a picture
- Thank you [www.pxfuel.com](https://www.pxfuel.com/en/free-photo-jlzhv) for a picture
- Thank you[https://pixabay.com/](https://pixabay.com/photos/jamaica-palm-trees-beach-1303880/) for a picture
- Thank you [https://pixabay.com/](https://pixabay.com/photos/woman-hike-lake-female-hiker-2896389/) for a picture
- Thank you [https://wikimedia.org/](https://upload.wikimedia.org/) even ehen the picture is no availble any more
- Thank you [https://www.flickr.com/](https://www.flickr.com/photos/bods/6062033422) for a picture.
- Thank you [https://commons.wikimedia.org](https://commons.wikimedia.org/wiki/File:The_Sognefjord.jpg) for a picture
- Thank you [https://www.flickr.com/](https://www.flickr.com/photos/paszczak000/4669043022) for a picture
- Thank you [https://www.flickr.com/](https://www.flickr.com/photos/redjunasun/5937648493) for a picture

### Acknowledgements

Thank you inspiration, very usefull guidence and tips:

- Seun Owonikoko @seun_mentor
- Code Institute
