# References

HW1:
https://stackoverflow.com/questions/35363194/how-do-i-use-the-spacing-utility-classes-in-bootstrap?utm_source=chatgpt.com
https://www.w3schools.com/django/ref_tags_if.php

HW2:
Manually Wrote:
User, Community, subRabble, Post, Comment, Conversation, Follow

Prompts used:
"what is the difference between blank and null in this:
preferred_name = models.TextField(blank=True, null=True)"

"explain this error: It is impossible to add a non-nullable field 'timestamp' to user without specifying a default. This is because the database needs something to populate existing rows."

"what does on_delete=models.CASCADE mean"

"what are the parameters for ForeignKey"

"how do i know that a class already has its own django id"

"how do i make a model have a foreign key to itself?"

"how do i make it so my admin page shows the models i've created?"

HW3:
Used AI to Write these models:
PostLike, CommentLike

Prompts used:
"what does pk stand for in this:
path("!<slug:identifier>/<int:pk>/", views.post_detail, name="post-detail"),"

"can you explain wat this error means: Reverse for 'post-detail' with arguments '('', 1)' not found. 1 pattern(s) tried: ['!(?P<identifier>[-a-zA-Z0-9_]+)/(?P<pk>[0-9]+)/\\Z']"

"the only community foreign key i have in subrabble is community_id which is its primary key and is a self incrementing number. how do I find the community_id from the community_indentifier"

"in my community i want to have multiple admins how do I do that "

"do i need to do this for the users key in community too? because a user can be in N communities and communities can have M users"

"should the User class have a foreign key to pretty much every other class?"

"so as a reference a class should only have a foreign key to another class if it's owned by that class?"

"would likes have to be its own entity to keep track of user likes?"

"why is my {% if user.id == post.account_id %} condition never true?"
