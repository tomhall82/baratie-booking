## Manual Testing

| Feature                                                                                                           | Expected Outcome                                                                                                                   | Testing Performed                                                                                                                                               | Result                                                                                                    | Pass/Fail |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------- |
| User can navigate to the home page  | User is re-directed to the home page | Baratie logo and Home clicked from various screens | User is re-directed to the home page | Pass |
| User can navigate to the menu page  | User is re-directed to the menu page | Menu clicked from various screens | User is re-directed to the menu page | Pass |
| User can navigate to the book a table page  | User is re-directed to the book a table page | Book a table clicked from various screens | User is re-directed to the book a table page | Pass |
| User is redirected to login page when clicking book a table if they are not already booked in  | User is re-directed to the login page | While signed out book a table clicked | User is re-directed to the login page | Pass |
| User is able to create an account  | User creates an account | Register clicked from various pages | User is re-directed to the account registration page and can create an account | Pass |
| User is able to create an login  | User logs into their account | Login clicked from various pages | User is re-directed to the login page and can log in to their account | Pass |
| User is able to sign out of their account  | User is asked to confirm they wish to sign out of their account and is signed out upon confirmation | Logout clicked from various pages | User is asked to confirm they wish to sign out of their account and is signed out upon confirmation | Pass |
| User can create a booking  | User can click book a table and create a booking | 10+ bookings made under a selection of different accounts | User can click book a table and create a booking | Pass |
| User can view their bookings  | User can click your bookings and view their bookings only | Multiple bookings made by different accounts to check they can only view their own bookings | User can click your bookings and view their bookings only | Pass |
| Staff user can view all bookings  | Staff user can click your bookings and view all bookings by all users | Staff account created to ensure they can view all bookings | Staff user can click your bookings and view all bookings by all users | Pass |
| User can edit their bookings  | User can click your bookings and edit their bookings only | Multiple bookings made by different accounts to check they can only edit their own bookings | User can click your bookings and edit their bookings only | Pass |
| Staff user can edit all bookings  | Staff user can click your bookings and edit all bookings by all users | Staff account created to ensure they can edit all bookings | Staff user can click your bookings and edit all bookings by all users | Pass |
| User can delete their bookings  | User can click your bookings and delete their bookings only | Multiple bookings made by different accounts to check they can only delete their own bookings | User can click your bookings and delete their bookings only | Pass |
| Staff user can delete all bookings  | Staff user can click your bookings and delete all bookings by all users | Staff account created to ensure they can delete all bookings | Staff user can click your bookings and delete all bookings by all users | Pass |
| All users are required to confirm deletion  | Once delete is clicked, all users are required to confirm they  wish to delete before entry is deleted | Delete clicked as staff and user to ensure confirmation is required | Once delete is clicked, all users are required to confirm they  wish to delete before entry is deleted | Pass |

## Negative Testing

Tests were performed on the create booking to ensure that:

1. A customer cannot book a date in the past.
1. A customer cannot book if the party size is less than one.
1. Forms cannot be submitted when required fields are empty.

## Unit Testing

Unit tests were created to test functionality such as correct data inputs and correct data being send and retrieved from the database. These can be found in the tests.py files in the respective apps.

Results:

![Unit tests](/docs/testing/baratie-unit-testing.png)

## Accessibility

[WAVE Web Accessibility Evaluation Tools](https://wave.webaim.org/) have been used to ensure site-wide accessibility.

Testing focused on the following areas and identified no issues:

- All forms have associated labels or aria-labels
- No colour contrast errors were detected.
- Heading levels are not missed or skipped.
- All none text content has alternative text or titles so descriptions are read out to screen readers.
- Aria properties are correctly implemented.

## Validator Testing

**HTML**

All pages have been run through the [W3C Markup Validation Service](https://validator.w3.org/). All pages have been validated with the exception of booking_edit.html. This is due to a known bug cuased due to the format the date and time are saved in being different from the format the fields wish to display the data as shown in the [Bugs](#bugs) section of this document.

Due to the django templating language code used in the HTML files, it is not possible to copy and paste into the validator. It is also not possible to validate by direct URI due to the secured views and pages which require logins. To test the validation on the files, open the page to validate, right click and view page source. This raw html code can then be copied and pasted into the validator to be tested.

![W3C Validator](/docs/testing/w3c-testing.png)

**CSS**

The custom CSS was validated using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) with no erros found.

![CSS Validation](/docs/testing/baratie-ws3-css.png)

**JavaScript**

![Baratie JS Hint](/docs/testing/baratie-js-hint.png)

**Python**

All python files have been run through the [CI Python Linter](https://pep8ci.herokuapp.com/) with no errors.

## Lighthouse

**Home**

**Menu**

**Book a table**

**Your bookings**

## Bugs

**Solved Bugs**

1. My database failed and would not allow me to POST or GET any data. This appeared to be due to a corrupted field. After an extended period of troubleshooting with both my mentor [Graeme Taylor](https://github.com/G-Taylor) and Code Institute tutors, the only solution identified was to delete that database and re-create it. Since doing so, the same issue has not been experienced.

**Known Bugs**

1. When editing a previously made booking, the date and time do not populate with the previously entered values. Upon further inspection this appears to be due to the format the data is saved in being different from the format the fields wish to display the data. Unfortunately, I have been unable to resolve this issue due to running out of time ahead of the submission deadline.
