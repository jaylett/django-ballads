# django-ballads

Coordinate multi-system transactions that can include database work, filesystem access and remote API calls (and anything else you can think of).

## Simple usage

    from django_ballad import Ballad
    
    with Ballad(using='default') as ballad:
        orm_obj1 = db_operations()

        file_obj = make_file_part(orm_obj1)
        ballad.compensation(lambda: file_obj.unlink())

        remote_obj = call_remote_api(orm_obj1, file_obj)
        ballad.compensation(lambda: remote_obj.delete())

        orm_obj2 = more_db_operations()

There's a Django `transaction.atomic` wrapped up inside a ballad, and it will be rolled back *before* any compensating transactions.

An exception raised within the ballad block will appear out the top, unless there are exceptions during rollback in which case you'll get a `BalladException` which wraps both the rollback exceptions and any exception that caused the rollback. (The special `BalladRollback` exception will be ignored. You can also ignore exceptions raised during rollback by setting `ignore_rollback_exceptions` when constructing the `Ballad`.)

Right now we don't support wrapping multiple different database transactions into a ballad, although you can often just nest `with transaction.atomic()` clauses suitably.

## Requirements

This is really intended for use with Django 1.6 and up, although you may be able to use Django 1.5's older support with some databases. Tested on 1.5.1 and pre-1.6 with sqlite3 and postgresql.

## Contact

This is very early days for this; feedback welcome.

James Aylett
http://tartarus.org/james/
https://github.com/jaylett/django-ballads
