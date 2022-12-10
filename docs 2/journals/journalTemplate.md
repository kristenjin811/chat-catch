Create a directory in your repository named journals. Then, create a new file named «your-name».md. The «your-name» part can be just your first name, unless there is more than one person on the team with the same first name. Make them unique.

In the journals, every day that you work on the project, you must make an entry in your journal after you've finished that day. At a minimum, you will need to include the following information:

* The date of the entry
* A list of features/issues that you worked on and who you worked with, if applicable
* A reflection on any design conversations that you had
* At least one ah-ha! moment that you had during your coding, however small

Keep your journal in reverse chronological order. Always put new entries at the top.

Here's a sample of the first two entries of someone's journal file.

## July 9, 2021

Today, I worked on:

* Getting a customer's data for the account page
  with Asa

Asa and I wrote some SQL. We tested it out with
Insomnia and the UI. We had to coordinate with
Petra who was working on the GHI with Azami.

Today, I found the F2/Rename symbol functionality
in Visual Studio Code! It allows me to rename a
variable without causing bugs. I am going to be
using this a lot!

## July 7, 2021

Today, I worked on:

* Signing up a customer with Petra

Petra and I had a hard time figuring out the logic
for what happens when a customer signs up. We
finally came to the conclusion that not only did we
have to create the `User` record, but we also needed
to create associated preference records **and** had
to log them in.

Today, database transactions finally clicked. It
happened while we were trying to insert the
preferences for the customer. We had a bug in the
code, so the `User` record got created, but none
of the preferences. All of the inserts should
succeed or fail together. So, we used a transaction
to do that.
