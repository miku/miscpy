# ABC and Metaclasses

* Duck Typing means, we care about behaviour (more about the structure)
* EAFP aligns with that

## How to check for behaviour?

* no interfaces to start with
* `getattr`, `try ... except` (EAFP)
* `isinstance` - may be too narrow (we do no care about the structure)


