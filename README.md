# Django:rocket: template project with custom user

* Project core folder at root ```(django-admin startproject core .)```
* Settings managed by .env file:
    * python-dotenv module is integrated so secrets and environment specific settings can be stored in a untracked .env file
* User app inherit and is ready to extend Django default 'AbrstractUser' class in its models file (admin and forms files are ready too):
    *  no problems with migrations adding custom fields as needed!

### ToDo:

- [ ] add templates for user authentication
- [ ] add .env example file
