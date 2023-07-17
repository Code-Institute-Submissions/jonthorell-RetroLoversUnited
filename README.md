NOTE: timeline in Agileproject. Made an initial mistake there so had start over from scratch. The dates are therefor not necessarily completely accurate

# Bugs

1. Navbar did not list categories for all pages at first. Solved with a mixin to the class-based views
2. Navbar catgories does not work from error pages
3. Problem finding a way of getting the group for the current user. The solution found is not as elegant as I would like, but it works.
4. Got error in devtools for two label lines. Turned out I had forgotten to remove them when the corresponding input field was removed.
5. Bell-drop down created an empty menu if there were no messages. Fixed by moving the ul-container.
6. Spacing issue between author and category menu. Not fixed yet.
7. Ran into an issue where the view-category-by-category retrieved data from articles instead of categories. Had forgotten to change the Model as well as it was the wrong template type.
8. article-by-author tried to look up category instead of user-id. FIXED. Wrong model.
9. When using view-by-author, the system inexplicable logs the user in as that user??
10. Faq gets same value from links.description all the time??
11. Modal did not close properly on mobile. Seems duplicated ids were responsible, but the browser on the PC was more forgiving.

# Todo

1. Clean up css from redundant classes
2. Document models
3. Add comments wherever needed
4. Chnage chip in category to display right avatar and editor-name. DONE
5. Add a credits view. Avatars needs to be added there apart from the rest. DONE

# Other

1. Credits works fine. Should be moved to separate app.
2. Code for pagination adapted from examples at: https://realpython.com/django-pagination/

# User classes

Every user belongs to one or more classes of user.

1. Admin. Or superusercs. They can do anything.
2. Editors. Has the ability to create new articles.
3. Members. Can comment on articles (and potentially like articles). Also needed to view profiles.
4. Anonymous users (or not logged in users). Can view articles and comments but not able to comment themselves.
5. Managers. Can see all active and inactive users.

In the issues tracker, webuser is a not logged in user. User is a logged in user.

Members is essentially everyone that is logged in. Admins is the designated superusers. Should also be a member of the editor group.
Editors are those users the admin has added to the editors group. If not a member of the editors group, the create article link disappears.

Bug: the code to retrieve categories from the database threw a "has no attributes" error. Turned out to be a name-mismatch since the name Category was used for a view as well.
Renaming the view name was not the same as the model name.

# Retro Lovers United

This is a site for dedicated users of the now very old Amiga-line of computers where they can get help, tips, and ideas of things to do with their beloved antiques.
Mostly just as a fun hobby, but maybe find some small niche where it can still be useful.

The site is written using HTML, CSS, Django, Python, and MD Bootstrap (Material Design Bootstrap)

# Main Page

When the site is launched, the screen is essentially divided into three parts.

![navbar](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/navbar.PNG?raw=true)

The navbar will of course always be visible no matter where you are on the page. The beachball on the far left takes you back to the homepage (the icon itself comes from the very first
demo released for the Amiga 1000 back in 1985 to showcase some of what it could do). Categories is a drop-down menu where you can choose which category of articles you want to view.
Contact and abouts are just links. Create Article and Admin will not be visible unless you are logged in with sufficient rights.

On the right hand side, the bell indicates whether you have unread notifications (for example, a comment has just been approved). It also acts as a drop-down menu. This icon will also not be shown if you
are not logged in.

The avatar finally will just show a generic one if you are not logged in. Depending on whether you are logged in or out, the menu it offers will offer you either:
* Create Account
* Login

Or:

* Logout

![landing-page](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/landing_page.PNG?raw=true)

The landing page is essentially just a welcome page, but with links to three latest articles added to the site.

![footer](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/footer.png?raw=true)

The copyright message in the footer will be hidden on smaller screens so the most important thing here is highlighted, the social media icons.
JUst a few that I deemed most suitable for a community site. The URLs for twitter and youtube are search strings into respective platform with
a relevant searchphrase. Github leads straight to this repository.
