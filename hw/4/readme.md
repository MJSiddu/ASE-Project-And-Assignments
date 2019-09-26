**Some important points related to the data used in training and testing the ZeroR and NB models:**

* ZeroR initial training: For both weathernon and diabetes data, we read 3 rows before doing any classification ( the expected results shown in HW4's git doc is doing this with first 2 rows only)
* Naive Bayes initial training: As suggested in HW4 git doc, We read 4 rows from weathernon data and 20 rows from diabetes data before doing any classification
* Because of these small changes in model's initial training data, our results are slightly different from the expected results


ZeroR
```
weathernon
 db   | rx | num |  a |  b |  c |  d | acc | pre |  pd |  pf |   f |   g | class
 ---- | -- | --- | -- | -- | -- | -- | --- | --- | --- | --- | --- | --- | -----
 data | rx | 12 | 0 | 3 | 3 | 6 | 0.5 | 0.67 | 0.67 | 1.0 | 0.67 | 0.0 | yes 
 data | rx | 12 | 6 | 3 | 3 | 0 | 0.5 | 0.0 | 0.0 | 0.33 | 0.67 | 0.0 | no 


diabetes
 db   | rx | num |  a |  b |  c |  d | acc | pre |  pd |  pf |   f |   g | class
 ---- | -- | --- | -- | -- | -- | -- | --- | --- | --- | --- | --- | --- | -----
 data | rx | 766 | 474 | 243 | 25 | 24 | 0.65 | 0.49 | 0.09 | 0.05 | 0.15 | 0.16 | tested_positive 
 data | rx | 766 | 24 | 25 | 243 | 474 | 0.65 | 0.66 | 0.95 | 0.91 | 0.78 | 0.16 | tested_negative 
```

Naive Bayes
```
weathernon
 db   | rx | num |  a |  b |  c |  d | acc | pre |  pd |  pf |   f |   g | class
 ---- | -- | --- | -- | -- | -- | -- | --- | --- | --- | --- | --- | --- | -----
 data | rx | 10 | 0 | 3 | 3 | 4 | 0.4 | 0.57 | 0.57 | 1.0 | 0.57 | 0.0 | yes
 data | rx | 10 | 4 | 3 | 3 | 0 | 0.4 | 0.0 | 0.0 | 0.43 | 0.57 | 0.0 | no

 diabetes
  db   | rx | num |  a |  b |  c |  d | acc | pre |  pd |  pf |   f |   g | class
 ---- | -- | --- | -- | -- | -- | -- | --- | --- | --- | --- | --- | --- | -----
 data | rx | 748 | 195 | 179 | 60 | 314 | 0.68 | 0.84 | 0.64 | 0.24 | 0.72 | 0.69 | tested_negative
 data | rx | 748 | 314 | 60 | 179 | 195 | 0.68 | 0.52 | 0.76 | 0.36 | 0.62 | 0.69 | tested_positive
 ```
