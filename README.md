# JSON to YAML OpenAPI Schema

Converts response JSON into an appropriate OpenAPI Schema in the YAML format.

## Examples

#### Object

```
python main.py '{"fname": "bobby", "lname": "tables"}'
```

Output:

```
type: object
properties:
  fname:
    type: string
  lname:
    type: string
```


#### List

```
python main.py '[{"fname": "bobby", "lname": "tables"}]'
```


Output:

```
type: array
items:
  type: object
  properties:
    fname:
      type: string
    lname:
      type: string
```

