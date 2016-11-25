#! /usr/bin/env python3.

# create ig definition file with all value sets in the /resources directory
import json, os, sys, logging, re
from lxml import etree
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.info('Start of program')
logging.info('The logging module is working.')
# create the ig.json file template as dictoinary
dir='/Users/ehaas/Documents/FHIR/Argo-DSTU2/'
namespaces={'o':'urn:schemas-microsoft-com:office:office',
            'x':'urn:schemas-microsoft-com:office:excel',
            'ss':'urn:schemas-microsoft-com:office:spreadsheet',
            'fhir':'http:/hl7.org/fhir'}
'''
ig_template = open(dir +'ig-template.json')  #ig-template  lack spreadsheet and valueset information
igjson = ig_template.read() # convert to strings
igpy =json.loads(igjson)  # convert to py dict format
'''

logging.info('create the ig.json file template as dictionary')
igpy = {"paths":{"temp":"temp","specification":"http://hl7.org/fhir/DSTU2","qa":"qa","txCache":"txCache","output":"output","pages":"pages","resources":["resources","examples"]},"version":"1.0.2","extraTemplates":["mappings"],"defaults":{"StructureDefinition":{"template-base":"sd.html","template-defns":"sd-definitions.html","template-mappings":"sd-mappings.html"},"ConceptMap":{"template-base":"cm.html"},"Any":{"template-format":"format.html","template-base":"base.html"},"ValueSet":{"template-base":"vs.html"}},"source":"ig.xml","canonicalBase":"http://hl7.org/fhir/us/argonaut","tool":"jekyll","sct-edition":"http://snomed.info/sct/731000124108","spreadsheets":[],"resources":{}}

logging.info('create the ig.xml file template as string')

igxml ='''<?xml version="1.0" encoding="UTF-8"?><!--Hidden IG for de facto IG publishing--><ImplementationGuide xmlns="http://hl7.org/fhir"><id value="ig"/><url value="http://hl7.org/fhir/us/argonaut/ImplementationGuide/ig"/><name value="Implementation Guide Template"/><status value="draft"/><experimental value="true"/><publisher value="FHIR Project"/><package><name value="base"/></package><page><source value="index.html"/><name value="blah"/><kind value="page"/></page></ImplementationGuide>'''



resources = os.listdir(dir + 'resources') # get all the files in the resource directory
vsid_re = re.compile(r'<id value="(.*)"/>') # regex for finding the index in vs
for i in range(len(resources)):# run through all the files looking for spreadsheets and valuesets
    if 'spreadsheet' in resources[i]: # for spreadsheets  append to the igpy[spreadsheet] array.
          igpy['spreadsheets'].append(resources[i])
          logging.info('adding ' + resources[i] + ' to spreadsheets array')
          sd_file = open(dir + 'resources/'+ resources[i]) # for each spreadsheet in /resources open value and read  SD id and create and append dict struct to definiions file
          sdxml = etree.parse(sd_file) # lxml module to parse excel xml
          sdid = sdxml.xpath('/ss:Workbook/ss:Worksheet[2]/ss:Table/ss:Row[11]/ss:Cell[2]/ss:Data', namespaces=namespaces)  # use xpath to get the id from the spreadsheet and lower case

          igpy['resources']['StructureDefinition/' + sdid[0].text.lower()] =  {'base': 'structuredefinition-'+ sdid[0].text.lower() + '.html'} # concat id into appropriate strings and add sd  base def to resources in def file
          logging.info('adding sd ' + sdid[0].text.lower() +' to resources ig.json')

          igpy['resources']['StructureDefinition/' + sdid[0].text.lower()]['defns'] =  'structuredefinition-' + sdid[0].text.lower() + '-definitions.html' # concat id into appropriate strings and add sd defitions to in def file
          logging.info('adding sd definitions ' + sdid[0].text.lower() +  ' definitions to resources ig.json')



    if 'valueset' in resources[i]: # for each vs in /resources open valueset resources and read id and create and append dict struct to definiions file
          vs_file = open(dir + 'resources/'+ resources[i]) # can use a package like untangle or Xmltodict but I'm gonna regex it for now"
          vsxml = vs_file.read()  # convert to string
          vsmo = vsid_re.search(vsxml)  # get match object which contains id
          vsid = vsmo.group(1) #get id as string
          igpy['resources']['ValueSet/' + vsid] =  {'base': 'valueset-'+ vsid + '.html'} # concat id into appropriate strings and add valuset base def to resources in def file
          logging.info('adding valueset ' + vsid +' to resources ig.json')
          vsxml = '<resource><purpose value="terminology"/><sourceReference><reference value="ValueSet/' + vsid + '"/></sourceReference></resource>' # concat id into appropriate string
          igxml = igxml.replace('name value="base"/>','name value="base"/>' + vsxml) # add valuset base def to ig resource
          logging.info('adding valueset ' + vsxml +' to resources in ig.xml')
    if 'capabilitystatement' in resources[i]: # for each cs in /resources open, read id and create and append dict struct to definiions file
          vs_file = open(dir + 'resources/'+ resources[i]) # use the same variables as for valuesets...see above
          vsxml = vs_file.read()  # convert to string
          vsmo = vsid_re.search(vsxml)  # get match object which contains id
          vsid = vsmo.group(1) #get id as string
          igpy['resources']['CapabilityStatement/' + vsid] =  {'base': 'capabilitystatement-'+ vsid + '.html'} # concat id into appropriate strings and add valuset base def to resources in def file
          logging.info('adding capabilitystatement ' + vsid +' to resources ig.json')
          vsxml = '<resource><purpose value="example"/><sourceReference><reference value="CapabilityStatement/' + vsid + '"/></sourceReference></resource>' # concat id into appropriate string
          igxml = igxml.replace('name value="base"/>','name value="base"/>' + vsxml) # add valuset base def to ig resource
          logging.info('adding capabilitystatement ' + vsxml +' to resources in ig.xml')
    if 'operationdefinition' in resources[i]: # for each cs in /resources open, read id and create and append dict struct to definiions file
          vs_file = open(dir + 'resources/'+ resources[i]) # use the same variables as for valuesets...see above
          vsxml = vs_file.read()  # convert to string
          vsmo = vsid_re.search(vsxml)  # get match object which contains id
          vsid = vsmo.group(1) #get id as string
          igpy['resources']['OperationDefinition/' + vsid] =  {'base': 'operationdefinition-'+ vsid + '.html'} # concat id into appropriate strings and add od base def to resources in def file
          logging.info('adding operationdefinition ' + vsid +' to resources ig.json')
          vsxml = '<resource><purpose value="example"/><sourceReference><reference value="OperationDefinition/' + vsid + '"/></sourceReference></resource>' # concat id into appropriate string
          igxml = igxml.replace('name value="base"/>','name value="base"/>' + vsxml) # add valuset base def to ig resource
          logging.info('adding operationdefinition ' + vsxml +' to resources in ig.xml')



#=====adding examples to ig.xml leaving out the ig.json part for know ==============
examples = os.listdir(dir + 'examples') # get all the examples in the examples directory assuming are in json the xml is causing a codec error so json is easier to process
for i in range(len(examples)):# run through all the examples and get id and resource type
    if 'json' in examples[i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
          ex_file = open(dir + 'examples/'+ examples[i]) # for each example in /examples open
          logging.info('load example json file'+ dir + 'examples/'+ examples[i])
          exjson = json.load(ex_file)
          extype = exjson['resourceType']
          ex_id = exjson['id']
          vsxml = '<resource><purpose value="example"/><sourceReference><reference value="'+ extype +'/' + ex_id + '"/></sourceReference></resource>' # concat id into appropriate string
          igxml = igxml.replace('name value="base"/>','name value="base"/>' + vsxml) # add example to ig resource
          logging.info('adding example' + extype+'/' + ex_id +' to resources in ig.xml')


'''======= leaving out the xml parsing============\
          sdxml = etree.parse(sd_file) # lxml module to parse example xml
          sdid = sdxml.xpath('//fhir:id/@value', namespaces=namespaces)  # use xpath to get the id
          extype = sdxml.xpath('name(/*)', namespaces=namespaces)  # use xpath to get the type '''


'''   ===========leaving out the ig.json part for now=========

       igpy['resources'][ extype + '/' + sdid[0].text] =  {'template-base': null}  # add example base def to resources in def file remove base.html
          logging.info('adding example' + extype + '/' + sdid[0].text + ' =  {template-base: null} to resources ig.json')

          igpy['resources'][ extype + '/' + sdid[0].text]['example'] = + extype.lower() + '-' + sdid[0].text+ '.html' # concat id into appropriate strings and add example in def file
          logging.info('adding example:' extype.lower() + '-' + sdid[0].text+ '.html to resources ig.json')
'''



# ig_file = open(dir + 'ig.json','w')
# ig_file.write(json.dumps(igpy)) # convert dict to json and replace ig.json with this file
logging.info('ig.json now looks like : ' + json.dumps(igpy))

# ig_file = open(dir + 'resources/ig.xml','w')
# ig_file.write(igxml) # convert dict to json and replace ig.json with this file
logging.info('ig.xml now looks like : ' + igxml)

logging.info('End of program')
