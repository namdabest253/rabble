HW 2 Comments Addressed:

I was unable to run your code since you haven't added pillow to the requirements.txt file. This is a dependency required by the ImageField attribute in your user.

In requirements.txt added line:
line 18: Pillow>=9.0

In general, it is preferable to use ModelAdmin classes when registering models because it allows for more customizability in the admin page.

In admin.py changed it to use ModelAdmin classes

HW3 Comments Addressed:

null = True (for a many to many field) causes a warning in django

In models.py changed admins attribute in Community model to a through table instead of a manytomany field attribute. So there isn't this warning anymore

rabble-fixture.json file has errors that prevent it from loading:
I was unable to load your fixture. The error I get is about a null value in "rabble.community" which is related to your user_id field. I also get an error about iterable type in "rabble.community" which expects your admins for a community to be a list

Deleted sqlite database, migrations and remade them with the updated models.py. Also deleted rabble-fixture.json and remade it with the new splite database and migrations.