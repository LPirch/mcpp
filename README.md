# McCabe++ (mcpp)

<img src="media/mcpp.jpeg" height=400/>

`mcpp` measures typical code complexity metrics like McCabe's cyclomatic
complexity.

The goal of this project is to provide a re-usable script to analyze C/C++
source code and extract complexity metrics from it.

## Complexity Metrics

| Dimension            | ID | Metric Description             |    |
|----------------------|----|--------------------------------|----|
| CD1: Function        | C1 | cyclomatic complexity          | ✅ |
| CD2: Loop Structures | C2 | number of loops                | 🕒 |
|                      | C3 | number of nested loops         | 🕒 |
|                      | C4 | maximum nesting level of loops | 🕒 |

## Vulnerability Metrics

| Dimension               | ID  | Metric Description                                                        |    |
|-------------------------|-----|---------------------------------------------------------------------------|----|
| VD1: Dependency         | V1  | number of parameter variables                                             | 🕒 |
|                         | V2  | number of variables as parameters for callee function                     | 🕒 |
| VD2: Pointers           | V3  | number of pointer arithmetic                                              | 🕒 |
|                         | V4  | number of variables involved in pointer arithmetic                        | 🕒 |
|                         | V5  | maximum number of pointer arithmetic operations a variable is involved in | 🕒 |
| VD3: Control Structures | V6  | number of nested control structures                                       | 🕒 |
|                         | V7  | maximum nesting level of control structures                               | 🕒 |
|                         | V8  | maximum number of control-dependent control structures                    | 🕒 |
|                         | V9  | maximum number of data-dependent control structures                       | 🕒 |
|                         | V10 | number of if structures without else                                      | 🕒 |
|                         |     | V11 number of variables involved in control predicates                    | 🕒 |

✅ ❌ 🕒


## Setup

```sh
pip install -e .
```

## Usage

```sh
setup       # build tree-sitter libs
```

Configuration parameters can be changed in `config.yaml` or directly on the CLI
with e.g. `someCmd paths.out_root=some/dir`.