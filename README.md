# AbstractSyntaxTree

Python3 script which takes a txt file generated from clang -ast-dump as input and outputs a dot file. 
The dot file can be converted to a pdf image of the abstract syntax tree using the following commands:

python3 ConvertToDot.py test.txt > ast.dot

dot -Tpdf ast.dot -o ast.pdf
