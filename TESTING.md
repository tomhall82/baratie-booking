## Manual Testing

| Feature                                                                                                           | Expected Outcome                                                                                                                   | Testing Performed                                                                                                                                               | Result                                                                                                    | Pass/Fail |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------- |
| Press enter to begin game                                                                                         | Game begins                                                                                                                        | Game launched and multiple keys pressed including enter                                                                                                         | Game begins                                                                                               | Pass      |
| Category selection                                                                                                | User enters "music" and the game launches using a word from the music category                                                     | Multiple tests selecting the music category with a print function to show the word generated so this could be cross referenced against the relevant word file   | Game launched with a word from the music category each time                                               | Pass      |
| Category selection                                                                                                | User enters "cars" and the game launches using a word from the cars category                                                       | Multiple tests selecting the cars category with a print function to show the word generated so this could be cross referenced against the relevant word file    | Game launched with a word from the cars category each time                                                | Pass      |
| Category selection                                                                                                | User enters "animals" and the game launches using a word from the animals category                                                 | Multiple tests selecting the animals category with a print function to show the word generated so this could be cross referenced against the relevant word file | Game launched with a word from the animals category each time                                             | Pass      |
| Category selection                                                                                                | User enters something other than "music", "cars" or "animals" and an error message is generated                                    | Multiple tests inputing various incorrect combinations of letters, numbers and special characters                                                               | User is shown an error message and asked to input another choice                                          | Pass      |
| Game reveals correct guesses                                                                                      | When the correct letter is guessed, this letter is revealed within the secret word                                                 | Using a print statement to show the correct answer both correct and incorrect guesses used as input                                                             | When a correct letter was entered the letter appeared in the secret word                                  | Pass      |
| Lose 1 life and figure appearing in gallows by one stage for incorrect letters guessed                            | When an incorrect letter is guessed, 1 life is deducted and a single stage added to the figure in the gallows.                     | Using a print statement to show the correct answer both correct and incorrect letters used as input                                                             | When an incorrect letter was entered the lives reduced by 1 and figure in the gallows reacted as expected | Pass      |
| Lose 2 lives and figure appearing in gallows by two stages for incorrect words guessed                            | When an incorrect word is guessed, 2 lives are deducted and two stages added to the figure in the gallows.                         | Using a print statement to show the correct answer both correct and incorrect words used as input                                                               | When an incorrect word was entered the lives reduced by 2 and figure in the gallows reacted as expected   | Pass      |
| Game logs previous guesses                                                                                        | When the a letter or word is guessed, it is logged in "Previous guesses"                                                           | Game played to monitor guesses to ensure they are logged correctly                                                                                              | All previous guesses, both letters and words logged                                                       | Pass      |
| Win game if correct answer is entered in its entirety                                                             | If the correct answer is entered in its entirety the game ends with the user winning                                               | Using a print statement to show the correct answer the answer was entered in its entirety as the first answer and after both correct and incorrect guesses.     | When the correct answer is entered in its entirety the user wins                                          | Pass      |
| Prompt if the same letter or word is entered twice                                                                | Prompt to guess again if the user enters a word or full answer that they have guessed previously                                   | Both correct and incorrect letters and words entered in multiple play throughs                                                                                  | Prompt came up everytime a letter or word was duplicated                                                  | Pass      |
| Game ends when lives reach zero and figure appears in gallows                                                     | Game ends when lives reach zero and figure appears in gallows                                                                      | Using a print statement to show the correct answer, incorrect guesses were entered as both letters and full words to cause losses                               | Game ended when lives reached zero and figure is fully displayed in gallows                               | Pass      |
| Win or loss screen displays as necessary showing the hidden word and asking user if they would like to play again | Loss or victory screen shows complete with a revealed secret word at the end of the game. User then given the option to play again | Played 10+ games to test                                                                                                                                        | Correct screen appeared after each win or loss and the option to play again is presented                  | Pass      |
| Play game function takes you to the category selection screen if Y is input                                       | If Y is entered when asked to play again then user is taken back to category selection                                             | 10+ games played to test                                                                                                                                        | Directed to category selection when Y was entered following play again prompt on every attempt            | Pass      |
| Play game function takes you to the thank you selection screen if N is input                                      | If N is entered when asked to play again then user is taken the thank you screen                                                   | 10+ games played to test                                                                                                                                        | Directed to thank you screen when N was entered following play again prompt on every attempt              | Pass      |
| Press enter to continue on thank you screen                                                                       | User is prompted to press enter on thank you screen to return to main menu                                                         | 10+ games played to test                                                                                                                                        | Once enter key is pressed, user is returned to main menu                                                  | Pass      |

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

All pages have been run through the [W3C Markup Validation Service](https://validator.w3.org/). All pages have been validated with the exception of booking_edit.html. This is due to a known bug cuased due to the format the date and time are saved in being different from the format the fields wish to display the data as shown in the [Bugs](#bugs) section of this document.

Due to the django templating language code used in the HTML files, it is not possible to copy and paste into the validator. It is also not possible to validate by direct URI due to the secured views and pages which require logins. To test the validation on the files, open the page to validate, right click and view page source. This raw html code can then be copied and pasted into the validator to be tested.

![W3C Validator](/docs/testing/w3c-testing.png)

## Lighthouse

## Bugs

**Solved Bugs**

1. My database failed and would not allow me to POST or GET any data. This appeared to be due to a corrupted field. After an extended period of troubleshooting with both my mentor [Graeme Taylor](https://github.com/G-Taylor) and Code Institute tutors, the only solution identified was to delete that database and re-create it. Since doing so, the same issue has not been experienced.

**Known Bugs**

1. When editing a previously made booking, the date and time do not populate with the previously entered values. Upon further inspection this appears to be due to the format the data is saved in being different from the format the fields wish to display the data. Unfortunately, I have been unable to resolve this issue due to running out of time ahead of the submission deadline.
