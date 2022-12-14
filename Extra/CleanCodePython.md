---
title: "Clean Code with Python"
author: [Martin Czygan]
date: "October 2020"
subject: "Python, Clean Code"
keywords: [Python, Clean Code]
subtitle: "A 1-day tour through techniques, projects and examples, customized for Honda Research Institute Europe"
lang: "en"
titlepage: true,
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "360049"
titlepage-rule-height: 0
titlepage-background: "background.pdf"
...

# Clean Code with Python

> A 1-day tour through techniques, projects and examples.

![](static/instacode-120441.png){width=50%}

* Author: Martin Czygan, <mailto:mczygan@grossweber.com>
* Date and Location: October 2020, Remote

## About the Instructor

* software developer, currently working in [Leipzig](https://www.ub.uni-leipzig.de/) and [San Francisco](https://archive.org/)
* using Python since around 2006
* co-wrote a [book on Pandas](https://www.packtpub.com/product/getting-started-with-python-data-analysis/9781785285110) (2015), [DBLP](https://dblp.org/search?q=martin%20czygan)
* [workshops](https://github.com/miku/workshops) on various topics (Python, Go, Git and data processing)
* co-host of a [programming language user group in Leipzig](https://golangleipzig.space/)
* stack overflow [contributor](https://stackoverflow.com/users/89391) (answering Python questions, mostly)
* open source contributor ([https://github.com/miku](https://github.com/miku))

Over the years I worked with various languages and could observe various
communities and their approach to software development.

# Clean Code Principles

## Introduction

* more and more software is written
* it is easy to create what is called *a mess*
* an unhealthy code base costs time, money, slows down, demotivates and
  ultimately impacts productivity

### Sidenote: Classic software failures

* projects go over budget
* companies spend millions and end up nowhere
* bad software causes fatalities, impacts revenue, and can pose generic risks,
  e.g. security incidents

A 2015 article in IEEE spectrum:

* [Transistor Production Has Reached Astronomical Scales](https://spectrum.ieee.org/computing/hardware/transistor-production-has-reached-astronomical-scales)

Every second of 2014, on average 8 trillion transistors were produced. It is
some software that will run on these.

Robert C. Martin motivation: Let us cleanup ourselves before we are going to be
hit by regulation.

* we are living in the age of data, so here's a quip on data and code:

> Code ages like fish, data ages like wine.

## What is clean code?

Before we dive in, what is our take?

* Please, go to the pad and answer in one sentence, or keywords:

> Question: How would you describe clean code? Which properties would it have?


----

### Answers from participants

![](static/d1b2pad.png)

* easy to understand and maintain
* being able to understand whats done where and easily (more or less) find a specific postion which does X 

> consistent structure, comments on what is done 

* readable/understandable, commented, easy usable
* organized, documented, tested; easy to "read"
* understandable, maintainable, reusable, tested 
* Clean code is a piece of artwork that won't cause trouble soon :)
* Readable, maintainable, well documented, 

> Easily readable and understandable

* Short, structured and easy to understand for any user (also from other field)
* Does not get lost in structure 
* Easy to see bugs or also warning if inputs are not correct or missing (fail fast)
* Each line can be understood from looking at the immediate surrounding code
* No dead code (throw away eveyrthing which does not spark joy) :D
* Modular
* uncluttered interfaces
* traceable bugs

> Elegant 

* Commented :-) (Smart and efficient)
* Something that reusable (oneself after some time as well as others)
* not error-prone and robust
* Consistent (e.g., not switching between camelcase and using underscores for variable names)
* Core that can be enhanced easily / with fair amount of effort without rewritting everything
* Something, that doesn't make you feel bad at  first sight

> short functions

* good variable and function names
* use of programming patterns
* clean code starts with good folder structure

----

### What other people say

The Book let's a few people speak.

> I like my code to be elegant and efficient. The
logic should be straightforward to make it hard for bugs to hide, the
dependencies minimal to ease maintenance, error handling complete according to
an articulated strategy, and performance close to optimal so as not to tempt
people to make the code messy with unprincipled optimizations.

> **Clean code does one thing well.** -- Bjarne Stroustrup

> Clean code is simple and direct. Clean code
**reads like well-written prose**. Clean code never obscures the designer's intent
but rather is full of crisp abstractions and straightforward lines of control.
-- Grady Booch

This emphasis of readability relates to *Readability counts.* from the Zen of
Python.


> Clean code can be read, and **enhanced** by a
developer other than its original author. It has **unit and acceptance tests**.
It has **meaningful names**. It provides **one way** rather than many ways for
doing one thing. It has **minimal dependencies**, which are explicitly defined,
and provides a clear and minimal API. Code should be literate since depending
on the language, not all necessary information can be expressed clearly in code
alone. -- Dave Thomas

> I could list all of the qualities that I notice in
clean code, but there is one overarching quality that leads to all of them.
**Clean code always looks like it was written by someone who cares**. There is
nothing obvious that you can do to make it better. All of those things were
thought about by the code’s author, and if you try to imagine improvements,
you’re led back to where you are, sitting in appreciation of the code someone
left for you—code left by some- one who cares deeply about the craft. --
Michael Feathers

> You know you are working on clean code when each
routine you read turns out to be **pretty much what you expected**. You can call it
beautiful code when the code also makes it look like the language was made for
the problem. -- Ward Cunningham

### Software Engineering and Programming

Software engineering has been described as programming over time, subjected to
deadlines.

* Boy scout rule: Leave the campground cleaner than you found it

Imagine checking code in, that is a tiny bit cleaner, more streamlined, better
documented, with fewer bugs than at checkout time. Code would only get better.

## Coding Guidelines

* I remember a time, when coding styles were something special. There was
  Checkstyle for Java (first released in 2001).
* Around the same time PEP8 was created (on 05-Jul-2001).

> PEP stands for Python Enhancement Proposal; The first PEP, PEP1, describes the process.

> A PEP is a design document providing information to the Python community, or
> describing a new feature for Python or its processes or environment.

Over 500 PEP has been suggested since then (PEPs are numbered, although with gaps).

Other notable PEPs are:

* [PEP 20 -- The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
* [PEP 257 -- Docstring conventions](https://www.python.org/dev/peps/pep-0257/)
* [PEP 3000 -- Python 3000](https://www.python.org/dev/peps/pep-3000/)


### PEP 8 -- Style Guide for Python Code

> One of Guido's key insights is that code is read much more often than it is
> written. The guidelines provided here are intended to improve the readability
> of code and make it consistent across the wide spectrum of Python code.

Every rule has exceptions.

> However, **know when to be inconsistent** -- sometimes style guide
> recommendations just aren't applicable. **When in doubt, use your best
> judgment**. Look at other examples and decide what looks best. And don't
> hesitate to ask!

### PEP8 condensed

#### Layout

* use 4 spaces (tabs, however, increase accessible e.g. for visually impaired programmers)
* indent consistently (Python 3 disallows mixing the use of tabs and spaces for indentation)

You can go further by using a tool like
[editorconfig](https://editorconfig.org/) to communicate a standard.

* continuation alignment ([examples](https://www.python.org/dev/peps/pep-0008/#indentation))
* maximum of 79 chars per line, and use continuation to break up lines or backslashes (note: I've seen this rule ignored often)
* lines should break before a binary operator ([example](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator))
* blank lines: 2 around classes and top level functions; one around methods; sparingly inside functions
* code should be written in UTF-8
* imports should be on separate lines
  ([example](https://www.python.org/dev/peps/pep-0008/#imports)), and always on
top of the file; in the best case they follow an order (stdlib, 3rd-party,
local).

> There is a tool called [isort](https://github.com/PyCQA/isort) that allows
> you to sort imports.

```python
$ cat unsorted.py
import re
import csv
import pandas as pd

```

Check the ordering.

```shell
 isort -c unsorted.py
ERROR: ... Snippets/SortImports/unsorted.py
    Imports are incorrectly sorted and/or formatted.
```

Dry run with `-d` flag:

```shell
$ isort -d unsorted.py
import csv
import re

import pandas as pd
```

* prefer absolute imports and simple package layouts
* put "module level dunder" names after docstring, before imports (except future special import)

#### String Quotes

* both single and double quotes are allowed, use consistently

#### Whitespace

* various considerations around whitespace; [examples](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements)

#### Trailing commas

```python
FILES = ('setup.cfg',)
```

It would be syntactically correct to remote the parentheses, but they are left
for clarity.

In lists, the last value can (and should) have a comma, too:

```python
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
```

#### Comments

> Comments that contradict the code are worse than no comments. Always make a
> priority of keeping the comments up-to-date when the code changes!

That is both an important and hard rule to follow. You have to think about
documentation as something equally important as code. It helps to **re-read** code
and fix issue incrementally.

----

Sidenote: Motivation and Documentation

Armin Ronacher, a long time active member of the Python community remarked that
documentation should look good. So good, that you want to write more of it, or
make it even clearer. There are a couple of documentation framework that can
help with that.

----

> Comments should be complete sentences. The first word should be capitalized,
> unless it is an identifier that begins with a lower case letter.

----

Sidenote: Comments and documentation can be a topic of discussion.

More than once I heard:

> Nobody will use my code, I do not need comments.

True, and often realistic. But is it enough to skip it altogether? Maybe you
are working on different project and after two years you come back to old,
undocumented code - your code can get foreign (even to yourself) soon.

I think there are reasons to skip e.g. documentation entirely, you want a
throwaway prototype or something similar.

----

* no inline comments, unless specific

```python
x = x + 1                 # Increment x
```

Comments can distract, but might add context.

```
x = x + 1                 # Compensate for border
```

### Other

PEP8 talks about names, and as they are important, let's move them to a
separate section.

## Naming Conventions

Let's first pin down a few general prinicples.

We name variables, functions, classes, modules, packages. Good names ease
understanding, less good names obstruct, or even mislead. Remember that code is
read 90% of the time, so considering sensible names is important.

### Reveal your intent

The following code snippet does not reveal its intent.

```python
def get_it():
    list1 = []
    for x in the_list:
        if x % 4 == 0:
            list1.append(x)
    return list1
```

* *implicity* of code
* the zen of python states (line 2): explicit is better then implicit

Trying to be explicit is an act of communication.

### Distinct names

* you will find fewer of these names in Python, but
  `XYZControllerForEfficientHandlingOfStrings`,
`XYZControllerForEfficientStorageOfStrings` are not distinct enough

### Meaningful distinctions

It happens that you have more of one thing and you end up with variable names
like: `a1`, `a2` and so on.

Typically, there is a better way to write this by grouping similar items in a
container like list or dictionary.

```python
transforms = [a, b, c]
```

What has been `a1` will become `a[0]` and so on.


----

Sidenote: Intents

* read own code and other peoples code
* good variable names make comments obsolete
* use constructs with intent

As an example for intent, sometimes you can choose between a list and tuple. A
tuple signals immutability to a reader, while functionally using a list or tuple
might be equivalent.

You can use a list and check, if an element is already in there. But Python has
a built-in `set` data type that conveys this exact meaning.

A program can have an exit code (e.g. important when used in scripts). It is a
fine detail, but these exit codes can convey meaning (some programs, e.g. like
wget use a range of exit codes that you can quickly lookup, which is helpful for
debugging).

Example: [Snippets/Unique/unique.py](Snippets/Unique/unique.py)

----

### Avoid noise

Other languages (e.g. Go) are being explicit about this, although Python has a
more flexible import system.

```python
class Product:

    def __init__(self):
        self.product_info = {}
        self.product_data = {}

product = Product()
product.product_info # XXX: too noisy
...
```

Noise slows us down. Imaging you encounter two classes, e.g.:

* Customer
* CustomerObject

Which one do you choose? Every decision we open up to the reader to figure out
him or herself can be a potential time sink as the reader needs to establish
the context first, by reading code, reading documentation, asking a colleague
and so on. Something that should have taken a minute, takes hours or days.

### Use pronouncable names

* `modymdhms` is hard to spell out and (without autocomplete) easy to get wrong

### Use searchable names

Code is read more often that it is written and finding relevant code is important.

* Rule: The length of a name should correspond to the size of its scope

When using the command line, `grep -r` and `ack` are your friends.

### Avoid mental mapping

We see this over and over again: clean code relates to reducing the *cognitive load*.

----

> But programmers are smart and juggle many things in their head at any point in time, no?

> Yes, they are and do. But clarity is king.

----

* a name that does not need a (semantic) translation reduces cognitive load

### Don't be cute

* since you can use any name, why not spice up names

```python
def make_me_a_sandwich(user):
    """ Grants user admin privileges. """
    ...
```

* do not do it, keep it boring, `set_admin_privileges(user)`.

### Use one word per concept

* fetch, retrieve, get - what is the difference?
* you are again making the reader think (which you want, but also do not want)
* if I see method names using fetch, retrieve and get used for similar things,
  I will start to try to understand what exactly this difference is made of -
which takes away time

Other examples:

* controller, manager, driver
* transform, process, modify, ...


### Use solution domain names

There will usually be a specific technical term, that has

```python
def enqueue_task(task):
    ...

def handle_websockets(conn):
    ...

def dfs(node):
    ...
```

### Use problem domain names

When no technical term fits the bill, names from the problem domain should be used.

```
def edge_detect(img):
    ...
```

## Naming Conventions according to PEP8

In the context of PEP8.

* aspirational, should be considered, but ok to miss, when code exists that
  follows a different style

### Regarding noise

> The X11 library uses a leading X for all its public functions. In Python,
> this style is generally deemed unnecessary because attribute and method names
> are prefixed with an object, and function names are prefixed with a module
> name.

```python
import os

if os.path.exists("filename"):
    pass
```

An exception is `os.stat` which returns (the C equivalent of a) namedtuple
(PyStructSequence); here all fields are prefixed by `st_`, e.g. `st_mode`,
`st_size` (see: [https://git.io/JUbO5](https://git.io/JUbO5)).

### Names to avoid

Single character variables names:

* `l`, `O`, `I`

### Module names should be short

Excluding some files, there are about 800 python files in the Python distribution.

<!-- find . -name "*py" | grep -v "lib2to3" | grep -v "test_" | grep -v "/test"
| grep -v "__init__.py" | wc -l -->

* around 20% of the module names have an underscore in it (see sample)

```shell
mac_greek.py
text_file.py
import_diagnostics.py
mac_croatian.py
build_scripts.py
popen_fork.py
iso8859_14.py
find_max_nesting.py
iso8859_2.py
asdl_highlight.py
```

### Class Names

* should use the `CapWords` convention

### Exceptions

* should be written with `CapWords` as classed, but have `Error` appended
* Example: `ClassificationError`

### Global variable names

* try to avoid them; the can make reasoning about functions that use them much harder

If you use them on a module level, use the `__all__` mechanism to explicitly
name exported names.

### Function and variable names

> Function names should be lowercase, with words separated by underscores as
> necessary to improve readability.

> Variable names follow the same convention as function names.

> mixedCase is allowed only in contexts where that's already the prevailing
> style (e.g. threading.py), to retain backwards compatibility.

### Function and method arguments

> Always use **self** for the first argument to instance methods.

> Always use **cls** for the first argument to class methods.


### Instance variables

* use a leading underscore only to for non-public methods and instance variables
* there are not visibility modifiers in Python, so access will still be possible

### Constants

* typically `ALL_UPPERCASE`

### Design for inheritance

Some ideas to keep in mind in context of object oriented programming.

* start with non-public methods, if unsure; as a public API might mean commitment
* or otherwise make clear that an API is not fixed yet

Attribute access.

> For simple public data attributes, it is best to expose just the attribute
> name, without complicated accessor/mutator methods.

* keep functional aspect (e.g. via properties) side-effect free
* no computationally expensive operation in a property (the attribute access
  signals a relatively fast operation)

Try to design classes to be subclasses in a way, that reduces the need to hide
data to a minimum. There is a name-mangling rule in Python.

```python
class A:
    def __init__(self):
        self.name = "any"
        self.lang = "python"

class M:
    def __init__(self):
        self.__name = "any"
        self.__lang = "python"

class B(A):
    def hello(self):
        print(self.name)

class C(M):
    def hello(self):
        print(self.__name)

b = B()
c = C()

b.hello()
# c.hello() # AttributeError
```

### Private and public interfaces

> To better support introspection, modules should explicitly declare the names
> in their public API using the `__all__` attribute. Setting `__all__` to an
> empty list indicates that the module has no public API.

## Clean Code rules and principles

Care in small things will add up. Ergonomically, it might be easier to focus on
a little improvement at a time.

Some guiding principles:

* write small functions
* use descriptive names
* use boolean flags as little as possible
* minimize side effects
* do one thing
* do not repeat yourself

----

Sidenote: A Python snippet from the web

![](static/PythonLido.png)

* [Snippets/Lido/lido2schema.py](Snippets/Lido/lido2schema.py)

Again, use the etherpad.

> Question: Name a few issue with this code.

You can read the code here as well:

* https://gist.github.com/miku/dce655ebbfb7218760af4c8c60f47629#file-example-py-L93-L133
* https://git.io/JUNMr

----

## SOLID Principles

Principles for design. Managing dependencies (between components) - how change
propagates to a system. There can be similar concerns expressed for data (e.g.
dependencies of data artifacts).

### Single Responsibility Principle (SRP)

* SRP: a class should have one and only one reason to change - reported in
  Philosophy of Software Design as a typical error (e.g. HTTP request library)

### Open/closed principle (OCP)

* you should be able to extend a class's behaviour without modifying; a
  compositional pattern

Typically done by subclassing a base class.

* we extend the behaviour
* we reuse methods of the superclass
* the superclass is completely unaware of its subclasses

If the superclass changes its behaviour, it will affect the subclasses.

* another way is to extract interfaces and supply different implementations
* an interface is declarative, does not supply implementation and hence subclasses will not be coupled to a specific superclass implementation detail

In Python, explicit interfaces are rarely seen.

* You can define a class to be subclassed and provide no implementation.

Example: [Snippets/AbstractClass](Snippets/AbstractClass/abstract.py)

The standard library supports the implementation of a number of standard
interfaces in the
[collections.abc](https://docs.python.org/3/library/collections.abc.html)
module.

### Liskov substitution principle (LSP)

* Objects of a superclass shall be replaceable with objects of its subclasses
  without breaking the application.

Example of a not following this rule: [Liskov](Snippets/Liskov/broken.py)

### Interface Segregation Principle (ISG)

* No client should be forced to depend on method it does not use ()
* keep interfaces small

In Python, we have duck-typing. You can pass any object to a function, as long
as it "responds" to a method, it satisfies an *informal* interface.

* Example: [Reader](Snippets/Reader/reader.py)

### Dependency Inversion Principle (DIP)

* High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. interfaces).
* Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

A typical design approach is bottom-up: Write lower level components first, then
build abstractions on top of them, directly. This can lead to coupling, as a lower level module might not easily changed.

By introducing an abstraction, a user and provider of functionality can be
decoupled.

* Example: [DependencyInversion](Snippets/DependencyInversion/main.py)

Note: Dependency Injection is a debated topic in Python. [Why is IoC / DI not
common in
Python?](https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python).

Quoting James Shore:

> "Dependency Injection" is a 25-dollar term for a 5-cent concept. [...]
> Dependency injection means giving an object its instance variables. 

## Generic rules

* KISS (keep it simple, solid), aka "flintstoning"
* DRY (don't repeat yourself)
* YAGNI (you ain't gonna need it)
* Composition over inheritance (example: logging module in standard library)
* Readability counts (Line seven of Zen of Python) 
* The rule of three 
* Principle of least surprise


A small, but effective tweak.

![](static/nesting.png)

The rule spelled out:

> Let the happy path flow down the left hand edge.

If necessary invert conditions to keep reduce indent.

```python
if json_obj is not None:
    authors = json_obj.get("author")
    if authors is not None:
        for author in authors:
            orcid = self.om.normalise(author.get("ORCID"))
            if orcid is not None:
                result.add(orcid)

```

----

Task: Apply the "happy path" rule to the snippet above.

* [https://github.com/opencitations/index/commit/09af4a174c0a6dbcf4a838550b5ad558fc3dcee6](https://github.com/opencitations/index/commit/09af4a174c0a6dbcf4a838550b5ad558fc3dcee6)


## Patterns and anti-patterns in Python

Patterns and anti-patterns.

### Avoid global

A global variable can potentially be altered from many places and can complicate
code comprehension.

* avoid the `global` keyword

----

Sidenote: On a higher level, the essay/paper "Out of the tar pit" (2006) talks
about common problems in software construction.

One key observation is that state, and keeping track of state.

> The biggest problem in the development and maintenance of large-scale software
> systems is complexity — large systems are hard to understand. We believe that
> the major contributor to this complexity in many systems is the handling
> of state and the burden that this adds when trying to analyse and reason about
> the system.


----

### Avoid mutable default values

A source of bugs is the following snippet:

```python
def fun(a=1, b=[]):
    b.append("x")
    print(b)


fun()
fun()
```


The alternative is to use `None` as a default:

```python
def fun(a=1, b=None):
    if b is None:
        b = []
    b.append("x")
    print(b)
```

### EAFP

Python believes that it is *easier to ask for forgiveness than permission* (or EAFP for short).

Example:

```python
data = {
    "a": 1, 
    "b": 2,
}

# Works, LBYL style (https://docs.python.org/3/glossary.html#term-lbyl)
if data.has_key("a"):
    v = data["a"]
else:
    do_something_else()

# Better, following EAFP (https://docs.python.org/3/glossary.html#term-eafp)
try:
    v = data["a"]
except KeyError:
    do_something_else()
```

### Classes vs functions

* OOD and OOP emphasize classes (and some languages require them)
* Python is a "multi-paradigm" langauge
* Talk by Jack Dietrich: ["Stop writing classes"](https://www.youtube.com/watch?v=o9pEzgHorH0) (reducing hundreds of lines to a few dozens) 


## Test automation and test-driven development

* a school of programming favors a test first approach (or TDD)
* the basic idea: write a failing test first, then write code to make it pass (and only to make it pass)

Example: [Snippets/TestDriven/test_example.py](Snippets/TestDriven/test_example.py)

## Refactoring tools

* typically supported by IDEs, such as PyCharm
* rename, invert boolean, ...

## Code metrics

* tokei; sloccount
* pylint

## Detecting fragile code

* cyclomatic complexity

## Balanced Toolset

More tools:

* pyflakes
* mypy and type hints

Examples:

* [Snippets/Mypy/account_dynamic.py](Snippets/Mypy/account_dynamic.py)
* [Snippets/Mypy/account_static.py](Snippets/Mypy/account_static.py)
* [Snippets/Mypy/freq_dynamic.py](Snippets/Mypy/freq_dynamic.py)
* [Snippets/Mypy/freq_static.py](Snippets/Mypy/freq_static.py)

```
$ mypy Snippets/Mypy/hints.py 
Success: no issues found in 1 source file
``` 

* pycodestyle (formerly pep8)

Example output:

```python
$ pycodestyle --first siskin
siskin/__init__.py:43:80: E501 line too long (80 > 79 characters)
siskin/conversions.py:136:24: E741 ambiguous variable name 'l'
siskin/mab.py:168:12: E713 test for membership should be 'not in'
siskin/mappings.py:82:1: E265 block comment should start with '# '
siskin/test_arguments.py:52:27: E711 comparison to None should be 'if cond is None:'
siskin/test_utils.py:140:26: E712 comparison to True should be 'if cond is True:' or 'if cond:'
siskin/utils.py:96:9: E731 do not assign a lambda expression, use a def
siskin/utils.py:566:29: W605 invalid escape sequence '\d'
siskin/assets/161/161_marcbinary.py:27:5: E722 do not use bare 'except'
siskin/assets/101/101_marcbinary.py:60:15: W291 trailing whitespace
siskin/assets/183/183_marcxml_sru.py:100:72: E262 inline comment should start with '# '
```

Enforcing code styles.

* black
* yapf

The latter can be configured.

```
$ cat .style.yapf
[style]

based_on_style = pep8
split_before_logical_operator = true
column_limit = 160
```

## Elements of agile programming

Agile programming tries to take on a different perspective on software
development, shifting emphasis.

* Individuals and interactions over processes and tools
* Working software over comprehensive documentation
* Customer collaboration over contract negotiation
* Responding to change over following a plan

Value feedback and everything that allows you to collect feedback more easily.

----

Sidenote: A way to get to feedback.

Working on a plugin project for a application, that was slowly loading. Every
invocation (e.g. manual test) required to wait about ten seconds and would
involve a couple more manual steps. Doable, but annoying.

Solution: Factor out the bare minimum to execute the code (e.g. the plugin
loader) plus add some preloading.

Result: feedback time went from a minute to two seconds, development speed and
motivation did not decline.

----

## Learning from successful open source projects

* reading popular source repositories
* reading the standard library

Open source has various pragmatic aspects:

* time constrained development
* a wide range of contributions (developers of various levels, code,
  documentation, bug reports, pull requests, ...)

## Deconstructing complex code

* no single approach
* start or extend documentation
* extract (common) functions
* extract shared code into an independent library
* if they do not exist, write tests for functions
* try to find existing libraries that implement functionality

----

# Code Organization and Continous Integration (CI)

## Structuring Python Projects

* python code can be a short single file (with standard library only)
* modules and packages

### Code Walkthrough: Package miniretry

The miniretry package is a minimal package and demonstrates a project skeleton
and the code, publish and install cycle.

* [Repository](https://github.com/miku/miniretry)
* [PyPI](https://pypi.org/project/miniretry/)

## Virtual environments

* motivation: separate projects and their dependencies

> a self-contained directory tree that contains a Python installation for a
> particular version of Python, plus a number of additional packages

### Basic Usage

```python
$ apt-get install python3-venv
$ python3 -m venv example
$ tree example
$ tree -d example -I "__pycache__"
example
├── bin
├── include
├── lib
│   └── python3.6
│       └── site-packages
│           ├── pip
│           │   ├── commands
│           │   ├── compat
│           │   ├── models
│           │   ├── operations
│           │   ├── req
│           │   ├── utils
│           │   ├── vcs
│           │   └── _vendor
│           ├── pip-9.0.1.dist-info
│           ├── pkg_resources
│           │   ├── extern
│           │   └── _vendor
│           │       └── packaging
│           ├── pkg_resources-0.0.0.dist-info
│           ├── setuptools
│           │   ├── command
│           │   ├── extern
│           │   └── _vendor
│           │       └── packaging
│           └── setuptools-39.0.1.dist-info
├── lib64 -> lib
└── share
    └── python-wheels

29 directories
```

Activation:

```python
$ source example/bin/activate
(example) $
$ which python
[...]/example/bin/python
```

Deactivate:

```python
(example) $ deactivate
$
```

### Virtualenv Helper Scripts

* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) is a convenience layer

It needs to be source in the shell startup script, which make a few scripts
available, like `mkvirtualenv`, `rmvirtualenv` or `workon` to switch between
environment.:

### Using Conda

* [docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

```python
$ conda create --name myenv
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/tir/anaconda3/envs/myenv



Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate myenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```


## Collaboration with git

* the branch-review-merge workflow

A few intermediate aspects of git:

* [gitbits](https://github.com/miku/gitbits)


### Working with hooks

* [commitlint](https://commitlint.js.org/)
* check lint results before committing, reject commit if source code got worse (e.g. require 7/10 or 8/10)
* static check, e.g. via mypy, again, reject commits on failures

## Git and gitlab CI

* gitlab is an open source git repository hosting and CI platfrom
* many CI as a service solutions are available 
* automation potential around testing and deployment

### Example scenario

A python library, that is tested on every commit and deployed on every tag. A
local PyPI conform mirror (e.g. via [Nexus
OSS](https://www.sonatype.com/nexus/repository-oss)), which supports a variety
of build artifacts.

* controlled by a version-controlled file, e.g. `gitlab-ci.yml`

```yaml
image: python:3.8.5-slim-buster

stages:
  - test
  - deploy

before_script:
   - pip install --upgrade pip
   - pip install pytest twine

tests:
  stage: test
  script:
    - pip install backports.csv # try installing this from pypi, nexus may not like the [.]
    - python setup.py develop --index-url $PYPI_PROXY_URL # faster, less load for pypi
    - pytest
  tags: [docker]
  except:
    - tags

upload_to_nexus:
  stage: deploy
  variables:
    TWINE_USERNAME: $NEXUS_USERNAME
    TWINE_PASSWORD: $NEXUS_PASSWORD
  script:
    - python setup.py sdist
    - twine upload --repository-url $NEXUS_REPOSITORY_URL dist/*
  only:
    - tags
  tags: [docker]
```

You can handle credentials in the web interface (settings differ across platforms).

![](static/gitlab.png)


## Packaging Python Applications

* See: [Packaging](Packaging.md)

## Deployment options

* upload to PyPI
* installing the package
* versioning
* automate artifact creation (see: gitlab example)

## Elements of CI: test, build, static code analysis

* CI tools, as service or self-hosted
* Basic gitlab tooling

## Tools

* imports: isort (maybe done by your IDE already)
* code style: black, yapf (editor: format on save)
* readability and static analysis: pylint, prospector, pylava
* repository: tokei, sloccount, git of theseus

### The yapf tool

* yet another python formatter, developed by google

> In essence, the algorithm takes the code and reformats it to the best
> formatting that conforms to the style guide, even if the original code didn't
> violate the style guide. The idea is also similar to the 'gofmt' tool for the
> Go programming language: end all holy wars about formatting - if the whole
> codebase of a project is simply piped through YAPF whenever modifications are
> made, the style remains consistent throughout the project and there's no point
> arguing about style in every code review.

The reference to the Go ecosystem is interesting.

* Go started with a single style guide and this approach has found its ways into
  other languages in the past years.
* While this seems like a small thing to do, it really takes away lots of
  debate, while at the same time improving readability.

* use yapf with your editor

Running it as pre-commit hook or as part of regular code maintenance:

```shell
$ yapf --parallel --in-place --recurse mypackage
```

### The pylint tool

> The Python community has formalized somerecommended programming styles to help
 everyone write code in a common, agreed-upon style that makes the mostsense for
 shared code. This style is captured in PEP 8, the "Style Guide for Python
 Code". Pylint can be a quick andeasy way of seeing if your code has captured
 the essence of PEP 8 and is thereforefriendlyto other potential users

List of messages:

* [http://pylint-messages.wikidot.com/all-codes](http://pylint-messages.wikidot.com/all-codes)

It is possible to ignore particular messages with special comments.

```
# pylint: disable=F0401,C0111,W0232,E1101,R0904,E1103,C0301
```

Configurable via `.pylintrc` file.

The pylint tool emits a single score between 0 and 10, rating the code.

```shell
$ pylint project
...

-----------------------------------
Your code has been rated at 9.37/10
```

### Meta analysers

The [prospector](http://prospector.landscape.io/en/master/) tool includes a
cyclomatic complexity measure (McCabe, 1976).

Example output:

```shell
$ prospector
project/example/some_file.py
  Line: 102
    pylint: redefined-builtin / Redefining built-in 'all' (col 37)
  Line: 163
    pylint: unbalanced-tuple-unpacking / Possible unbalanced tuple unpacking with sequence: left side has 2 label(s), right side has 0 value(s) (col 4)
  Line: 181
    pylint: redefined-builtin / Redefining built-in 'id' (col 4)
  Line: 187
    mccabe: MC0001 / Loop 187 is too complex (29)
  Line: 212
    pylint: redefined-builtin / Redefining built-in 'format' (col 4)
  Line: 215
    pep8: W605 / invalid escape sequence '\.' (col 26)
    pep8: W605 / invalid escape sequence '\s' (col 28)
    pep8: W605 / invalid escape sequence '\d' (col 30)
    pep8: W605 / invalid escape sequence '\s' (col 33)
    pep8: W605 / invalid escape sequence '\s' (col 37)
    pep8: W605 / invalid escape sequence '\d' (col 40)
  Line: 219
```

The [pylava](https://github.com/pylava/pylava) does similar things with a
different, yet overlapping set of tools. The default output is a bit more
compact.

```shell
siskin/sources/vkfilmff.py:103:80: E501 line too long (101 > 79 characters) [pycodestyle]
siskin/database.py:28:1: W0611 'logging' imported but unused [pyflakes]
siskin/database.py:32:1: W0611 'six.moves.urllib.parse' imported but unused [pyflakes]
siskin/database.py:38:80: E501 line too long (84 > 79 characters) [pycodestyle]
siskin/database.py:52:80: E501 line too long (100 > 79 characters) [pycodestyle]
```

### The tokei tool

There are a lot of source code line counters, but I found tokei to be particularly fast.

* [https://github.com/XAMPPRocky/tokei/releases/](https://github.com/XAMPPRocky/tokei/releases/)

```shell
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
 Autoconf                8         2652         2038          154          460
 Batch                   3            8            5            2            1
 C Header               16         2540         1429          708          403
 CSS                     1           69           69            0            0
 Dockerfile              1           47           21           19            7
 JSON                    3          132          118            0           14
 Makefile                1           27           19            0            8
 Pan                     2           75           74            1            0
 Python               1104       443745       349100        25715        68930
 ReStructuredText      140        72137        50795            0        21342
 Shell                  16          932          609          134          189
 SVG                    13          613          607            5            1
 Plain Text              6          140            0          130           10
 TOML                    1           32           29            2            1
 YAML                   22          978          837           59           82
-------------------------------------------------------------------------------
 HTML                  109        12786        12084           55          647
 |- CSS                 10          593          327            2          264
 |- JavaScript           5          185          146           19           20
 (Total)                          13564        12557           76          931
-------------------------------------------------------------------------------
 Jupyter Notebooks       1            0            0            0            0
 |- Markdown             1          237            1          184           52
 |- Python               1          210          189            7           14
 (Total)                            447          190          191           66
-------------------------------------------------------------------------------
 Markdown               18         1739            0         1271          468
 |- Python               1           40           36            0            4
 (Total)                           1779           36         1271          472
===============================================================================
 Total                1465       539917       418533        28467        92917
===============================================================================
```

# Design Patterns

A look into design patterns and their applications Python.

## Favor object composition over class inheritance

* you can extend classes along multiple "axes", which leads to "class proliferation"
* standard library "logging" is an example of "composition over inheritance"

### Logging

With inheritance only, you could wind up with:

* Logger
* StdoutLogger
* StderrLogger
* FilteredStdoutLogger
* ...

Various ways to adapt:

* **Adaptor** pattern, using a conventional interface, e.g. the "write" method and
  wrap all output modalities in a new class supplying this function, adapting to
  the needs of the logger.
* **Bridge**, similar to Adaptor, but using a custom abstraction, e.g. a message
  that works slightly higher in the hierarchy (e.g. passing a message, versus
  "write")

> "Adapter makes things work after they're designed; Bridge makes them work
> before they are. [GoF, p219]"

* **Decorator** pattern

If a filter wraps a logger with the same method name, e.g. `log`, we can stack
them.

```python

class Filter:
    def __init__(self, pattern, logger):
        self.pattern = pattern
        self.logger = logger

    def log(self, message):
        if pattern in message:
            self.logger.log(message)

log1 = SomeLogger("app.log")
log2 = Filter("debug", log1)
log3 = Filter("todo", log2)
...
```

The way the standard library implements logging is by separating loggers, formatters, handlers.

> Handler objects are responsible for dispatching the appropriate log messages
> (based on the log messages’ severity) to the handler’s specified destination. 

* streams, files

Actually, more the
[docs](https://docs.python.org/3/howto/logging.html#useful-handlers) list more
than 10 implementations, like `TimeRotatingFileHandler` and `HTTPHandler`.

> Formatter objects configure the final order, structure, and contents of the
> log message. Unlike the base logging.Handler class, application code may
> instantiate formatter classes, although you could likely subclass the
> formatter if your application needs special behavior. 

Putting these things together:

```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

## MVC

* model view controller, separation of concerns

Often used in frameworks with UI elements.

* web frameworks
* GUI frameworks, although Tkinter seems to have a more tighter coupling

In web framworks the separation goes along:

* database abstraction and queries (M)
* mostly logic-less HTML templates (V)
* handing of the request-response cycle (C)

In desktop toolkits, you will have some **Observer** pattern implemented.

For example in a classic (Java) example, the tabular data model (`TableModel`) can
inform other components about change via `addTableModelListener`, propagating events.

A test for true MVC design:

> Is the program functional even without the view? Or the controller?

## Global objects

* similar to singletons

Often used for constants, defined on module level and exported.

Special cases, e.g. *dunder* constants, like `__version__`.

A few builtin dunder names:

* `__file__` (the current file)
* `__name__` (the name of the module, e.g. `__main__` when invoked from the command line)

## Abstract Factory

Factories are classes that build objects. Not really needed in Python.

> But Python has the concept of callables, which typically allow to pass in the
> class itself.

Python has first class functions, which are callable. Methods are callable, and
classes are, too, if they implement `__call__`.

There are alternatives:

* a simple function
* a method on a class
* a generator with some state

```python
class Switch:
    def __init__(self):
        self.on = False
    def __call__(self):
        print("switch is {}".format("on" if self.on else "off"))
        self.on = bool(1 - self.on)


switch = Switch()
switch()
switch()
```

For specifying required functionality, create an abstract class by returning
`NotImplementedError` on the methods that subclasses need to provide. 

## Singleton pattern

Examples:

* [Snippets/Singleton/classic.py](Snippets/Singleton/classic.py)
* [Snippets/Singleton/new.py](Snippets/Singleton/new.py)

Notes.

* overwriting `__new__`
* not that pronounced either, use global object instead

## Iterator pattern

There is concept of an iterator in Python (in
[iterable](https://docs.python.org/3.4/library/collections.abc.html#collections.abc.Iterable)),
[iterator](https://docs.python.org/3.4/library/collections.abc.html#collections.abc.Iterator).

* `iter` has a dual role; it turns a sequence into an iterator or allows to use
  a callable to create a sequence

Example application, reading a file in blocks:

```python
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)
```

> Return a new *partial* object which when called will behave like func called
> with the positional arguments args and keyword arguments keywords.


## Wrap Up

Design patterns exists, but some of the original patterns are less prevalent as
Python constructs exist to (partially) address the problems.


# Reproducibility

> It is common practice that in teams working in the field of natural sciences
all group members manage their primary data in highly individual systems.

-- https://datascience.codata.org/jms/article/download/dsj.8.18/198 (2009)

Aspects of reproducibility:

* source code
* data
* collaboration

Some approaches require a minimal change in individual workflow, other require
some group consensus or infrastructure support.

## Source Code

### Jupyter versioning

* Jupytext for versioning notebooks

### Project layout

* use convention for project structure, e.g. like [kedro](https://github.com/quantumblacklabs/kedro)

### Environment

* [watermark](https://github.com/rasbt/watermark) a notebook
* leave a requirements.txt file
* using virtual environments help you to keep workspaces and projects isolated

```
$ pip freeze > requirements.txt
```

* include a `setup.py` and create a package, maybe with command line tools for managing the experiment

There are more complex tools that allow running notebooks in the cloud (or on premise):

* [Binder](https://mybinder.org/)

Binder will inspect your git repository and will try to recreate a suitable
environment from scratch (via Linux Containers).

----

Sidenote: While Makefiles seem to come from another time altogher, they still
can be useful for expressing dependencies. There is a stanza that I try to
follow: checkout, config, build.

For example, if I would have a repo for an experiment, with maybe a report or
paper, I would aim for a complete rerun from data gathering to run, diagram and
final PDF generation. That will take some time to get right first, but it's a
great way to not having to go to all steps manually again. A Makefile can serve
as documentation as well.

----

### Documentation

A tool like [pandoc](https://pandoc.org/) can help to convert notes taken in
markdown into TeX, PDF and other formats.

If your code is public, you may want to look into some documentation hosting like:

* [readthedocs](https://docs.readthedocs.io/en/stable/)

## Data

### Accessibility

* cloud notebooks, google colab, can reference cloud storage (similar across
  cloud, e.g. Azure notebooks)
* internal, referencable cloud storage to be used in notebooks (open source S3
  storage systems available)

For example Pandas does have options to read remote data.

```python
df = pd.read_csv('s3://pandas-test/tips.csv')
```

One example of an open source solution for S3 API is
[seaweedfs](https://github.com/chrislusf/seaweedfs).

> SeaweedFS is a distributed object store and file system to store and serve
> billions of files fast! Object store has O(1) disk seek, transparent cloud
> integration. Filer supports cross-cluster active-active replication,
> Kubernetes, POSIX, S3 API, encryption, Erasure Coding for warm storage, FUSE
> mount, Hadoop, WebDAV.

### Packaging

* goal: reduce time to group and clean data
* datapackage, [project](https://frictionlessdata.io/data-package/)

> Data Package is a simple container format used to describe and package a
> collection of data. The format provides a simple contract for data
> interoperability that supports frictionless delivery, installation and
> management of data.

Another tool in that realm is [json-stat](https://json-stat.org/).

The general idea is that once some work has been done in cleaning and grouping
data, this work should in the best case not be lost, but documented and
snapshotted, so you (or someone else) can come back to it later.

### Versioning

* [dvc](https://dvc.org/doc/use-cases/versioning-data-and-model-files)

## Collaboration

* git and git hosting
* CI pipelines for code checks
* Google Colab, https://colab.research.google.com/

# On testing and pytest

The Django web framework is a prominent Python project.

From its docs:

> You might have created a brilliant piece of software, but you will find that
> many other developers will refuse to look at it because it lacks tests;
> without tests, they won’t trust it. Jacob Kaplan-Moss, one of Django’s
> original developers, says “Code without tests is broken by design.”

> That other developers want to see tests in your software before they take it
seriously is yet another reason for you to start writing tests.

From: https://docs.djangoproject.com/en/3.1/intro/tutorial05/#tests-make-your-code-more-attractive

## The testing spectrum

* throwaway code
* experiment
* industrial code, used, contracts, SLA, maintenance, support team

Methodologies:

* Test-driven-development (TDD)
* issue driven testing; to address regressions
* code and tests (OSS)

## Reproducibility

Code is written in vastly different contexts. But there are some issues, even in
the scientifc realm.

> The replication crisis (or replicability crisis or reproducibility crisis) is,
> as of 2020, an ongoing **methodological crisis** in which it has been found that
> many scientific studies are difficult or impossible to replicate or reproduce.

Also: 2016 Nature article

* [1,500 scientists lift the lid on
  reproducibility](https://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970)

The first sentence only:

> More than 70% of researchers have tried and failed to reproduce another
> scientist's experiments, and more than half have failed to reproduce their own
> experiments.

## A not atypical example

* CS paper from 2018, "cited by 9"
* code released alongside paper (+)
* no tests (-)
* pylint score (-)


```
$ tokei
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
 CSS                     2          442          366            5           71
 HTML                    1          202          187            0           15
 JavaScript              2          146          100           18           28
 Markdown                1           69            0           57           12
 Python                  5          873          706           45          122
 Plain Text              2            9            0            9            0
===============================================================================
 Total                  13         1741         1359          134          248
===============================================================================
```

Is it tested?

```
$ find . -name "*py" | wc -l
5
$ find . -name "test_*py" | wc -l
0
```

The pylint score out of the box:

```
$ pylint *py
Your code has been rated at 3.54/10
```

Some of those errors:

```
     44 (line-too-long)
     43 (missing-function-docstring)
     33 (invalid-name)
     17 (import-error)
     16 (wrong-import-order)
     12 (logging-not-lazy)
     10 (no-member)
      8 (missing-class-docstring)
      7 (unused-argument)
      6 (useless-object-inheritance)
      6 (unused-variable)
      6 (singleton-comparison)
      6 (no-self-use)
      5 (missing-module-docstring)
      5 (missing-final-newline)
      5 (anomalous-backslash-in-string)
      4 (wrong-import-position)
      4 (too-few-public-methods)
      4 (pointless-string-statement)
      4 (no-else-return)
```

There is one folder called `test`, but it contains an example input file (we
sometimes call this a fixture).

The repo states:

> Please cite the corresponding publication in case you make use of our tools.

A personal comment:

* I will spend more time than necessary to understand what the code does.
* I will want to confirm some workings before I use it as a part of a different
  project.
* I will probably copy things into a new project and use parts as starting point.


A brief look at the project history:

* written offline, before moving to github (often the case when tools get open-sourced)
* touch on about three days, two pull requests

Interetingly, the pull requests (PR) came from a second person:

* the person wanted to commit the `requirements.txt` into the repo - the least
  you can do to enable another person to recreate the environment
* the second PR was about some error that happens at runtime only (and only, if
  you are rebuilding the environment)

Note: I have not cherry-picked this repository, but it already tells a story.

## A brief look at scikit-learn

### Overview

Big project, lots of users, many QA measures in place.

```
$ tokei
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
 Autoconf                2           34           32            1            1
 Batch                   4          199          161            2           36
 C                       3         1089          772          174          143
 C Header                8          442          298           49           95
 C++                     5         6810         5535          466          809
 CSS                     7         9609         9213          117          279
 JavaScript              9         3330         2202          485          643
 JSON                    2          195          169            0           26
 Makefile                4          182          129           15           38
 Markdown                4           96            0           71           25
 Python                821       272819       216641        19903        36275
 ReStructuredText      139        50755        38287            0        12468
 Shell                  19         1165          760          221          184
 SVG                     3         1399         1174           39          186
 Plain Text             40          337            0          232          105
 TOML                    1           15           14            1            0
 YAML                    5          409          371           24           14
-------------------------------------------------------------------------------
 HTML                    7          867          815            8           44
 |- JavaScript           2          168          137           15           16
 (Total)                           1035          952           23           60
===============================================================================
 Total                1083       349920       276710        21823        51387
===============================================================================
```

Around 800 Python files, a quarter of which are tests.

```
$ find . -name "*py" -type f | wc -l
821

$ find . -name "test_*py" -type f | wc -l
204
```

You also meet old friends:

* setup.py

Some more project related files in the repo:

* pyproject.toml (which relates to [PEP 518](https://www.python.org/dev/peps/pep-0518/))

Which mostly provides bootstrap dependencies:

```toml
[build-system]
# Minimum requirements for the build system to execute.
requires = [
    "setuptools",
    "wheel",
    "Cython>=0.28.5",
    "numpy==1.13.3; python_version=='3.6' and platform_system!='AIX' and platform_python_implementation == 'CPython'",
    "numpy==1.14.0; python_version=='3.6' and platform_system!='AIX' and platform_python_implementation != 'CPython'",
    "numpy==1.14.5; python_version=='3.7' and platform_system!='AIX'",
    "numpy==1.17.3; python_version>='3.8' and platform_system!='AIX'",
    "numpy==1.16.0; python_version=='3.6' and platform_system=='AIX'",
    "numpy==1.16.0; python_version=='3.7' and platform_system=='AIX'",
    "numpy==1.17.3; python_version>='3.8' and platform_system=='AIX'",
    "scipy>=0.19.1",
]
```

We also see a file called `conftest.py` which is a pytest related file.

Other files in the repo:

* related to git
* code coverage, e.g. `.codecov.yml`

A SAAS solution for code health, with some options:

```yaml
coverage:
  status:
    project:
      default:
        # Commits pushed to master should not make the overall
        # project coverage decrease by more than 1%:
        target: auto
        threshold: 1%
```

* lgtm.yaml - scanning for CVEs

> LGTM is a variant analysis platform that automatically checks your code for
> real CVEs and vulnerabilities.

The first take-away:

* modern projects can **accumulate quite a bit of boilerplate config** to do all
  kinds of tasks related to **code quality over time**; many SAAS offerings will be
  free for open source projects; some things are completely open source or can
  be incorporated into internal workflows by using git hooks or other tools

### Building and running tests

* I can run the standard tools to create a workable development environment

Here, I could run (via [Building from
source](https://scikit-learn.org/stable/developers/advanced_installation.html#building-from-source)):

```shell
(sklearn) $ pip install --no-build-isolation --editable .
Obtaining file:///home/tir/code/scikit-learn/scikit-learn
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Collecting joblib>=0.11
  Downloading joblib-0.17.0-py3-none-any.whl (301 kB)
     |████████████████████████████████| 301 kB 2.1 MB/s 
Collecting numpy>=1.13.3
  Downloading numpy-1.19.2-cp38-cp38-manylinux2010_x86_64.whl (14.5 MB)
     |████████████████████████████████| 14.5 MB 3.8 MB/s 
Collecting scipy>=0.19.1
  Using cached scipy-1.5.2-cp38-cp38-manylinux1_x86_64.whl (25.7 MB)
Collecting threadpoolctl>=2.0.0
  Using cached threadpoolctl-2.1.0-py3-none-any.whl (12 kB)
Installing collected packages: joblib, numpy, scipy, threadpoolctl, scikit-learn
  Running setup.py develop for scikit-learn
Successfully installed joblib-0.17.0 numpy-1.19.2 scikit-learn scipy-1.5.2 threadpoolctl-2.1.0
```

This will pick up pyproject.toml and other requirements. I can install them into
a virtual environment (which is created with `mkvirtualenv`, but that does not
matter).

----

Sidenote: The python packaging landscape changes slowly, but changes. We have
[poetry](https://python-poetry.org/docs/pyproject/#poetry-and-pep-517) and
[pipenv](https://pypi.org/project/pipenv/) and classic
[setup.py](https://packaging.python.org/tutorials/packaging-projects/).

We looked at the basic setup.py approach in session one, which is still widely
used and provides a baseline.

----

Recap:

* checked out project
* created some isolated environment
* ran a single (standard) command that would install dependencies and build the project

This process did not install `pytest` automatically, but a simple `pip install
pytest` would work (version might be an issue). Then:

```
(sklearn) $ pytest
...
collected 18122 items / 2 skipped / 18120 selected
...

17155 passed, 914 skipped, 28 xfailed, 27 xpassed, 4162 warnings in 620.59s (0:10:20) 

real    10m22.915s
user    20m9.719s
sys     14m59.659s
```

* xfail - expected to fail (e.g. unimplemented feature)
* xpass - expected to pass, but failed

Running the whole test suite takes 10 minutes. All test passed. Some were
skipped automatically (maybe pandas or matplotlib were missing).

> What does this enable me to do?

* given understanding of technical or domain problem this project allows me to
  start contributing in less than an hour
* it allows me to keep track of everything that is happening within this project
  with a few git commands
* it allows me to understand, whether changes I make break functionality without
  me having to necessarily read all related code
* it allows me to follow a guideline, tight but clear, set by the community of
  developers working on this project
  (https://scikit-learn.org/stable/developers/contributing.html#contributing-code)
* it allows me to contribute in various ways, e.g. with code,
  [documentation](https://scikit-learn.org/stable/developers/contributing.html#contribute-documentation),
  etc.

What does this ultimately lead to?

* clean code over time
* motivated developers seeing their contribution included in the project
* focus on problem domain (ML), not minutiae
* less frustration, because some process is in place and it is to some extend
  very explicit

Last but not least:

* http://gael-varoquaux.info/programming/getting-a-big-scientific-prize-for-open-source-software.html

> Getting a big scientific prize for open-source software (2019-12-01)

> An important acknowledgement for a different view of doing science: open,
> collaborative, and more than a proof of concept.

> [...] No. We did it different. We reached out to an open community. We did
> BSD-licensed code. We worked to achieve quality at the cost of quantity. We
> cared about installation issues, on-boarding biologists or medical doctors,
> playing well with the wider scientific Python ecosystem.

...

> The world does not understand how much the promises of data science, for today
> and tomorrow, need open source projects, easy to install and to use by
> everybody. These projects are like roads and bridges: they are needed for
> growth although [c.] no one wants to pay for maintaining them.

## Economy of testing

* cost of finding a bug at various points in project: 1x, 10x, 100x.
* testing has become easier with many different tools that automate what an
  expert did years or decades ago: e.g. style, lint, coverage, fuzzing and more.

There are some metrics around testing, relating to the (average) cost of bugs.

* actb - average cost of testing bug
* acpb - average cost of production bug

```python
actb = (cost_of_detection + cost_of_internal_failure) / (test_bugs)

acpb = cost_of_external_failure / production_bugs

test_roi = ((acpb - actb) * test_bugs ) / cost_of_detection
```

The internal failure costs:

> The testing and development costs that we incur purely because we find bugs.
For example, **filing bug reports**, **fixing bugs**, **confirmation testing bug fixes**,
and **regression testing** changed builds are activities that incur costs of
internal failure.

These considerations are more for industry software, for experimental code, the
reproducibility story is probably more interesting.


## The pytest project

* python has [unittest](https://docs.python.org/3/library/unittest.html) is
  standard library, classic framework (inspired by JUnit)
* setUp, tearDown, assertTrue, assertEquals, assertRaises, ...

The basic notions are similar:

* fixture
* test case
* test suite
* test runner
* helpful messages

One goal of pytest was to be a bit more pythonic (with unittest coming fro JUnit)

### Basics

* pytest detects tests by name prefix, e.g. `test_*` functions and methods
* grouping in a class possible
* only a single `assert`

Calling pytest with filename, directory or via name filter `-k` to select
specific files.

```
$ pytest test_fixture.py
$ pytest -k fix
```

### Marks

* setting metadata on functions
* a list of builtin marks can be found here: [marks](https://docs.pytest.org/en/stable/reference.html#marks-ref)

For example, you can mark a test function with
[skipif](https://docs.pytest.org/en/stable/reference.html#pytest-mark-skipif) to
skip under certain conditions; or
[xfail](https://docs.pytest.org/en/stable/reference.html#pytest-mark-xfail) to
expect a failed test.

### Fixtures

* pytest approach to fixtures is interesting, as it is mostly name based

If we run this, we do not get any output.

```python
def test_hello(tmpdir):
    print(tmpdir)
```

The test would pass, but not print anything on this successful test.

```
platform linux -- Python 3.7.8, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/tir/code/miku/cleancodepython/Snippets/TestingBasic
collected 1 item                                                                                                                                                                                                                              

test_fixture.py .                                                            [100%]
```

We need to pass `-s` shortcut to see the output, as pytest offers various capture method.

```
  --capture=method      per-test capturing method: one of fd|sys|no|tee-sys.
  -s                    shortcut for --capture=no.
```

Default:

> During test execution any output sent to stdout and stderr is captured. If a
> test or a setup method fails its according captured output will usually be
> shown along with the failure traceback.

The output can be captured on a filesystem (fd 0 and 1) level (e.g. when calling
external commands) or on `sys.write` level. The `tee-sys` captures and passes
through output, like the tee (T) command.

* Example: [Snippets/Testing/test_ls.py](Snippets/Testing/test_ls.py)

There are more builtin fixtures:

* [https://docs.pytest.org/en/stable/builtin.html](https://docs.pytest.org/en/stable/builtin.html)

Examples are: caching values, capturing logging messages, recording warnings

### Fixture: monkeypatch

> monkeypatch can be used to patch functions dependent on the user to always
> return a specific value.

* Example: [Snippets/Testing/test_ssh.py](Snippets/Testing/test_ssh.py)

### Custom fixture

Fixtures can provide various test dependencies. They are a form of dependency
injection.

You can include these in your testfiles or in `conftest.py` to be shared by multiple tests.

A fixture can be valid in different scopes:

> Fixtures requiring network access depend on connectivity and are usually
> time-expensive to create. Extending the previous example, we can add a
> scope="module" parameter to the @pytest.fixture invocation to cause the
> decorated smtp_connection fixture function to only be invoked once per test
> module (the default is to invoke once per test function). 

> Possible values for scope are: function, class, module, package or session.

Initialization goes from session to function.

A fixture can handle both setup and teardown, when using `yield` at the point
where execution should continue in the test.

Examples:

* [Snippets/Testing/test_fixture_custom.py](Snippets/Testing/test_fixture_custom.py)
* [Snippets/Testing/test_fixture_autouse.py](Snippets/Testing/test_fixture_autouse.py)
* [Snippets/Testing/test_fixture_yield.py](Snippets/Testing/test_fixture_yield.py)

### Other plugins

* common data directory for test files:
  [pytest-datadir](https://pypi.org/project/pytest-datadir/) or
  [pytest-datafiles](https://pypi.org/project/pytest-datafiles/)


## Code coverage

Coverage measures the ratio of tested lines of code and lines of code. 100%
coverage does not mean bug free.

Automated tool:

* [https://coverage.readthedocs.io/en/coverage-5.3/](https://coverage.readthedocs.io/en/coverage-5.3/)

You can run it standalone:

```
$ coverage run -m pytest -v
```

This will generate an sqlite3 database, be default `.coverage`. Generate a report:

```
$ coverage report -i gluish/*
Name                  Stmts   Miss  Cover
-----------------------------------------
gluish/__init__.py        8      0   100%
gluish/common.py        117     59    50%
gluish/format.py         70     30    57%
gluish/intervals.py      27     15    44%
gluish/parameter.py       5      0   100%
gluish/task.py           77     55    29%
gluish/utils.py          54     30    44%
-----------------------------------------
TOTAL                   358    189    47%
```

Or install a pytest plugin for coverage.

```
$ pip install pytest-cov
```

Run alongside tests:

```
$ pytest --cov=gluish -v gluish/*
```

Various outputs are available, e.g. HTML.

## Other testing helpers

requests is a popular HTTP library,
[responses](https://github.com/getsentry/responses) is a great addition to test
HTTP interactions.

```python
@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps

def test_api(mocked_responses):
    mocked_responses.add(
        responses.GET, 'http://twitter.com/api/1/foobar',
        body='{}', status=200,
        content_type='application/json')
    resp = requests.get('http://twitter.com/api/1/foobar')
    assert resp.status_code == 200
```

# Miscellanea

## Separate code and configuration

* [XDG spec](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)

The [configparser](https://docs.python.org/3/library/configparser.html) module
supports a basic ini style format with sections.

* everything stored as string
* fallback defaults

Maybe a config framework can help:

* [dynaconf](https://www.dynaconf.com/)

## Core and Plugin architecture

* The imageio package has a core and support for various formats.

> Imagio is plugin-based. Every supported format is provided with a plugin. You
can write your own plugins to make imageio support additional formats. And we
would be interested in adding such code to the imageio codebase!

> Registering

> Strictly speaking a format can be used stand alone. However, to allow imageio
to automatically select it for a specific file, the format must be registered
using ``imageio.formats.add_format()``.

> Note that a plugin is not required to be part of the imageio package; as long
as a format is registered, imageio can use it. This makes imageio very easy to
extend.

One core notion is that of a Format:

```python
class Format(object):
    """Represents an implementation to read/write a particular file format

    A format instance is responsible for 1) providing information about
    a format; 2) determining whether a certain file can be read/written
    with this format; 3) providing a reader/writer class.

    Generally, imageio will select the right format and use that to
    read/write an image. A format can also be explicitly chosen in all
    read/write functions. Use ``print(format)``, or ``help(format_name)``
    to see its documentation.

    To implement a specific format, one should create a subclass of
    Format and the Format.Reader and Format.Writer classes. see
    :doc:`plugins` for details.

    Parameters
    ----------
    name : str
        A short name of this format. Users can select a format using its name.
    description : str
        A one-line description of the format.
    extensions : str | list | None
        List of filename extensions that this format supports. If a
        string is passed it should be space or comma separated. The
        extensions are used in the documentation and to allow users to
        select a format by file extension. It is not used to determine
        what format to use for reading/saving a file.
    modes : str
        A string containing the modes that this format can handle ('iIvV'),
        “i” for an image, “I” for multiple images, “v” for a volume,
        “V” for multiple volumes.
        This attribute is used in the documentation and to select the
        formats when reading/saving a file.
    """
```

There is a `DummyFormat` example included, which make starting a new format simpler.

The core also contains:

```python
"""

These are the main classes of imageio. They expose an interface for
advanced users and plugin developers. A brief overview:

  * imageio.FormatManager - for keeping track of registered formats.
  * imageio.Format - representation of a file format reader/writer
  * imageio.Format.Reader - object used during the reading of a file.
  * imageio.Format.Writer - object used during saving a file.
  * imageio.Request - used to store the filename and other info.

...
"""
```

The FormatManager is a singleton, via module import:

```python
# Load some bits from core
from .core import FormatManager, RETURN_BYTES

# Instantiate format manager
formats = FormatManager()
```

Each format registers itself.

```python
# Register. You register an *instance* of a Format class.
format = FfmpegFormat(
    "ffmpeg",
    "Many video formats and cameras (via ffmpeg)",
    ".mov .avi .mpg .mpeg .mp4 .mkv .wmv",
    "I",
)
formats.add_format(format)
```

Higher level functions will use lookups to find the right format.

```python
    # Create request object
    request = Request(uri, "r" + mode, **kwargs)

    # Get format
    if format is not None:
        format = formats[format]
    else:
        format = formats.search_read_format(request)
    if format is None:
        modename = MODENAMES.get(mode, mode)
        raise ValueError(
            "Could not find a format to read the specified file in %s mode" % modename
        )

```

# Design Approach

* "worse is better" (Richard Gabriel), https://www.dreamsongs.com/RiseOfWorseIsBetter.html

Two concurrent approaches to design, exemplified on Unix.


* Simplicity -- the design must be simple, both in implementation and interface.
    It is more important for the implementation to be simple than the interface.
    Simplicity is the most important consideration in a design. Correctness --
    the design must be correct in all observable aspects. It is slightly better
    to be simple than correct.

* Consistency -- the design must not be overly
    inconsistent. Consistency can be sacrificed for simplicity in some cases,
    but it is better to drop those parts of the design that deal with less
    common circumstances than to introduce either implementational complexity or
    inconsistency.

* Completeness -- the design must cover as many important situations as is
    practical. All reasonably expected cases should be covered. Completeness can
    be sacrificed in favor of any other quality. In fact, completeness must be
    sacrificed whenever implementation simplicity is jeopardized.

* Consistency can be sacrificed to achieve completeness if simplicity is
    retained; especially worthless is consistency of interface.

> There is a final benefit to worse-is-better. Because a New Jersey language and
> system are not really powerful enough to build complex monolithic software,
> large systems must be designed to reuse components. Therefore, a tradition of
> integration springs up.


## Data Science Related Projects

* https://github.com/quantumblacklabs/kedro

> Kedro is an open-source Python framework that applies software engineering
> best practices to data and machine-learning pipelines. You can use it, for
> example, to optimise the process of taking a machine learning model into a
> production environment. You can use Kedro to organise a single-user project
> running on a local environment, or collaborate in a team on an
> enterprise-level project.

* https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html

Some practices they suggest:

* https://kedro.readthedocs.io/en/stable/02_get_started/05_example_project.html#what-best-practice-should-i-follow-to-avoid-leaking-confidential-data
* https://kedro.readthedocs.io/en/stable/11_faq/01_faq.html#what-is-data-engineering-convention

Template library:

* https://github.com/drivendata/cookiecutter-data-science/

Other projects:

* https://github.com/pachyderm/pachyderm
* https://dvc.org/
