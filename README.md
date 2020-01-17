# Django:rocket: template project with custom user

* Project core folder at root ```(django-admin startproject core .)```
* Settings managed by __.env__ file:
    * __python-dotenv__ module is integrated so _secrets_ and environment specific settings can be stored in a __untracked__ .env file
* User app inherits and is ready to extend Django default __AbstractUser__ class in its models file (admin and forms files are ready too):
    *  no problems with migrations adding custom fields as needed!

### ToDo:

- [x] add templates for user authentication
- [x] add .env example file
- [ ] add test
- [ ] add deploy configurations
- [ ] add first installation how to
