## Learning Django

Notes to review and ask questions about later...

```
// My Sandbox
Python: 2.7.2
Django: 1.6.3
```

### Commands

Commands I will likely forget!

#### Managing the Sandbox

Like `npm`, can isolate environments and have a concept of *local* and *global* packages

```
// create a new sandbox
$ virtualenv <ENV>

// play in it
$ cd <ENV> && source bin/activate

...

// leave the sandbox
$ deactivate
```

#### Running the Dev Server

Think `grunt serve`! *Some* fs changes are even watched!

```
// Start 'er up!
$ python manage.py runserver [port]
```

#### Flushing changes to DB

Uses information about your models to create db entities. (Yet another DB ORM).

```
// See the generated SQL (before)
$ python manage.py sql <app>

// Add/Mutate db
$ python manage.py syncdb
```

 > Note: Deprecated as of 1.7 in favor of `migrate` 
 
This handy abstraction uses the db config from `settings.py` to determine the SQL needed to write changes. SQL data type are inferred from the python models (eg; bool, decimal, etc) so...

 > **Q:** Will the python db ORM ever support NoSQL?
 
#### Play in an interactive shell

```
// start shell session
$ python manage.py shell

(InteractiveConsole)
>>>

// ....

>>> exit()
```
 
#### Scaffolding a new app

```
$ python manage.py startapp <app>
```

 > Note: app is conventionally a pluralized noun (polls, users, reviews)

### VirtualEnv

For sandboxing environments and packages! This is corollary to node's local-first and global stuff. Unlike node, global is default. To get sandboxes, the tool is called `virtualenv`. It is not shipped with python, but can be installed globally via `pip`

http://www.virtualenv.org/en/latest/virtualenv.html

When first creating a sandbox, the following directory structure is initialized:

```
env         // Sandbox
├── bin         // local env overrides PATH
├── include     // python header files
├── lib         // python libs
└── mysite      // django project
	├── manage.py   // CLI Hooks
	└── mysite      // main module[?]
	    ├── __init__.py     // identifies directory as a python package
	    ├── settings.py     // project-level settings
	    ├── urls.py         // Routing Table
	    └── wsgi.py         // for WSGI-compatible web servers
```

### PIP

The package manager. **Does this do smart satisfying of deps?** CLI syntax supports semver, but if I try to install an incompatible package, wthat does the package manager do for me?

```
// install something
$ pip install django

// List installed packages
$ pip freeze
```

### Django 

Fundamental terminology

 > **Projects vs. apps**
What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular Web site. A project can contain multiple apps. An app can be in multiple projects.

#### Projects

Webapps and websites. The top-level `mysite` directory. Django projects have an immediate child: `manage.py` file that helps with scaffolding (setting `PATH` vars, registerring the project's `settings.py`, etc.)

The `manage.py` and `django-admin.py` both provide CLI hooks to a number of project-level administrative tasks.

#### Apps

The building blocks of django projects. Django projects are typically composed of many narrowly-scoped and reusable apps *á la* the Unix Philosophy.  

 > **Q:** What delineates packages, modules, and apps?

### Django Admin

Think `phpmyadmin`.

### Django CLI

READ THIS: https://docs.djangoproject.com/en/dev/ref/django-admin/#django-admin-py-and-manage-py

```
// scaffold a new project 
$ django-admin.py startproject mysite

$ python manage.py runserver
```

## Potential Gotcha's

Misc pearls of wisdom and questions to spark conversation.

### Order matters 

Cannot reference vars before they are defined. 

```
// Okay
foo = 'foo'
bar = 'bar'
foobar = foo + bar

// Throws 'NameError'
bizzbuzz = bizz + buzz
bizz = 'bizz'
buss = 'buzz'
```

 > **Q:** Does this apply to functions (`callables`) as well?


### Re-using model behaviors in filters

 > **Q:** Is this possible?

```
class MyClass(models.Model):
    foo = models.CharField(max_length=120)
    def predicateMethod(self):
        if (...):
            return true
        else:
            return false

MyClass.objects.filter(predicateMethod=True)
```

How to keep behaviors DRY?

### Language Features

Python is prettier than PHP. Django is not unlike popular PHP MVC frameworks. (Regex-oritented routing, string templating, templating mini-languages {handlebars, twig, etc.}, PIP <==> Composer), PSR modules, PDO Active Record (which I hate) 
