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

* one goal of pytest was to be a bit more pythonic (with unittest coming fro
JUnit)
* helpful messages

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

* Example: [Snippets/Testing](Snippets/Testing), `test_ls.py`

There are more builtin fixtures:

* [https://docs.pytest.org/en/stable/builtin.html](https://docs.pytest.org/en/stable/builtin.html)

Examples are: caching values, capturing logging messages, recording warnings

### Fixture: monkeypatch

> monkeypatch can be used to patch functions dependent on the user to always
> return a specific value.

* Example: [Snippets/Testing](Snippets/Testing), `test_ssh.py`

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

* `test_fixture_custom.py`
* `test_fixture_autouse.py`
* `test_fixture_yield.py`

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



