### Why Re-invent the Wheel? ###

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
[ 3 ] Load Table From File

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

```
[ 1 ] Onboard New User
[ 2 ] Create New Table
[ 3 ] Load Table From File

# > 3
Enter the owner of the table:
> medovicn
Enter the name of the table:
> audit_data
Enter the delimeter to split on:
> ,
Enter the path to the file to load:
> ./sample_data/audit_data_2021_09_12.csv
Data load complete!
```
