 
 Task 2:

 ```
 db   | rx | num |  a |  b |  c |  d | acc | pre |  pd |  pf |   f |   g | class
 ---- | -- | --- | -- | -- | -- | -- | --- | --- | --- | --- | --- | --- | -----
 data | rx | 14 | 8 | 0 | 0 | 6 | 0.93 | 1.0 | 1.0 | 0.0 | 1.0 | 1.0 | yes 
 data | rx | 14 | 11 | 0 | 1 | 2 | 0.93 | 0.67 | 1.0 | 0.08 | 0.8 | 0.96 | no 
 data | rx | 14 | 8 | 1 | 0 | 5 | 0.93 | 1.0 | 0.83 | 0.0 | 0.91 | 0.91 | maybe
 ```

 Task 1 & 3: 

```
IN OUR IMPLEMENTATION, DROPPED COLUMNS ARE NOT CONSIDERED DURING COLUMN INDEXING


EX: For the given column headers -- 'outlook, ?$temp,  <humid, wind, !play',
Temp column will be dropped. After dropping the temp column, the index of humid column will be 2 according to our implementation and not 3 as shown in sample out


So please verify the answers accordingly


t.cols
|   1
|  |  add : Sym1
|  |  col :1
|  |  txt: outlook
|  |  mode: sunny
|  |  most: 5
|  |  n :14
|  |  cnt :{'rainy': 5, 'sunny': 5, 'overcast': 4}
|   2
|  |  add : Num1
|  |  txt: <humid
|  |  col :2
|  |  m2 :1375.2142857142858
|  |  mu :81.64285714285715
|  |  n :14
|  |  sd :10.285218242007035
|   3
|  |  add : Sym1
|  |  col :3
|  |  txt: wind
|  |  mode: FALSE
|  |  most: 8
|  |  n :14
|  |  cnt :{'FALSE': 8, 'TRUE': 6}
|   4
|  |  add : Sym1
|  |  col :4
|  |  txt: !play
|  |  mode: yes
|  |  most: 9
|  |  n :14
|  |  cnt :{'yes': 9, 'no': 5}
t.my
|   class: 4
|   goals: [1, 3]
|   nums: [1]
|   syms: [0, 2, 3]
|   w : [1] : -1
|   xs : [0, 2]
```