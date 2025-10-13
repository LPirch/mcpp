# McCabe++ (mcpp)

<img src="https://github.com/LPirch/mcpp/blob/master/media/mcpp.jpeg?raw=true" height=400/>

`mcpp` measures typical code complexity metrics like McCabe's cyclomatic
complexity.

The goal of this project is to provide a re-usable script to analyze C/C++
source code and extract complexity metrics from it. The implemented metrics
are taken from the [paper](https://xiaoningdu.github.io/assets/pdf/leopard.pdf)

> LEOPARD: Identifying Vulnerable Code for Vulnerability Assessment through Program Metrics  

This tool is released as part of our research in vulnerability discovery and 
has been used in our paper

> SoK: Where to Fuzz? Assessing Target Selection Methods in Directed Fuzzing" 

See also the corresponding [repo](https://github.com/wsbrg/crashminer).

## Complexity Metrics

| Dimension            | ID | Metric Description             |
|----------------------|----|--------------------------------|
| CD1: Function        | C1 | cyclomatic complexity          |
| CD2: Loop Structures | C2 | number of loops                |
|                      | C3 | number of nested loops         |
|                      | C4 | maximum nesting level of loops |

## Vulnerability Metrics

| Dimension               | ID  | Metric Description                                                        |
|-------------------------|-----|---------------------------------------------------------------------------|
| VD1: Dependency         | V1  | number of parameter variables                                             |
|                         | V2  | number of variables as parameters for callee function                     |
| VD2: Pointers           | V3  | number of pointer arithmetic                                              |
|                         | V4  | number of variables involved in pointer arithmetic                        |
|                         | V5  | maximum number of pointer arithmetic operations a variable is involved in |
| VD3: Control Structures | V6  | number of nested control structures                                       |
|                         | V7  | maximum nesting level of control structures                               |
|                         | V8  | maximum number of control-dependent control structures                    |
|                         | V9  | maximum number of data-dependent control structures                       |
|                         | V10 | number of if structures without else                                      |
|                         | V11 | number of variables involved in control predicates                        |

## Additional Metrics

| Dimension         | ID | Metric Description                                      |
|-------------------|----|---------------------------------------------------------|
| XD: Extra         | x1 | number of return statements                             |
|                   | x2 | number of cast expressions                              |
|                   | x3 | number of variable declarations                         |
|                   | x4 | maximum number of operands in an expression             |
| TD: AST Structure | t1 | number of AST nodes (descendants)                       |
|                   | t2 | height of the AST                                       |
|                   | t3 | average branching factor of the AST                     |
| SD: Code Smells   | s1 | number of non-trivial numeric constants (magic numbers) |
|                   | s2 | number of goto statements                               |
|                   | s3 | number of function pointers                             |
|                   | s4 | number of function calls without return value usage     |
| MD: Memory Ops    | m1 | number of memory allocations (malloc, alloc, new, etc.) |
|                   | m2 | number of pointer dereferences (`*`, `[]`, `->`)        |


## Setup

Build a docker container which performs the setup automatically or run the
installation on your local machine:

```sh
pip install .
```

> Note: It is recommended to install packages in virtual environments.


## Usage

### From Python

Simply import `mcpp` and then use the extract function (or one of its variants).

```python
from pathlib import Path
from mcpp import extract

input_dir = Path("some/dir")
in_files = list(input_dir.glob("**/*.c"))
result = extract(in_files)

# to extract only a subset of the metrics
result = extract(in_files, ["V1", "C3"])

# full list of metrics:
from mcpp import METRICS
print(list(METRICS.keys()))
```


### CLI

Configuration parameters can be changed in `config.yaml` or directly on the CLI
with e.g. `mcpp paths.out_root=some/dir`.

Using all defaults:
```sh
mcpp                # with default params like input directory, see config.yaml
```

Changing params from command line:
```sh
mcpp in_path=/some/dir/single_source out_path=single_source_metrics.json
mcpp metrics=\[C1,C2,V4\]
```

Or by passing a changed `config.yaml`:
- `-cp` (config_path) specifies the absolute path to the directory where the config file is located
- `-cn` (config_name) specifies the name of the config file
```sh
mcpp -cp /some/other/dir -cn myconfig.yaml
```

Try out the example:

```sh
mcpp in_path=examples/data/source paths.out_root=examples/data-out
cat examples/data-out/complexity.json
```
