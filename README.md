# The Baratie

This is a website for the fictional restaurant "The Baratie" which is featured in the anime One Piece.

![baratie-responsive-screenshots-from-am-i-responsive](/docs/images/baratie-am-i-responsive.png)

[Visit The Baratie](https://baratie-9bf2bc8ed0f8.herokuapp.com/)

## Contents

## User Experience (UX)

### Strategy

#### Site Goals

The aim of this site is to enable staff and customers to create, view, edit and delete bookings for the fictional restaurant "The Baratie". 

The site is also intended to give a breif overview oof the history of the restaraunt and show the menu.

#### Aglie Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out over four weeks.

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have. They were assigned to sprints and story pointed according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/users/tomhall82/projects/3/views/1) and can be viewed to see more information on the project cards.

![Baratie Kanban Board](/docs/images/baratie-kanban-board.png)

#### Epics & User Stories

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

**EPIC 3 - Booking**
- As a user, I would like to be able to create a new booking when I want to visit the restaurant.
- As a user, I would like to view my bookings to review the information.
- As a user, I would like to be able to edit a booking so that I can make changes as necessary.
- As a user I would like to delete a booking when no longer required.

**EPIC 4 - User Account**
- As a developer, I need to implement allauth so that users can sign up and have access to the websites features.
- As a Site User I can register an account so that I can book a table.

**EPIC 5 - Deployment**
- As a developer I need to deploy the project to heroku so that it is live for users

**EPIC 6 - Documentation**
- Create README.md
- Create TESTING.md

### Scope

The website should:
- Be responsive and fully functional across a variety of devices.
- Condense the navigation menu to a hamburger menu on devices with smaller screens.
- Allow authorised users to perform CRUD functionality on bookings.
- Allow authorised users to view only their bookings.
- Allow staff users to view all bookings.
- Have a home page with information about the restaraunt.

### Structure

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

* cloudinary==1.29.0 - Cloundinary was set up for use but no custom uploads were made, settings remain for future development
* crispy-bootstrap5==0.6 - This was used to allow bootstrap5 use with crispy forms
* cryptography==37.0.2 - Installed as dependency with another package
* defusedxml==0.7.1 - Installed as dependency with another package
* dj-database-url==0.5.0 - Used to parse database url for production environment
* dj3-cloudinary-storage==0.0.6 - Storage system to work with cloudinary
* Django==4.0.5 - Framework used to build the application
* django-admin-rangefilter==0.8.4 - This was used to search bookings in the admin for a range between 2 dates
* django-allauth==0.51.0 - Used for the sites authentication system, sign up, sign in, logout, password resets ect.
* django-crispy-forms==1.14.0 - Used to style the forms on render
* django-model-utils==4.2.0 - Installed as dependency with another package
* gunicorn==20.1.0 - Installed as dependency with another package
* idna==3.3 - Installed as dependency with another package
* oauthlib==3.2.0 - Installed as dependency with another package
* psycopg2==2.9.3 - Needed for heroku deployment
* pycparser==2.21 - Installed as dependency with another package
* PyJWT==2.4.0 - Installed as dependency with another package
* python3-openid==3.2.0 - Installed as dependency with another package
* requests==2.27.1 - Installed as dependency with another package
* requests-oauthlib==1.3.1 - Installed as dependency with another package (allauth authentication)
* six==1.16.0 - Installed as dependency with another package
* sqlparse==0.4.2 - Installed as dependency with another package
* tzdata==2022.1 - Installed as dependency with another package
* urllib3==1.26.9 - Installed as dependency with another package
* whitenoise==6.2.0 - Used to serve static files directly without use of static resource provider like cloundinary

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

-

### Media

-

### Troubleshooting & Reference Resources

- [django documentation](https://docs.djangoproject.com/en/4.2/)
- [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [stackoverflow](https://stackoverflow.com/)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/)

## Acknowledgments

- [Graeme Taylor](https://github.com/G-Taylor), my Code Institute mentor.
