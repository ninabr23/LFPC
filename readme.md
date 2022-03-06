# Laboratory No.1
## Theme : Regular or context-free grammar

### Laboratory Tasks:
- Convert regular grammar to finite automaton(FA) `Grammar.to_fa()`
- Determine the grammar type by the Chomsky classification `Grammar.type`
- Using Finite Automaton check if some input string is accepted by FA `Grammar.is_acceptable(string="{input string}")`
- **Bonus Point** Using some graphic libraty plot FA Graph ` Grammar.graph() `

## Requirements for the program:
- Install requirements.txt `pip install -r requirements.txt`
- Install `graphviz` in your computer(debian -> `sudo apt install graphviz -y`), for other OS please check [graphiz.org](https://www.graphviz.org/download/)

## Program structure:
```
.
├── __pycache__
│   └── grammar.cpython-38.pyc
├── main .py
├── readme.md
├── requirements.txt
├── utils
│   ├── __init__.py
│   └── grammar.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```
### Legend:
- main.py - *The main program where the script is running*
- readme.md
- requirements.txt - *The libraries needed for the program to work*
- utills - *The utils map where is the `Grammar` class*
    - `__init__.py` - *File that shows this directory can be imported*
    - grammar.py - *`Grammar` class*
- venv - *Virtual Environment for the program*
