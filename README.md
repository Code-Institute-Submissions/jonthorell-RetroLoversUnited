# RetroLoversUnited

The aim of this project is to create a community site for everyone that is as obessive with the classic Amiga-computer as I am.

The project is live 
[here](https://retroloversunited.herokuapp.com/)

![mockup-picture](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/mockup.PNG?raw=true?raw=true)

# Background and use-case

The project is for all intents and purposes a community site for that use or is interested in the old Amiga-line of computers.

Designated editors can create and edit articles that may or may not be commented on by ordinary users. Those comments must be approved by a moderator
before they are visible, to prevent spam comments. Users can always edit or delete their comment if they want to. The editors can likewise delete their
articles (although if they do that, the associated comments will be deleted as well).

Everyone can at any time delete their account, but the same caveat applies. Associated articles (in case user was an editor) and commments will
be deleted as well.

The screen is divided into three parts.

At the top,

![navbar](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/navbar.PNG?raw=true)

Authors and Categories are pop-down menues that will show shortcuts to all articles by a given editor, or articles
in a given category (i.e. Hardware). Contact, About, FAQ (essentially a "list" of vocabulary specific to the Amiga), & Credits
are always shown. Create Article, Admin, and List Active Users are shown depending on whether the logged in user has the right
to use the function.

The icon on the far right controls account related functions such as sign up, login, logout, edit profile, & delete account.

In the middle you have the main part where you can see list of articles, categories, and interact with them using forms. In this example, a list of articles
by author Amy Squirrel.

![middle-part](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/landing_page.PNG?raw=true)

And finally, at the bottom. A footer with copyright information and links to social media.

![footer](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/footer.png?raw=true)

# Design considerations (visual).

1. Colors and other graphical elements have been "stolen" or mimicked from AmigaOS as much as possible. 
2. The beachball at the top-left is a sort-of unofficial logo.
3. The grey background is the default background color of the GUI.
4. The navbar uses the same white as the AmigaOS menubar.
5. The black text is the default font-color.
6. The orange text comes from the "fuel-gauge" that indicates how full a disk is (from an earlier version of AmigaOS).
7. The black background and the blinking graphics on the 403 page is how the Amiga indicates it has run into a dead-end software failure.
8. The site should be fully responsive.

# Technologies used

1. HTML
2. CSS (with classes from MaterializeBootstrap as well as my own)
3. Javascript
4. Django
5. Python
6. Git (from within Visual Studio), pushed to GitHub. UserStories and Kanban board is also hosted at GitHub.
7. Postgres SQL

NOTE: timeline in Agileproject. Made an initial mistake there so had start over from scratch. The dates are therefor not necessarily completely accurate. Also, I probably should have set the different
iterations without due-dates. See further under lessons learned.

# Design considerations (code)

1. Since it is a django-project, configuation is done in settings.py, forms.py, & urls.py
2. The project consists of three apps. One main where the main logic takes place. And two subapps, faq and credits. Point one applies here as well.
3. The main code is in views.py and "scattered" in the django template files as well such as the articles_by_author file. In the latter case it stuff like this:
```django
{% if profile.user.is_active %}
{% endif %
```
4. Comments are used in both the python code and the template files. In the latter case, it is html-comments surrounded by the django comment-tags. The purpose for doing it twice is that the html-comment sticks out color-wise in the code editor and the django-tags make sure commens are not visible in view source.
5. Everything is based upon class-based views rather than being function based.

# Design considerations (user classes)

# User classes

Every user belongs to one or more classes of user. This is implemented using django groups.

1. Admin. Or superusers. They can do anything.
2. Editors. Has the ability to create new articles.
3. Members. Can comment on articles. Also needed to view profiles. When someone sign up, they are automatically added to this group.
4. Anonymous users (or not logged in users). Can view articles and comments but not able to comment themselves.
5. Managers. Can see all active and inactive users.

In the issues tracker, webuser is a not logged in user. User is a logged in user.

# Deployment

All coding takes place in Visual Studio and regularily pushed to the repo at GitHub. There are some "hidden" environmental variables in a file called env.py that is excluded from git
pushes. Those variables are used when running locally. The variables in question are:

* DATABASE_URL
* SECRET_KEY
* CLOUDINARY_URL
* EMAIL_HOST_PASSWORD
* EMAIL_HOST_USER

# Deployment to Heroku

In order to deploy something to Heroku, several steps needs to be taken care of.

This is taken for granted that the project is already hosted at GitHub.

Code changes are regularily pushed into that repository using either Visual Studio or the cli command git using:

1. git add .
2. git commit -m "commit message"
3. git push

The steps for deployment to Heroku are:

1. Create an account at Heroku.
2. Create an app in Heroku, with a unique name and a region
3. Under settings, create an environment variable with the name PORT and value of 8000. Duplicate the variables under deployment here as well.
4. In your development environment, do: pip freeze > requirements.txt to add the requirements needed to build the project at heroku.
Things installed, if any, locally will be added to the requirements file, to make sure everything necessary will be available when deployed.
This might include things not necessarily referenced, but it will make sure the build will be complete.
5. Make sure there's a file named Procfile in the root of your repo with this line: web: gunicorn retroloversunited.wsgi
6. Under deployment, connect the github account to the heroku-account
7. Under deployment method, connect the app to the correct github repository
8. Decide if you want the deployment to be automatic or manual. That is a matter of preference. For now, I have opted to make it manual.

# Database design

The different models works like this.

# Bugs encountered and fixed

1. Navbar did not list categories for all pages at first. Solved with a mixin to the class-based views
2. The code to retrieve categories from the database threw a "has no attributes" error. Turned out to be a name-mismatch since the name Category was used for a view as well.
Renaming the view name was not the same as the model name fixed the problem.
3. Problem finding a way of getting the group for the current user. The solution found is not as elegant as I would like, but it works.
4. Got error in devtools for two label lines. Turned out I had forgotten to remove them when the corresponding input field was removed.
5. Change chip in category to display right avatar and editor-name. DONE
6. Spacing issue between author and category menu. DONE
7. Ran into an issue where the view-category-by-category retrieved data from articles instead of categories. Had forgotten to change the Model as well as it was the wrong template type.
8. article-by-author tried to look up category instead of user-id. FIXED. Wrong model.
9. When using view-by-author, the system inexplicable logs the user in as that user??. Fixed. context_view was wrong
10. Faq gets same value from links.description all the time?? Fixed
11. Modal did not close properly on mobile. Seems duplicated ids were responsible, but the browser on the PC was more forgiving. Changed to pop-out instead
12. If user manually changes article id in url bar for editarticle, the display is empty. Works good enough to get the form into place and look into that problem later. Fixed.
13. In edit_article, the kwarg-value was empty when the get-method was available. It worked fine when the get-method was commented-out. Which was a bit of a bummer since the kwarg-value was essential for the logic that checked whether the logged in user was authorized to edit it. Fixed.

## Remaining bugs

The categories and authors menues in some situations fails to display their content. Works in most cases but has not been able to find the root cause.

# Todo

1. Clean up css from redundant classes
2. Document models
3. Add comments wherever needed


# Other

1. Credits worked fines as is, but decided to move it and the FAQ to separate apps.
2. Code for pagination uses classes from Materialize Bootstrap.
3. Filter on status. Done in views.py for index. Can't do that for the others since it needs custom code in the template with if/else/for-loops
4. Articles in draft-mode will only be shown in "My articles". It is the only place where it makes sense to show it since no other editor should ever need to see it.

# Testing

Testing has been done manually in selecting the different menu entries, trying to get an unauthorized user getting the possibility to edit something, and trying to get user
A to be able to edit/delete something belonging to user B, among other things. Further details in subheadings but as a general rule I have not been able to trigger errors
of that sort but get the proper error message as expected.

## Lighthouse

One Lighthouse screenshot per view. In All cases Lighthouse complains about missing explicit size-tags (not surprising since it is in a header.html that in turn is included in base.html). However,
the error is misleading. The width and height attributes are set using css-classes which lighthouse does not pick up upon.

Lighthouse also complains about things I can not do much about without re-rewriting the front-end framework that is being used.

In this example for instance.

The buttons are created on the fly by the classname added. 

Index

![index](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/lighthouse/index.PNG?raw=true)

# Lessons learned

Setting deadlines on Agile milestones was not a good idea when you are new to both the Agile methodology and trying to learn the Django framework at the same time. Especially since I can not work
on the project full-time due to other things on my plate. Having just the user stories and the project board would have been sufficient.

As always, I tend to make the project too big in scope.



