### `read_box` format
```
<Name> <Id> <IsWhite=1/IsBlack=0> <NumPIs> <NumPOs>  
<DelayTable>  
<Name> <Id> ... 
```


### `read_box -e` (extended format) 

```
.box <Id> <Name> <NumPIs> <NumPOs> [seq|comb] [black|white] [inner|outer]
<DelayTable>
.box <Id> ...
```

NumPIs, NumPOs = primary inputs/outputs, respectively. The delay table must have NumPIs * NumPOs entries.
Delay table: delays are stored in row-major order. e.g.:

# assuming 2 inputs and 3 outputs
1 1
3 4
4 2

pDelays[0] = 1; // output 0, input 0
pDelays[1] = 1; // output 0, input 1
pDelays[2] = 3; // output 1, input 0
pDelays[3] = 4; // output 1, input 1
pDelays[4] = 4; // output 2, input 0
pDelays[5] = 2; // output 2, input 1



# segfaults:
read_box on the following file:

adder 0 1 2 1
10 20
30 40

and on read_box -e:
.box 0 adder 2 1 comb white inner
10 20
30 40


## read_lut .lut file:
LUT size | area | pin delays

i area delay_0 delay_1 delay_2 ... delay_{i-1}

    i – LUT input size (1 to FPGA_MAX_LUTSIZE)

    area – Area cost of an i-input LUT

    delay_k – Delay from input pin k to output

e.g. 
```
3 1.3 0.2 0.3 0.5
```

TODO: malformed


FPGA mapping commands:
 if               ifif             print_box✅        print_lut✅
 print_tim        read_box✅         read_lut✅         write_box✅