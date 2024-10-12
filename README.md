# The Baratie

This is a website for the fictional restaurant "The Baratie" which is featured in the anime One Piece.

![baratie-responsive-screenshots-from-am-i-responsive](/docs/images/baratie-am-i-responsive.png)

[Visit The Baratie](https://baratie-9bf2bc8ed0f8.herokuapp.com/)

## Contents

## User Experience (UX)

## Strategy

#### Site Goals

The aim of this site is to enable staff and customers to create, view, edit and delete bookings for the fictional restaurant "The Baratie". 

The site is also intended to give a breif overview of the history of the restaraunt and show the menu.

#### Aglie Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out over four weeks.

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have. They were assigned to sprints and story pointed according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/users/tomhall82/projects/3/views/1) and can be viewed to see more information on the project cards.

![Baratie Kanban Board](/docs/images/baratie-kanban-board.png)

### Epics & User Stories

**EPIC 1 - Setup**
- As a developer, I need to set up the project so that it is ready to create the project.
- As a developer, I need to set up whitenoise so that my static files are included in deployment

**EPIC 2 - Core pages**
- As a developer I need to create "base.html" so that I have a platform to build all other pages from.
- As a developer I need to create "index.html" so users will take them to a landing page which gives infomation about the restaurant.
- As a developer I need to create "menu.html" so users will be able to view restaurant menu(s).
- As a developer I need to create "book.html" so users will be able to book a table at the restaurant.
- As a developer I need to create "booking_edit.html" so users will be able to edit their booking.
- As a developer I need to create "booking_success.html" so users will receive confirmation when they have successfully made their booking.
- As a developer, I need to implement a 403 error page to redirect unauthorised users to.
- As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist.
- As a developer, I need to implement a 500 error page to alert users when an internal server error occurs.

**EPIC 3 - Booking**
- As a user, I would like to be able to create a new booking when I want to visit the restaurant.
- As a user, I would like to view my bookings to review the information.
- As a user, I would like to be able to edit a booking so that I can make changes as necessary.
- As a developer I would like to offer feedback when incorrect data has been entered into booking fields.
- As a user I would like to delete a booking when no longer required.

**EPIC 4 - User Account**
- As a developer, I need to implement allauth so that users can sign up and have access to the websites features.
- As a Site User I can register an account so that I can book a table.

**EPIC 5 - Deployment**
- As a developer I need to deploy the project to heroku so that it is live for users

**EPIC 6 - Documentation**
- Create README.md
- Create TESTING.md

## Scope

The website should:
- Be responsive and fully functional across a variety of devices.
- Condense the navigation menu to a hamburger menu on devices with smaller screens.
- Allow authorised users to perform CRUD functionality on bookings.
- Allow authorised users to view only their bookings.
- Allow staff users to view all bookings.
- Have a home page with information about the restaraunt.

## Structure

### Features
- base.html features a navagation bar which will adapt to scree size and display different options depending if an authorised user if logged in.

Desktop display not logged in:

![Baratie nav bar not logged in](/docs/images/baratie-nav-bar.png)

Desktop display logged in:

![Baratie nav bar logged in](/docs/images/baratie-nav-bar-logged-in.png)

Mobile display:

![Baratie nav bar mobile](/docs/images/baratie-nav-bar-small.png)

- base.html also features a footer showing the developers name and year of development, along with social media links.

![Baratie footer](/docs/images/baratie-footer.png)

- The home page builds from base.html and contains details about the restaraunt along with a hero image showing the exterior of the establishment.

![Baratie home page](/docs/images/baratie-home.png)

- The menu page builds from base.html and provides information and images of the food on offer.

![Baratie menu](/docs/images/baratie-menu.png)

- The booking page builds from base.html and is only accessible if the user has logged in to an authorised account.

![Baratie booking page](/docs/images/baratie-booking-form.png)

- Following a successful booking you will be redirected to the booking success page which contains a link to take you back to browse the menu.

![Baratie booking success](/docs/images/baratie-booking-success.png)

- Should a field by filled in incorrectly (date in the past or a party of less than 1) and error toast will pop up and identify the error to the user.

![Baratie error toast](/docs/images/toast-error.png)

- Your bookings page is only available to users who have signed in with an authorised account. This page will only show bookings made by the currently logged in user, unless that user has a staff status.

Individual user:

![Baratie my bookings user](/docs/images/user-my-bookings.png)

Staff user:

![Baratie my bookings staff](/docs/images/staff-my-bookings.png)

- Delete booking confirmation to ensure user is certain before deleting their booking.

![Baratie confirm delete](/docs/images/baratie-confirm-delete.png)

- A pirate Favicon was implemented across all pages to make the site easy to identify from the users tabs. Of course this had to be the Jolly Roger.

![Baratie favicon](/docs/images/baratie-favicon.png)

**Error Pages**

- A 403 error page has been implemented to provide feedback to the user if they try to access unauthorized content.

![Baratie 403 page](/docs/images/baratie-403.png)

- A 404 page has been implemented and will display if a user navigates to a broken link.

![Baratie 403 page](/docs/images/baratie-404.png)

- A 500 error page has been displayed to notify users when an internal server error occurs. The message lets users know that the problem is at our end.

![Baratie 403 page](/docs/images/baratie-500.png)

### Future Development
- Refine bookings enable staff to allocate tables.
- Add functionality for staff to easily amend the menu.
- Limit restaurant and table capacity.

## Technolgies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to make the custom slider on the menu page change and the bootstrap date picker.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for various icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
- TinyPNG
  - This was used to compress the hero image for optimal load times

**Frameworks Used**

* Django - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

* Bootstrap - A framework for building responsive, mobile-first sites.

**Python Modules Used**

* Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete.
* Mixins (LoginRequiredMixin, UserPassesTestMixin) - Used to enforce login required on views and test user is authorized to perform actions.
* messages - Used to pass messages to the toasts to display feedback to the user upon actions.
* reverse_lazy - Used to provide a reversed URL as the url attribute of a generic class-based view.
* redirect - Used to redirect the user to a specified URL

**External Python Modules**

* cryptography==43.0.1 - Installed as dependency with another package
* defusedxml==0.7.1 - Installed as dependency with another package
* dj-database-url==0.5.0 - Used to parse database url for production environment
* Django==4.2.15 - Framework used to build the application
* django-allauth==0.57.2 - Used for the sites authentication system, sign up, sign in, logout, password resets ect.
* gunicorn==20.1.0 - Installed as dependency with another package
* idna==3.7 - Installed as dependency with another package
* oauthlib==3.2.2 - Installed as dependency with another package
* psycopg2==2.9.9 - Needed for heroku deployment
* pycparser==2.22 - Installed as dependency with another package
* PyJWT==2.9.0 - Installed as dependency with another package
* python3-openid==3.2.0 - Installed as dependency with another package
* requests==2.31.0 - Installed as dependency with another package
* requests-oauthlib==2.0.0 - Installed as dependency with another package (allauth authentication)
* six==1.16.0 - Installed as dependency with another package
* sqlparse==0.5.1 - Installed as dependency with another package
* tzdata==2024.1 - Installed as dependency with another package
* urllib3==2.2.1 - Installed as dependency with another package
* whitenoise==5.3.0 - Used to serve static files directly without use of static resource provider

## Testing

For a detailed overview of both manual and automated test cases and results, please refer to [TESTING.md](TESTING.md).

## Deployment & Local Development

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (The URL of your live database)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site](https://baratie-9bf2bc8ed0f8.herokuapp.com/)

### How to Fork

To fork the GitHub baratie-booking repository:

Log in (or sign up) to Github.
Go to the repository for this project, tomhall82/baratie-booking.
Click the Fork button in the top right corner.

### How to Clone

To clone the baratie-booking repository:

Log in (or sign up) to GitHub.
Go to the repository for this project, tomhall82/baratie-booking.
Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

The link to the repository can be found here - [https://github.com/tomhall82/baratie-booking](https://github.com/tomhall82/baratie-booking)

# Credits

## Credits

### Code Used

- This project was created using methods taught in the Code Institutes walkthrough project "I think therefore I blog"

### Content

- Content for the about section taken from [One Piece Wiki](https://onepiece.fandom.com/wiki/Baratie).
- Content for the menu taken from [Just One Cookbook](https://www.justonecookbook.com/).

### Media

- Images for the Baratie, Sanji, Zeff and booking success courtesy of [Netflix](https://www.netflix.com/gb/title/80217863).
- Anime images for error pages courtesy of the [One Piece anime](https://www.crunchyroll.com/series/GRMG8ZQZR/one-piece?srsltid=AfmBOoq0XlK7RIKkiMrkuW9X91aZ-p_7wly5kOzw_MXmjcrIawXui04t) created by Oda Sensei.

### Troubleshooting & Reference Resources

- [django documentation](https://docs.djangoproject.com/en/4.2/)
- [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [stackoverflow](https://stackoverflow.com/)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/)

## Acknowledgments

- [Graeme Taylor](https://github.com/G-Taylor), my Code Institute mentor.
