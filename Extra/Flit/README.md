# Flit

* write code
* run "flit init"

Good for the simple case.

> Specifically, the easy things are pure Python packages with no build steps (neither compiling C code, nor bundling Javascript, etc.). The vast majority of packages on PyPI are like this: plain Python code, with maybe some static data files like icons included.

> It’s easy to underestimate the challenges involved in distributing and installing code, because it seems like you just need to copy some files into the right place. There’s a whole lot of metadata and tooling that has to work together around that fundamental step. But with the right tooling, a developer who wants to release their code doesn’t need to know about most of that.


----

> 

* flit init helps you set up the information Flit needs about your package.
* Subpackages are automatically included: you only need to specify the top-level package.
* Data files within a package directory are automatically included. Missing data files has been a common packaging mistake with other tools.
* The version number is taken from your package’s __version__ attribute, so that always matches the version that tools like pip see.
* flit publish uploads a package to PyPI, so you don’t need a separate tool to do this.



```
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "hello"
authors = [{name = "MC", email = "a@b.com"}]
readme = "README.md"
license = {file = "LICENSE"}
classifiers = ["License :: OSI Approved :: MIT License"]
dynamic = ["version", "description"]

```
