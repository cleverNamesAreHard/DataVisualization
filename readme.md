### But Why Tho ###

*Why not re-invent the wheel?*

I wanted to try my hand at a software I'd use for work to **house, manipulate, and display data**.

The idea is to provide **graphing, plotting, tables**, and other visual display medium in a **Web Interface**.

### Usage ###

```
> python dvcli.py
```

### CLI Example ###

```
[ 1 ] Onboard New User
[ 2 ] Create New Table

# > 2
Please enter the owner to onboard to:
> testuser
Please enter the tablename to create:
> demographic_info
Please enter your comma-separated headers:
> name,age,weight,enrolled

Valid types are TEXT, BOOLEAN, INTEGER, DECIMAL
Please enter the type for the following header:
received_by > text

Valid types are TEXT, BOOLEAN, INTEGER, DECIMAL
Please enter the type for the following header:
manager > integer

Valid types are TEXT, BOOLEAN, INTEGER, DECIMAL
Please enter the type for the following header:
shift > decimal

Valid types are TEXT, BOOLEAN, INTEGER, DECIMAL
Please enter the type for the following header:
receive_date > boolean
Table Created!
```
