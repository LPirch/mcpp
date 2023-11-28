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
| CD2: Loop Structures | C2 | number of loops                | ✅ |
|                      | C3 | number of nested loops         | ✅ |
|                      | C4 | maximum nesting level of loops | ✅ |

## Vulnerability Metrics

| Dimension               | ID  | Metric Description                                                        |    |
|-------------------------|-----|---------------------------------------------------------------------------|----|
| VD1: Dependency         | V1  | number of parameter variables                                             | ✅ |
|                         | V2  | number of variables as parameters for callee function                     | ✅ |
| VD2: Pointers           | V3  | number of pointer arithmetic                                              | ✅ |
|                         | V4  | number of variables involved in pointer arithmetic                        | ✅ |
|                         | V5  | maximum number of pointer arithmetic operations a variable is involved in | ✅ |
| VD3: Control Structures | V6  | number of nested control structures                                       | ✅ |
|                         | V7  | maximum nesting level of control structures                               | ✅ |
|                         | V8  | maximum number of control-dependent control structures                    | ✅ |
|                         | V9  | maximum number of data-dependent control structures                       | ✅ |
|                         | V10 | number of if structures without else                                      | ✅ |
|                         | V11 | number of variables involved in control predicates                        | ✅ |



## Setup

Due to a limitation of setuptools (including external build steps), you need to
run the `setup` command manually once before installing the package.

```sh
pip install -e .
setup               # builds tree-sitter lib
pip install
```

## Usage

Configuration parameters can be changed in `config.yaml` or directly on the CLI
with e.g. `someCmd paths.out_root=some/dir`.

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
