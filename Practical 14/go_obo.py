#import the necessary libraries
import xml.dom.minidom
import xml.sax
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#start the time for DOM parsing
#parse the file
#set the initial count for each ontology and the total count to zero
#sort the elements under the element "term" out
DOM_start_time = datetime.now()
DOMTree = xml.dom.minidom.parse("C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 14\\go_obo.xml")
collection = DOMTree.documentElement
biological_process_count = 0
cellular_component_count = 0
molecular_function_count = 0
total_count = 0
term = collection.getElementsByTagName("term")  
#loop the sorted elements
#if the elements contain namespace the first node of the element is equal to the three specific ontologies
#add the respective count for each ontology by one
for line in term:
    namespace = line.getElementsByTagName("namespace")[0].firstChild.nodeValue
    total_count += 1
    if namespace == "biological_process":
        biological_process_count += 1
    elif namespace == "cellular_component":
            cellular_component_count += 1
    elif namespace == "molecular_function":
         molecular_function_count += 1

print("Biological_process_count_DOM: " + str(biological_process_count))
print("Cellular_component_count_DOM: " + str(cellular_component_count))
print("Molecular_function_count_DOM: " + str(molecular_function_count))
print(total_count)
#stop the time and calculate the time used for DOM parsing
DOM_end_time = datetime.now()
DOM_used_time = DOM_end_time - DOM_start_time
#start the time for SAX parsing
SAX_start_time = datetime.now()
#create a class as the SAX handler
#check if the namespace is under the element term
#set the intial count for three ontologies to zero
#add a count to the respective ontology if it was encountered
class NamespaceHandler (xml.sax.ContentHandler):
    def __init__(self):
        self.namespace = ""
        self.namespace_interm = False
        self.element_innamespace = False
        self.biological_process_count = 0
        self.cellular_component_count = 0
        self.molecular_function_count = 0
        
    def startElement(self, name, attr):
        if name == "term":
            self.namespace_interm = True
        if self.namespace_interm and name == "namespace":
                self.element_innamespace = True
            
    def endElement(self, name):
        if self.element_innamespace:
            if self.namespace == "biological_process":
                self.biological_process_count += 1
            elif self.namespace == "cellular_component":
                self.cellular_component_count += 1
            elif self.namespace == "molecular_function":
                self.molecular_function_count += 1 
            self.namespace = ""
            self.namespace_interm = False
            self.element_innamespace = False
            
    def characters(self, content):
        if self.element_innamespace:
            self.namespace += content.strip()
#set the parser for SAX
#set the handler from  the class
#parse the file using SAX  
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler = NamespaceHandler()
parser.setContentHandler(Handler)
parser.parse("C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 14\\go_obo.xml")
    
print("Biological_process_count_SAX: " + str(Handler.biological_process_count))
print("Cellular_component_count_SAX: " + str(Handler.cellular_component_count))
print("Molecular_function_count_SAX: " + str(Handler.molecular_function_count))
#stop the time and calculate the time for SAX parsing
SAX_end_time = datetime.now()
SAX_used_time = SAX_end_time - SAX_start_time
print("DOM used time: ", DOM_used_time)
print("SAX used time: ", SAX_used_time)
#plot the results
GO_terms_in_DOM = ["Biological_process", "Cellular_component", "Molecular_function"]
GO_terms_counts_in_DOM = [30794, 4392, 12154]
GO_terms_in_SAX = ["Biological_process", "Cellular_component", "Molecular_function"]
GO_terms_counts_in_SAX = [30794, 4392, 12154]

plt.figure(figsize=(10, 8))
plt.subplot(2,1,1)
plt.bar(GO_terms_in_DOM, GO_terms_counts_in_DOM, width = 0.5)
plt.xlabel("Terms")
plt.ylabel("Count of terms")
plt.title("Occurrences of three specified ontologies")

plt.subplot(2,1,2)
plt.bar(GO_terms_in_SAX, GO_terms_counts_in_SAX, width = 0.5)
plt.xlabel("Terms")
plt.ylabel("Count of terms")
plt.title("Occurrences of three specified ontologies")
plt.tight_layout()
plt.show()
plt.clf()

        
        
