# Txt to Dot File Converter
# Takes an Abstract Syntax Tree .txt file dumped by clang as input
# and outputs a dot file that can be used to create a graph

import re
import sys

#initialize variables
List = []
count = 0
cur_indent = 0
prev_indent = 0
filename = sys.argv[1]

#print first line of dot file
print("digraph unamed {\n")

#open text file that will be converted to dot file
with open(filename, "rt") as myfile:
    for content in myfile:
        #if the file is not empty,store the first word in each line in res[]
        if (content.find("NULL") == -1):
            res = re.findall(r'[\=\++\w]+', content)
            #makes a node for each word, prints nodes using dot syntax
            if (res):
                count+=1
                print("\t")
                print("Node" + str(count) + " ")
                print("[shape=record,label=\"{" + str(res[0]))
                
                #if integer literal, print Int value
                if (str(res[0]) == "IntegerLiteral"):
                    print("," + str(res[len(res)-1]))
                
                #if reference to declared variable, print variable name
                if (str(res[0]) == "DeclRefExpr"):
                    if(content.find("arr") != -1):
                        print(",arr")
                    else:
                        print("," + str(res[len(res)-2]))
            
                #if binary or unary operator, print operator
                if ((str(res[0]) == "BinaryOperator") or (str(res[0]) == "UnaryOperator")):
                        if (content.find("'<'") != -1):
                            print(",\<")
                        elif (content.find("'>'") != -1):
                            print(",\>")
                        elif (content.find("'-'") != -1):
                            print("," + content[len(content)-3:len(content)-2])
                        elif (content.find("'&'") != -1):
                            print("," + content[len(content)-19:len(content)-18])
                        else:
                            print("," + str(res[len(res)-1]))
            
                print("}\"];")
                print("\n")

                #uses number of indents to determine relationships between nodes and
                #stores node number on stack and pushing/popping nodes as relationships
                #are defined
                cur_indent = content.find("-")
                
                if (cur_indent>prev_indent):
                    #add node to stack (relationship between new node/prev node)
                    List.append(str(count))
                elif (cur_indent == prev_indent):
                    #two nodes at same level, pop old node and push new node
                    List.pop()
                    List.append(str(count))
                else:
                    #relationship between nodes is more than one indent apart
                    diff = prev_indent - cur_indent
                    diff = int(diff/2)
                    while (diff >= 0):
                        List.pop()
                        diff -= 1
                    List.append(str(count))
                    
                prev_indent = cur_indent

                #prints relationship between two nodes
                if (count>1):
                    print("\t Node" + str(List[len(List)-2]) + " -> Node" + str(List[len(List)-1]) + ";")
                    print("\n")
print("}")
