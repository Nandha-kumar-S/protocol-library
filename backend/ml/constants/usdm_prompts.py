class Objectivesandendpoints:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information from the "protocol section" and populate the schema while maintaining the original structure.

Chain of command:
Step 1: Analyze the USDM Schema
Thoroughly analyze the provided USDM schema template. Identify and understand all required information, paying close attention to each attribute's purpose, Understand the definition of every attribute, and note the required format for each field (e.g., string, integer). Also recognize that many attributes can be nested. For example, a Section class like Objective may contain an Endpoint attribute, which itself is a Section with its own nested attributes.
Step 2: Analyze the Clinical Protocol Content
Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information relevant to the section you are mapping to the USDM schema. Ensure you capture every piece of information from the protocol that is required by the USDM template.
Step 3: Populate the USDM Schema
Fill the USDM section schema template with the relevant information extracted from the protocol. For each section (e.g., Objective, Endpoint), provide a unique, arbitrary identifier that is relevant to the section (e.g., OBJ1, Endpoint_001).Provide a descriptive name for each section that reflects its content in the protocol, and Populate all other attributes according to their definitions and the data you extracted from the protocol.
Step 4: Final Output
Present the final output in a valid JSON format.

Notes to keep in mind:

1. Every section class should have an "extensionAttributes" attribute, in case one aims to amend that section later on. Similarly every section needs to have an "instanceType" attribute for better search and identification functionality. An instance type attribute is defined as a string that explicitly declares what the JSON object represents. In a complex, nested data structure, this is vital for parsing and interpreting the data correctly.
2. When no explicit notes are provided in the protocol section, leave the notes section blank.
3. do not fill in the code for the sections and fill a place holder starting with CNCIt-001, do not add your own code value.
4. Review the example provided so you have an idea of how the input is interpreted and output json needs to be

Example:
"""

        EXAMPLE_INPUT = """

"""

        EXAMPLE_OUTPUT = """

"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Activity:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information from "protocol section" and populate the schema while maintaining the original structure.

Chain of command:
Step 1: Analyze the USDM Schema
Thoroughly analyze the provided USDM schema template. Identify and understand all required information, paying close attention to each attribute's purpose, Understand the definition of every attribute, and note the required format for each field (e.g., string, integer). for any attribute with cardinality, provide a unique label, for example for definedprocedures within activity, provide a unique id procedure_001, and move on to the next attribute.
Step 2: Analyze the Clinical Protocol Content
Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information relevant to the section you are mapping to the USDM schema. Ensure you capture every piece of information from the protocol that is required by the USDM template.
Step 3: Populate the USDM Schema
Fill the USDM section schema template with the relevant information extracted from the protocol. For each usdm class, provide a unique, arbitrary identifier that is relevant to the section (e.g., ACT_001, Activity_001).Provide a descriptive name for each section that reflects its content in the protocol, and Populate all other attributes according to their definitions and the data you extracted from the protocol.
Step 4: Final Output
Present the final output in a valid JSON format.

Notes to keep in mind:

1. Every section class should have an "extensionAttributes" attribute whihc must be null. similarly every section needs to have an "instanceType" attribute. An instance type attribute is defined as string that explicitly declares what the JSON object represents.
2. When no explicit notes are provided in the protocol section, leave the notes section blank.
3. do not fill in the code for the sections and fill a place holder starting with CNCIt-001, do not add your own code value.
4. Review the example provided so you have an idea of how the input is interpreted and output json needs to be


Example:
"""

        EXAMPLE_INPUT = """

"""

        EXAMPLE_OUTPUT = """

"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class StudyAmendment:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information from "protocol section" and populate the schema while maintaining the original structure.

Chain of command:
Step 1: Analyze the USDM Schema
Thoroughly analyze the provided USDM schema template. Identify and understand all required information, paying close attention to each attribute's purpose, Understand the definition of every attribute, and note the required format for each field (e.g., string, integer). for any attribute with any type of cardinality, provide a unique label, for example for GeographicScope within study amendements, provide a unique id geographicScope_001, and move on to the next attribute. do not attempt to fit information inattributes with cardinality.
Step 2: Analyze the Clinical Protocol Content
Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information relevant to the section you are mapping to the USDM schema. Ensure you capture every piece of information from the protocol that is required by the USDM template.
Step 3: Populate the USDM Schema
Fill the USDM section schema template with the relevant information extracted from the protocol. For each usdm class, provide a unique, arbitrary identifier that is relevant to the section (e.g., AMEND_001, AMEND_002).Provide a descriptive name for each section that reflects its content in the protocol, and Populate all other attributes according to their definitions and the data you extracted from the protocol.
Step 4: Final Output
Present the final output in a valid JSON format.

Notes to keep in mind:

1. Every section class should have an "extensionAttributes" attribute which must be null. Similarly every section needs to have an "instanceType" attribute. An instance type attribute is defined as a string that explicitly declares what the JSON object represents.
2. When no explicit notes are provided in the protocol section, leave the notes section blank.
3. do not fill in the code for the sections and fill a place holder starting with CNCIt-001, do not add your own code value.
4. Review the example provided so you have an idea of how the input is interpreted and output json needs to be 


Example:
"""

        EXAMPLE_INPUT = """

"""

        EXAMPLE_OUTPUT = """

"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class StudyAmendmentImpact:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information from the "protocol section" and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyAmendmentImpact. Understand each attribute's purpose, data type, and cardinality. For any attribute with cardinality, provide a unique label (e.g., geographicScope_001).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information relevant to the section you are mapping to the USDM schema. Ensure you capture every piece of information from the protocol that is required by the USDM template.
Populate the USDM Schema: Fill the StudyAmendmentImpact schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Impact_001). Populate the attributes text, isSubstantial, type, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyAmendmentImpact").
When no explicit notes are provided in the protocol section, leave the notes attribute as an empty string "".
Do not fill in the code for the sections and use a placeholder starting with CNCIt-001. Do not add your own code value. Code system and code version will always be http://www.cdisc.org and 2024-09-27. The decode should be relevant to the data it is representing.
Remember that isSubstantial is a boolean and must be true or false.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON


{
  "title": "10.7. Protocol Amendment History",
  "extracted_text": "Amendment 1 was substantial, updating procedures in the Schedule of Activities, removing contradictory text on SAE reporting, and adding details on interim analysis."
}
"""

        EXAMPLE_OUTPUT = """
JSON


impacts": [
              {
                "id": "StudyAmendmentImpact_1",
                "extensionAttributes": [],
                "type": {
                  "id": "CNCIt_001",
                  "extensionAttributes": [],
                  "code": "CNCIt_00",
                  "codeSystem": "http://www.cdisc.org",
                  "codeSystemVersion": "2024-09-27",
                  "decode": "Study Data Robustness",
                  "instanceType": "Code"
                },
                "text": "Amendment 1",
                "isSubstantial": true,
                "notes": [],
                "instanceType": "StudyAmendmentImpact"
              }
            ],
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class StudyAmendmentReason:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information from the "protocol section" and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyAmendmentImpact. Understand each attribute's purpose, data type, and cardinality. For any attribute with cardinality, provide a unique label (e.g., geographicScope_001).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information relevant to the section you are mapping to the USDM schema. Ensure you capture every piece of information from the protocol that is required by the USDM template.
Populate the USDM Schema: Fill the StudyAmendmentImpact schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., StudyAmendmentReason_001). 
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyAmendmentReason").
When no explicit notes are provided in the protocol section, leave the notes attribute as an empty string "".
Do not fill in the code for the sections and use a placeholder starting with CNCIt-001. Do not add your own code value. Code system and code version will always be http://www.cdisc.org and 2024-09-27. The decode should be relevant to the data it is representing.
Remember that other reasons should be left blank
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON


{
  "title": "10.7. Protocol Amendment History",
  "extracted_text": "Amendment 1 was substantial, updating procedures in the Schedule of Activities, removing contradictory text on SAE reporting, and adding details on interim analysis."
}
"""

        EXAMPLE_OUTPUT = """
JSON
"primaryReason": {
              "id": "StudyAmendmentReason_1",
              "extensionAttributes": [],
              "code": {
                "id": "CNCIt_001",
                "extensionAttributes": [],
                "code": "CNCIt_001",
                "codeSystem": "http://www.cdisc.org",
                "codeSystemVersion": "2024-09-27",
                "decode": "Protocol Design Error",
                "instanceType": "Code"
              },
              "otherReason": null,
              "instanceType": "StudyAmendmentReason"
            },
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Abbreviations:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information from the "protocol section" and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyAmendmentImpact. Understand each attribute's purpose, data type, and cardinality. For any attribute with cardinality, provide a unique label (e.g., geographicScope_001).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information relevant to the section you are mapping to the USDM schema. Ensure you capture every piece of information from the protocol that is required by the USDM template.
Populate the USDM Schema: Fill the Abbreviation schema template with the relevant information extracted from the protocol. For each abbreviation, provide a unique, arbitrary identifier (e.g., Abbreviation_001). Populate the attributes abbreviatedText, expandedText, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Abbreviation").
abbreviatedText is the short form (e.g., "AE"), while expandedText is the full term (e.g., "Adverse Event").
When no explicit notes are provided, leave the notes attribute as an empty string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "List of Abbreviations",
  "extracted_text": "•    AE: Adverse Event•    ECG: Electrocardiogram•    SAE: Serious Adverse Event"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "abbreviations": [
    {
      "id": "Abbreviation_001",
      "instanceType": "Abbreviation",
      "extensionAttributes": null,
      "abbreviatedText": "AE",
      "expandedText": "Adverse Event",
      "notes": ""
    },
    {
      "id": "Abbreviation_002",
      "instanceType": "Abbreviation",
      "extensionAttributes": null,
      "abbreviatedText": "ECG",
      "expandedText": "Electrocardiogram",
      "notes": ""
    },
    {
      "id": "Abbreviation_003",
      "instanceType": "Abbreviation",
      "extensionAttributes": null,
      "abbreviatedText": "SAE",
      "expandedText": "Serious Adverse Event",
      "notes": ""
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Address:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information from the "protocol section" and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyAmendmentImpact. Understand each attribute's purpose, data type, and cardinality. For any attribute with cardinality, provide a unique label (e.g., geographicScope_001).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information relevant to the section you are mapping to the USDM schema. Ensure you capture every piece of information from the protocol that is required by the USDM template.
Populate the USDM Schema: Fill the Address schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Address_001). Populate the attributes text, lines, district, city, postalCode, state, and country according to the data you extracted.
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Address").
The text attribute should contain the full, unsegmented address string, while the other attributes (lines, city, etc.) should contain the segmented parts.
The country attribute should be a Code object, and you should use the CNCIt-001 placeholder for the code ID.
If any address component (like district or state) is not explicitly provided, leave it blank.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Contact Information",
  "extracted_text": "Sponsor: Alexion Pharmaceuticals, Inc.Address: 121 Seaport Boulevard, Boston, MA 02210, USA"
}
"""

        EXAMPLE_OUTPUT = """
JSON
"legalAddress": {
              "id": "Address_1",
              "extensionAttributes": [],
              "text": "121 Seaport Boulevard, Boston, , MA, 02210, United States of America",
              "lines": [
                "121 Seaport Boulevard"
              ],
              "city": "Boston",
              "district": "",
              "state": "MA",
              "postalCode": "02210",
              "country": {
                "id": "CNCIt_001",
                "extensionAttributes": [],
                "code": "CNCIt_001",
                "codeSystem": "http://www.cdisc.org",
                "codeSystemVersion": "2024-09-27",
                "decode": "United States of America",
                "instanceType": "Code"
              },
              "instanceType": "Address"
            },
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Administration:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about product, agent, or therapy administration and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Administration. Understand each attribute's purpose, data type, and cardinality. Pay special attention to nested classes like Quantity, AliasCode, AdministrationDuration, AdministrableProduct, and MedicalDevice. For any attribute with a cardinality, provide a unique identifier (e.g., AdministrableProduct_001).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information related to how products or therapies are administered, including dose, frequency, route, and duration.
Populate the USDM Schema: Fill the Administration schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Administration_001). For each administration, populate the attributes name, description, label, dose, frequency, route, notes, administrableProduct, duration, and medicalDevice according to the data you extracted.
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Administration").
The dose attribute is a Quantity object, which requires a value and a unit. Both unit, frequency, and route are AliasCode objects and need an id and a nested standardCode with an id and name. Use the placeholder CNCIt-001 for the code id.
The duration attribute is a mandatory AdministrationDuration object and must have its own id and instanceType. It also contains a nested Quantity object for the duration value and unit.
The administrableProduct and medicalDevice attributes are relationships. If information for these is present, link to their respective objects via their unique identifiers (e.g., administrableProductId: "AdministrableProduct_001").
When a field is not explicitly mentioned in the protocol, like label or notes, leave it as an empty string "" or an empty array [] as appropriate.
The name attribute should be a unique literal identifier, often a combination of dose and product.
Review the provided examples to see how each nested object (Quantity, AliasCode, Duration) is structured and populated.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.3. Justification for Dose",
  "extracted_text": "1: ALXN1840 at 60 mg single dose has been shown to have an adequate safety profile and be well-tolerated in healthy participants.2: In the Phase 2 Study WTX101-201, daily ALXN1840 doses were 15 mg for 6 participants, 30 mg for 13 participants, and 60 mg for 9 participants at Week 24"
}
"""

        EXAMPLE_OUTPUT = """
JSON
"administrations": [
              {
                "id": "Administration_1",
                "extensionAttributes": [],
                "name": "15_MG",
                "label": "",
                "description": "15 mg/day",
                "duration": {
                  "id": "Duration_1",
                  "extensionAttributes": [],
                  "text": "",
                  "quantity": {
                    "id": "Quantity_5",
                    "extensionAttributes": [],
                    "value": 28.0,
                    "unit": {
                      "id": "AliasCode_101",
                      "extensionAttributes": [],
                      "standardCode": {
                        "id": "Code_535",
                        "extensionAttributes": [],
                        "code": "C25301",
                        "codeSystem": "http://www.cdisc.org",
                        "codeSystemVersion": "2024-09-27",
                        "decode": "Day",
                        "instanceType": "Code"
                      },
                      "standardCodeAliases": [],
                      "instanceType": "AliasCode"
                    },
                    "instanceType": "Quantity"
                  },
                  "durationWillVary": true,
                  "reasonDurationWillVary": "Need reason",
                  "instanceType": "Duration"
                },
                "dose": {
                  "id": "Quantity_6",
                  "extensionAttributes": [],
                  "value": 15.0,
                  "unit": {
                    "id": "AliasCode_102",
                    "extensionAttributes": [],
                    "standardCode": {
                      "id": "Code_536",
                      "extensionAttributes": [],
                      "code": "C28253",
                      "codeSystem": "http://www.cdisc.org",
                      "codeSystemVersion": "2024-09-27",
                      "decode": "Milligram",
                      "instanceType": "Code"
                    },
                    "standardCodeAliases": [],
                    "instanceType": "AliasCode"
                  },
                  "instanceType": "Quantity"
                },
                "route": {
                  "id": "AliasCode_103",
                  "extensionAttributes": [],
                  "standardCode": {
                    "id": "Code_537",
                    "extensionAttributes": [],
                    "code": "C38288",
                    "codeSystem": "http://www.cdisc.org",
                    "codeSystemVersion": "2024-09-27",
                    "decode": "Oral Route of Administration",
                    "instanceType": "Code"
                  },
                  "standardCodeAliases": [],
                  "instanceType": "AliasCode"
                },
                "frequency": {
                  "id": "AliasCode_104",
                  "extensionAttributes": [],
                  "standardCode": {
                    "id": "Code_538",
                    "extensionAttributes": [],
                    "code": "C25473",
                    "codeSystem": "http://www.cdisc.org",
                    "codeSystemVersion": "2024-09-27",
                    "decode": "Daily",
                    "instanceType": "Code"
                  },
                  "standardCodeAliases": [],
                  "instanceType": "AliasCode"
                },
                "administrableProductId": null,
                "medicalDeviceId": null,
                "notes": [],
                "instanceType": "Administration"
              },
              {
                "id": "Administration_2",
                "extensionAttributes": [],
                "name": "30_MG",
                "label": "",
                "description": "30 mg/day (administered as 2 \u00d7 15 mg ALXN1840 tablets)",
                "duration": {
                  "id": "Duration_2",
                  "extensionAttributes": [],
                  "text": "",
                  "quantity": {
                    "id": "Quantity_8",
                    "extensionAttributes": [],
                    "value": 11.0,
                    "unit": {
                      "id": "AliasCode_106",
                      "extensionAttributes": [],
                      "standardCode": {
                        "id": "Code_543",
                        "extensionAttributes": [],
                        "code": "C25301",
                        "codeSystem": "http://www.cdisc.org",
                        "codeSystemVersion": "2024-09-27",
                        "decode": "Day",
                        "instanceType": "Code"
                      },
                      "standardCodeAliases": [],
                      "instanceType": "AliasCode"
                    },
                    "instanceType": "Quantity"
                  },
                  "durationWillVary": true,
                  "reasonDurationWillVary": "Need reason",
                  "instanceType": "Duration"
                },
                "dose": {
                  "id": "Quantity_9",
                  "extensionAttributes": [],
                  "value": 30.0,
                  "unit": {
                    "id": "AliasCode_107",
                    "extensionAttributes": [],
                    "standardCode": {
                      "id": "Code_544",
                      "extensionAttributes": [],
                      "code": "C28253",
                      "codeSystem": "http://www.cdisc.org",
                      "codeSystemVersion": "2024-09-27",
                      "decode": "Milligram",
                      "instanceType": "Code"
                    },
                    "standardCodeAliases": [],
                    "instanceType": "AliasCode"
                  },
                  "instanceType": "Quantity"
                },
                "route": {
                  "id": "AliasCode_108",
                  "extensionAttributes": [],
                  "standardCode": {
                    "id": "Code_545",
                    "extensionAttributes": [],
                    "code": "C38288",
                    "codeSystem": "http://www.cdisc.org",
                    "codeSystemVersion": "2024-09-27",
                    "decode": "Oral Route of Administration",
                    "instanceType": "Code"
                  },
                  "standardCodeAliases": [],
                  "instanceType": "AliasCode"
                },
                "frequency": {
                  "id": "AliasCode_109",
                  "extensionAttributes": [],
                  "standardCode": {
                    "id": "Code_546",
                    "extensionAttributes": [],
                    "code": "C25473",
                    "codeSystem": "http://www.cdisc.org",
                    "codeSystemVersion": "2024-09-27",
                    "decode": "Daily",
                    "instanceType": "Code"
                  },
                  "standardCodeAliases": [],
                  "instanceType": "AliasCode"
                },
                "administrableProductId": null,
                "medicalDeviceId": null,
                "notes": [],
                "instanceType": "Administration"
              }
            ],
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class AdministrableProduct:
        ROLE_TEMPLATE = """
You are a clinical data management and protocol analysis expert.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the investigational product and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for AdministrableProduct. Understand each attribute's purpose, data type, and cardinality. For any attribute with a cardinality (e.g., identifiers), provide a unique label (e.g., productIdentifier_001).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information relevant to the investigational product and its properties. Ensure you capture every piece of information that is required by the USDM template.
Populate the USDM Schema: Fill the AdministrableProduct schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Product_001). Populate the attributes name, description, label, administrableDoseForm, sourcing, productDesignation, pharmacologicClass, and notes according to the data you extracted. For attributes with cardinality, provide a unique label for each instance.
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "AdministrableProduct").
For attributes that point to a Code or AliasCode object, use the CNCIt-001 placeholder for the code ID.
The administrableDoseForm should be a short, recognizable term (e.g., "Tablet"), which is an AliasCode. The other codes, like sourcing, productDesignation, and pharmacologicClass should be Code objects.
If the protocol describes a product but doesn't provide explicit values for an attribute like pharmacologicClass, leave that attribute blank.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "6.4 Study Intervention",
  "extracted_text": "The investigational medicinal product, ALXN1840, is provided as 15 mg tablets for oral administration. It is a chelating agent and a zinc-based molecule. The product is centrally sourced."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
    "products": [
        {
            "id": "AdministrableProduct_001",
            "instanceType": "AdministrableProduct",
            "extensionAttributes": null,
            "name": "ALXN1840",
            "description": "ALXN1840 is an investigational medicinal product provided as 15 mg tablets for oral administration.",
            "label": "ALXN1840 15 mg Tablets",
            "administrableDoseForm": {
                "id": "AliasCode_001",
                "instanceType": "AliasCode",
                "standardCode": {
                    "id": "Code_CNCIt-001",
                    "name": "Tablet"
                }
            },
            "sourcing": {
                "id": "Code_CNCIt-001",
                "name": "Central Source"
            },
            "productDesignation": {
                "id": "Code_CNCIt-001",
                "name": "Investigational Medicinal Product"
            },
            "pharmacologicClass": {
                "id": "Code_CNCIt-001",
                "name": "Chelating Agent"
            },
            "notes": "",
            "identifiers": [],
            "properties": [],
            "ingredients": []
        }
    ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class AdministrableProductIdentifier:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the administrable product's identifiers and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for AdministrableProductIdentifier. Understand each attribute's purpose, data type, and cardinality. Note the required format for each field (e.g., string). Pay close attention to the scope attribute, which is a required relationship to the Organization class.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract any identifiers, codes, or text used to name or characterize the investigational product.
Populate the USDM Schema: Fill the AdministrableProductIdentifier schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ProductIdentifier_001). Populate the attributes text and scope according to the data you extracted.
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "AdministrableProductIdentifier").
The text attribute should contain the literal identifier string (e.g., "ALXN1840").
The scope attribute is a required relationship. You must link it to a pre-defined or newly created Organization object (e.g., an organization with the ID Organization_001). This is crucial because an identifier is assigned by an organization.
If the protocol provides an identifier without explicitly naming the assigning organization, use a generic placeholder organization (e.g., Organization_Sponsor).
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Drug",
  "extracted_text": "The study drug, known as ALXN1840, is manufactured by Alexion Pharmaceuticals, Inc."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "administrableProductIdentifiers": [
    {
      "id": "AdministrableProductIdentifier_001",
      "instanceType": "AdministrableProductIdentifier",
      "extensionAttributes": null,
      "text": "ALXN1840",
      "scope": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "name": "Alexion Pharmaceuticals, Inc."
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Administrableproductproperty:
        ROLE_TEMPLATE = """
You are a clinical data management and protocol analysis expert.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the administrable product's properties and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for AdministrableProductProperty. Understand each attribute's purpose, data type, and cardinality. Note that the quantity attribute is a nested Quantity object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract any quantifiable or descriptive characteristics of the investigational product, such as strength, concentration, or other defining attributes.
Populate the USDM Schema: Fill the AdministrableProductProperty schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ProductProperty_001). Populate the attributes name, type, text, and quantity according to the data you extracted.
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "AdministrableProductProperty").
The type attribute is a Code object and should be populated with a placeholder ID (CNCIt-001).
The quantity attribute is a nested Quantity object, which requires both a value (a number) and a unit (another nested object, typically an AliasCode).
The text attribute can be used for descriptive properties that are not quantifiable. If the property is a quantity, the text field may be left blank.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Product Description",
  "extracted_text": "The study drug is available as a 15 mg tablet. The concentration is 100 mg/mL."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "administrableProductProperties": [
    {
      "id": "AdministrableProductProperty_001",
      "instanceType": "AdministrableProductProperty",
      "extensionAttributes": null,
      "name": "Tablet Strength",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Strength"
      },
      "text": "",
      "quantity": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "value": 15.0,
        "unit": {
          "id": "AliasCode_001",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Milligram"
          }
        }
      }
    },
    {
      "id": "AdministrableProductProperty_002",
      "instanceType": "AdministrableProductProperty",
      "extensionAttributes": null,
      "name": "Concentration",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Concentration"
      },
      "text": "100 mg/mL",
      "quantity": {
        "id": "Quantity_002",
        "instanceType": "Quantity",
        "value": 100.0,
        "unit": {
          "id": "AliasCode_002",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "mg/mL"
          }
        }
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class AdministrationDuration:
        ROLE_TEMPLATE = """
You are a clinical data management and protocol analysis expert.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the duration of a product administration and populate the schema while maintaining the original structure.
Chain of Command:
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for AdministrationDuration. Understand each attribute's purpose, data type, and cardinality. Note that the quantity attribute is a nested Quantity object, and the durationWillVary attribute is a boolean.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract information related to how long a treatment is administered, including any specified timeframes, whether the duration is expected to change, and the reason for any variation.
Populate the USDM Schema: Fill the AdministrationDuration schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Duration_001). Populate the attributes description, quantity, durationWillVary, and reasonDurationWillVary according to the data you extracted.
Final Output: Present the final output in a valid JSON format.
Notes to keep in mind:
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "AdministrationDuration").
The quantity attribute is a nested Quantity object and should include both a value (a number) and a unit (a nested AliasCode).
The durationWillVary attribute must be a boolean value (true or false).
The reasonDurationWillVary attribute should be populated with the specific rationale if durationWillVary is true. If durationWillVary is false, this attribute should be left blank.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Duration",
  "extracted_text": "Participants will receive the study intervention for a period of up to 12 weeks. The duration may vary based on subject response and tolerability."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "durations": [
    {
      "id": "AdministrationDuration_001",
      "instanceType": "AdministrationDuration",
      "extensionAttributes": null,
      "description": "Participants will receive the study intervention for a period of up to 12 weeks.",
      "quantity": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "value": 12.0,
        "unit": {
          "id": "AliasCode_001",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Week"
          }
        }
      },
      "durationWillVary": true,
      "reasonDurationWillVary": "The duration may vary based on subject response and tolerability."
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Analysispopulation:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the analysis populations and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for AnalysisPopulation. Understand each attribute's purpose, data type, and cardinality. Note that subsetOf is a relationship with a cardinality of 0..*.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that define the populations for analysis. Your goal is to extract all information relevant to these populations, including their names, descriptions, and any criteria used to define them.
Populate the USDM Schema: Fill the AnalysisPopulation schema template with the relevant information extracted from the protocol. For each analysis population, provide a unique, arbitrary identifier (e.g., AnalysisPopulation_001). Populate the attributes name, text, description, label, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "AnalysisPopulation").
The name attribute is a literal identifier (e.g., "ITT Population").
The text attribute can be used for any unstructured text from the protocol that defines the population. The description attribute is for a more detailed narrative.
The subsetOf relationship can be linked to other PopulationDefinition objects by their identifiers, but for this task, a placeholder like PopulationDefinition_001 will suffice.
If a field is not explicitly mentioned in the protocol, leave it blank.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "9.3 Populations for Analysis",
  "extracted_text": "All analyses of primary endpoints will be performed on the Intent-to-Treat (ITT) Population, which consists of all randomized patients who receive at least one dose of study medication. A Per Protocol (PP) Population will also be used for supportive analyses. The Per Protocol set was updated in Amendment 1."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "analysisPopulations": [
    {
      "id": "AnalysisPopulation_001",
      "instanceType": "AnalysisPopulation",
      "extensionAttributes": null,
      "name": "Intent-to-Treat Population",
      "text": "All randomized patients who receive at least one dose of study medication.",
      "description": "All randomized patients who receive at least one dose of study medication.",
      "label": "ITT",
      "notes": "",
      "subsetOf": []
    },
    {
      "id": "AnalysisPopulation_002",
      "instanceType": "AnalysisPopulation",
      "extensionAttributes": null,
      "name": "Per Protocol Population",
      "text": "The Per Protocol set was updated in Amendment 1.",
      "description": "A Per Protocol (PP) Population will also be used for supportive analyses.",
      "label": "PP",
      "notes": "",
      "subsetOf": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class AssignedPerson:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about assigned personnel and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for AssignedPerson. Understand each attribute's purpose, data type, and cardinality. Note that the organization attribute is an optional relationship to the Organization class.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that list key personnel. Your goal is to extract all relevant information for each person, including their name, job title, and the organization they belong to.
Populate the USDM Schema: Fill the AssignedPerson schema template with the relevant information extracted from the protocol. For each assigned person, provide a unique, arbitrary identifier (e.g., Person_001). Populate the attributes name, description, label, jobTitle, and organization according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "AssignedPerson").
The name attribute should capture the full name of the person.
The organization attribute is a relationship. You must link it to a pre-defined or newly created Organization object by its identifier (e.g., organization: { "id": "Organization_001" }).
If a field, such as description or label, is not explicitly mentioned, leave it as a blank string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Signature Page",
  "extracted_text": "Study Sponsor: Alexion Pharmaceuticals, Inc.Principal Investigator: Dr. Jane Doe, M.D., Department of Clinical Research"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "assignedPersons": [
    {
      "id": "AssignedPerson_001",
      "instanceType": "AssignedPerson",
      "extensionAttributes": null,
      "name": "Jane Doe",
      "description": "",
      "label": "Dr. Jane Doe, M.D.",
      "jobTitle": "Principal Investigator",
      "organization": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "extensionAttributes": null,
        "name": "Department of Clinical Research"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class BiospecimenRetention:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about biospecimen retention and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for BiospecimenRetention. Understand each attribute's purpose, data type, and cardinality. Note that the attributes isRetained and includesDNA are boolean values.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that discuss the collection, storage, and future use of biological samples. Your goal is to extract all relevant information, including whether samples will be stored, for how long, and if they contain DNA.
Populate the USDM Schema: Fill the BiospecimenRetention schema template with the relevant information extracted from the protocol. For each instance of biospecimen retention, provide a unique, arbitrary identifier (e.g., BiospecimenRetention_001). Populate the attributes name, description, label, isRetained, and includesDNA according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "BiospecimenRetention").
isRetained and includesDNA must be a boolean value (true or false).
The name attribute should be a unique literal identifier for the retention policy (e.g., "Future Research Sample Storage").
If a field is not explicitly mentioned in the protocol, such as label or description, leave it as a blank string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "7.5 Biospecimen Handling",
  "extracted_text": "Residual blood samples will be stored for future genetic analysis. These samples contain DNA and will be retained indefinitely for future research related to this study's disease area. Informed consent for this retention is obtained from all participants."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "biospecimenRetentions": [
    {
      "id": "BiospecimenRetention_001",
      "instanceType": "BiospecimenRetention",
      "extensionAttributes": null,
      "name": "Residual Blood Sample Retention",
      "description": "Residual blood samples will be stored indefinitely for future research related to this study's disease area.",
      "label": "Genetic Sample Storage",
      "isRetained": true,
      "includesDNA": true
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Characteristic:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the distinguishing qualities or aspects of an entity (e.g., a population, a disease) and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Characteristic. Understand each attribute's purpose, data type, and cardinality. Note that the dictionary attribute is an optional relationship to the SyntaxTemplateDictionary class.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract any descriptions or attributes that define or distinguish a particular entity within the protocol (e.g., specific inclusion/exclusion criteria, a disease state, a patient's condition).
Populate the USDM Schema: Fill the Characteristic schema template with the relevant information extracted from the protocol. For each characteristic, provide a unique, arbitrary identifier (e.g., Characteristic_001). Populate the attributes name, description, label, text, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Characteristic").
The name attribute is a literal identifier for the characteristic (e.g., "Confirmed Diagnosis of WD").
The text attribute can be used for the exact text from the protocol that defines the characteristic. The description attribute can be used for a more narrative representation.
If a field is not explicitly mentioned, such as label or notes, leave it as a blank string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "5.1 Inclusion Criteria",
  "extracted_text": "Inclusion criterion for confirmation of diagnosis of WD changed to Leipzig score ≥ 4 and expanded to include historical test results."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "characteristics": [
    {
      "id": "Characteristic_001",
      "instanceType": "Characteristic",
      "extensionAttributes": null,
      "name": "Confirmed Diagnosis of WD",
      "description": "Confirmation of diagnosis of WD changed to Leipzig score ≥ 4 and expanded to include historical test results.",
      "label": "Leipzig score ≥ 4",
      "text": "Leipzig score ≥ 4 and expanded to include historical test results.",
      "notes": ""
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Condition:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a state of being and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Condition. Understand each attribute's purpose, data type, and cardinality. Note the relationships to context and appliesTo, which have a cardinality of 0..*.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract any descriptions of a patient's health status, disease state, or other qualifying medical conditions, particularly those found in inclusion/exclusion criteria or adverse event sections.
Populate the USDM Schema: Fill the Condition schema template with the relevant information extracted from the protocol. For each condition, provide a unique, arbitrary identifier (e.g., Condition_001). Populate the attributes name, description, label, text, and notes according to the data you extracted. For attributes with cardinality like context and appliesTo, provide unique labels (e.g., Activity_001).
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Condition").
The name attribute is a literal identifier for the condition.
The text attribute can be used for the exact, unstructured text from the protocol that describes the condition. The description attribute is for a more narrative representation.
The context and appliesTo attributes are relationships. You should link to other relevant objects (e.g., Activity, Procedure) using their unique identifiers. If these linked objects are not explicitly defined in the provided text, use a placeholder ID like Activity_001.
If a field, such as label or notes, is not explicitly mentioned, leave it as a blank string "" or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "5.2 Exclusion Criteria",
  "extracted_text": "Exclusion criterion 1: Current or prior diagnosis of primary biliary cholangitis."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "conditions": [
    {
      "id": "Condition_001",
      "instanceType": "Condition",
      "extensionAttributes": null,
      "name": "Primary Biliary Cholangitis",
      "description": "Current or prior diagnosis of primary biliary cholangitis.",
      "label": "Primary Biliary Cholangitis Diagnosis",
      "text": "Current or prior diagnosis of primary biliary cholangitis.",
      "notes": "",
      "context": [],
      "appliesTo": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Conditionassignment:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the logical conditions that govern a study decision or action and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ConditionAssignment. Understand each attribute's purpose, data type, and cardinality. Note that conditionTarget is a mandatory relationship to a ScheduledInstance class.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract any logical rules, criteria, or assumptions that trigger a specific event or action, such as a patient's transition to a new phase, a change in treatment, or the discontinuation of a study.
Populate the USDM Schema: Fill the ConditionAssignment schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ConditionAssignment_001). Populate the attributes condition and conditionTarget according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ConditionAssignment").
The condition attribute should contain the logical condition as a string (e.g., "if patient meets X criteria").
The conditionTarget is a mandatory relationship. You must link it to a ScheduledInstance object by its unique identifier (e.g., conditionTarget: { "id": "ScheduledInstance_001" }). This object represents the specific event or schedule item to which the condition applies.
If the protocol provides a condition without explicitly naming the target instance, use a generic placeholder (e.g., ScheduledInstance_Transition).
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Flow",
  "extracted_text": "Patients will continue in the treatment phase until they meet the criteria for study completion or early discontinuation."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "conditionAssignments": [
    {
      "id": "ConditionAssignment_001",
      "instanceType": "ConditionAssignment",
      "extensionAttributes": null,
      "condition": "patient meets the criteria for study completion or early discontinuation",
      "conditionTarget": {
        "id": "ScheduledInstance_001",
        "instanceType": "ScheduledInstance",
        "description": "Patients will continue in the treatment phase until they meet the criteria for study completion or early discontinuation."
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Documentcontentreference:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a document content reference and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for DocumentContentReference. Understand each attribute's purpose, data type, and cardinality. Note that the appliesTo attribute is a mandatory relationship to a StudyDefinitionDocument class.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract information that cites or points to a specific section within the document. This is often found in tables of contents, cross-references, or mentions of other protocol sections.
Populate the USDM Schema: Fill the DocumentContentReference schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., DocRef_001). Populate the attributes sectionNumber, sectionTitle, and appliesTo according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "DocumentContentReference").
The sectionNumber should contain the numeric or alphanumeric identifier of the section (e.g., "10.7").
The sectionTitle should contain the title of the section (e.g., "Protocol Amendment History").
The appliesTo is a mandatory relationship. You must link it to a pre-defined StudyDefinitionDocument object by its unique identifier (e.g., appliesTo: { "id": "Protocol_001" }). This object represents the main protocol document itself. If not explicitly mentioned, assume the reference is to the current protocol.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Document History",
  "extracted_text": "Protocol Amendment Summary of Changes Table is located directly before the Table of Contents."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "documentContentReferences": [
    {
      "id": "DocumentContentReference_001",
      "instanceType": "DocumentContentReference",
      "extensionAttributes": null,
      "sectionNumber": "",
      "sectionTitle": "Protocol Amendment Summary of Changes Table",
      "appliesTo": {
        "id": "StudyDefinitionDocument_001",
        "instanceType": "StudyDefinitionDocument",
        "extensionAttributes": null,
        "name": "Protocol"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Eligibilitycriterion:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about study eligibility criteria (inclusion and exclusion criteria) and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for EligibilityCriterion. Understand each attribute's purpose, data type, and cardinality. Note the relationships to criterionItem, next, and previous.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that define eligibility. Your goal is to extract all individual criteria, their numeric or textual identifiers, and whether they are inclusion or exclusion criteria.
Populate the USDM Schema: Fill the EligibilityCriterion schema template with the relevant information extracted from the protocol. For each criterion, provide a unique, arbitrary identifier (e.g., EligibilityCriterion_001). Populate the attributes name, description, label, identifier, category, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "EligibilityCriterion").
The identifier attribute should contain the numeric or alphanumeric label of the criterion (e.g., "1", "11").
The category attribute is a Code object that specifies if the criterion is an Inclusion or Exclusion criterion. Use the CNCIt-001 placeholder for the code ID.
The criterionItem is a mandatory relationship to an EligibilityCriterionItem object. You should create and link to this object using a unique identifier.
The next and previous attributes are for linking criteria in a list. You should use the id of the subsequent or preceding criterion to populate these fields. If a criterion is the first or last in the list, leave the corresponding field as null.
If a field is not explicitly mentioned, leave it as a blank string "" or null as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "5.2 Exclusion criteria",
  "extracted_text": "Exclusion criterion for drug screen revised to state that cannabinoids will not be tested. ... Exclusion criterion 11 revised to “The use of an experimental or unapproved/unlicensed therapy..."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "eligibilityCriteria": [
    {
      "id": "EligibilityCriterion_001",
      "instanceType": "EligibilityCriterion",
      "extensionAttributes": null,
      "name": "Exclusion for drug screen",
      "description": "Exclusion criterion for drug screen revised to state that cannabinoids will not be tested.",
      "label": "Drug Screen",
      "identifier": null,
      "category": {
        "id": "Code_CNCIt-001",
        "name": "Exclusion"
      },
      "notes": "",
      "criterionItem": {
        "id": "EligibilityCriterionItem_001",
        "instanceType": "EligibilityCriterionItem",
        "extensionAttributes": null,
        "description": "Exclusion criterion for drug screen revised to state that cannabinoids will not be tested."
      },
      "next": {
        "id": "EligibilityCriterion_002"
      },
      "previous": null
    },
    {
      "id": "EligibilityCriterion_002",
      "instanceType": "EligibilityCriterion",
      "extensionAttributes": null,
      "name": "Exclusion for experimental therapy",
      "description": "Exclusion criterion 11 revised to “The use of an experimental or unapproved/unlicensed therapy...",
      "label": "Experimental Therapy",
      "identifier": "11",
      "category": {
        "id": "Code_CNCIt-001",
        "name": "Exclusion"
      },
      "notes": "",
      "criterionItem": {
        "id": "EligibilityCriterionItem_002",
        "instanceType": "EligibilityCriterionItem",
        "extensionAttributes": null,
        "description": "The use of an experimental or unapproved/unlicensed therapy at the same time or within 90 days or 5 half-lives, whichever is longer, prior to the Screening Visit."
      },
      "next": null,
      "previous": {
        "id": "EligibilityCriterion_001"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Eligibilitycriterionitem:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract the core textual content of an individual eligibility criterion and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for EligibilityCriterionItem. Understand each attribute's purpose, data type, and cardinality. Note that the dictionary attribute is an optional relationship.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract the specific text that defines each inclusion or exclusion criterion, as this forms the basis of the criterion item.
Populate the USDM Schema: Fill the EligibilityCriterionItem schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., EligibilityCriterionItem_001). Populate the attributes name, description, label, text, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "EligibilityCriterionItem").
The text attribute should contain the exact, verbatim text of the criterion from the protocol.
The description attribute can be a narrative representation, which may be the same as or a slightly refined version of the text.
The name and label attributes should be concise identifiers for the criterion item.
If a field, such as notes, is not explicitly mentioned, leave it as a blank string "".
Remember that EligibilityCriterionItem is a nested class within EligibilityCriterion. Your output should reflect this hierarchy.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "5.2 Exclusion criteria",
  "extracted_text": "Exclusion criterion 11 revised to “The use of an experimental or unapproved/unlicensed therapy at the same time or within 90 days or 5 half-lives, whichever is longer, prior to the Screening Visit.”"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "eligibilityCriterionItems": [
    {
      "id": "EligibilityCriterionItem_001",
      "instanceType": "EligibilityCriterionItem",
      "extensionAttributes": null,
      "name": "Experimental Therapy Use",
      "description": "The use of an experimental or unapproved/unlicensed therapy prior to the Screening Visit.",
      "label": "Experimental Therapy Use",
      "text": "The use of an experimental or unapproved/unlicensed therapy at the same time or within 90 days or 5 half-lives, whichever is longer, prior to the Screening Visit.",
      "notes": ""
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Encounter:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about study encounters (visits) and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Encounter. Understand each attribute's purpose, data type, and cardinality. Note the optional relationships to transitionEndRule, transitionStartRule, scheduledAt, next, and previous.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections like the Schedule of Events or Visit Schedule. Your goal is to extract all information related to each study visit, including its name, description, type, and the location or mode of contact.
Populate the USDM Schema: Fill the Encounter schema template with the relevant information extracted from the protocol. For each encounter, provide a unique, arbitrary identifier (e.g., Encounter_001). Populate the attributes name, description, label, type, environmentalSettings, contactModes, and notes according to the data you extracted. For relationships, provide unique identifiers (e.g., TransitionRule_001).
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Encounter").
The name attribute should be a literal identifier for the visit (e.g., "Screening Visit").
The type, environmentalSettings, and contactModes attributes are Code objects. Use the CNCIt-001 placeholder for the code ID.
The next and previous relationships can be used to represent the chronological order of visits. Use the id of the next or previous encounter to populate these fields.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.2 Schedule of Activities",
  "extracted_text": "Patients will participate in an in-person Screening Visit (Day -28 to Day -1), followed by a clinic visit for the start of treatment. A follow-up phone call will be made 30 days after the last dose."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "encounters": [
    {
      "id": "Encounter_001",
      "instanceType": "Encounter",
      "extensionAttributes": null,
      "name": "Screening Visit",
      "description": "The Screening Visit is an in-person visit.",
      "label": "Screening Visit",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Screening"
      },
      "environmentalSettings": {
        "id": "Code_CNCIt-001",
        "name": "Clinic"
      },
      "contactModes": {
        "id": "Code_CNCIt-001",
        "name": "In-person"
      },
      "notes": "",
      "transitionEndRule": null,
      "next": {
        "id": "Encounter_002"
      },
      "transitionStartRule": null,
      "scheduledAt": {
        "id": "Timing_001",
        "instanceType": "Timing",
        "description": "Day -28 to Day -1"
      },
      "previous": null
    },
    {
      "id": "Encounter_002",
      "instanceType": "Encounter",
      "extensionAttributes": null,
      "name": "Follow-up Phone Call",
      "description": "A follow-up phone call will be made 30 days after the last dose.",
      "label": "Follow-up",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Follow-up"
      },
      "environmentalSettings": {
        "id": "Code_CNCIt-001",
        "name": "Home"
      },
      "contactModes": {
        "id": "Code_CNCIt-001",
        "name": "Phone"
      },
      "notes": "",
      "transitionEndRule": null,
      "next": null,
      "transitionStartRule": null,
      "scheduledAt": {
        "id": "Timing_002",
        "instanceType": "Timing",
        "description": "30 days after the last dose"
      },
      "previous": {
        "id": "Encounter_001"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Endpoint:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about study endpoints and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Endpoint. Understand each attribute's purpose, data type, and cardinality. Pay close attention to the level attribute, which is a Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that define the study's objectives and outcomes. Your goal is to extract all information related to the endpoints, including their names, descriptions, purpose, and level of importance (e.g., primary, secondary).
Populate the USDM Schema: Fill the Endpoint schema template with the relevant information extracted from the protocol. For each endpoint, provide a unique, arbitrary identifier (e.g., Endpoint_001). Populate the attributes name, description, label, text, notes, level, and purpose according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Endpoint").
The name attribute should be a literal identifier for the endpoint (e.g., "Change from Baseline in VAS Pain Score").
The level attribute is a Code object that classifies the endpoint's importance (e.g., "Primary", "Secondary", "Exploratory"). Use the CNCIt-001 placeholder for the code ID.
The purpose attribute should contain the textual rationale for the endpoint.
If a field, such as label or notes, is not explicitly mentioned, leave it as a blank string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "8.1 Primary Objective and Endpoint",
  "extracted_text": "The primary objective is to evaluate the efficacy of the study drug. The primary endpoint is the change from baseline in the Visual Analog Scale (VAS) pain score at 12 weeks. An interim analysis will be performed on this data to support a Marketing Authorisation Application."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "endpoints": [
    {
      "id": "Endpoint_001",
      "instanceType": "Endpoint",
      "extensionAttributes": null,
      "name": "Change from Baseline in VAS Pain Score",
      "description": "The primary endpoint is the change from baseline in the Visual Analog Scale (VAS) pain score at 12 weeks.",
      "label": "Primary Endpoint",
      "text": "change from baseline in the Visual Analog Scale (VAS) pain score at 12 weeks.",
      "notes": "Interim analysis will be performed on this data.",
      "level": {
        "id": "Code_CNCIt-001",
        "name": "Primary"
      },
      "purpose": "To evaluate the efficacy of the study drug."
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Estimand:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the study's estimand, a precise description of the treatment effect, and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Estimand. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationships to analysisPopulation, variableOfInterest (an Endpoint), intercurrentEvents, and interventions.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections related to statistical analysis and study objectives. Your goal is to identify the core components of the estimand: the population, the variable being measured, the interventions being compared, and how intercurrent events are handled.
Populate the USDM Schema: Fill the Estimand schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Estimand_001). Populate the attributes name, description, label, populationSummary, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Estimand").
The analysisPopulation, variableOfInterest, intercurrentEvents, and interventions attributes are mandatory relationships. You must link these to their respective objects by their unique identifiers (e.g., analysisPopulation: { "id": "AnalysisPopulation_001" }).
The populationSummary provides a synopsis of the endpoint of interest within the target population.
If the protocol describes multiple estimands, create a separate JSON object for each one.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "9.4 Estimands and Sensitivity Analyses",
  "extracted_text": "The primary estimand is defined as the effect of the study drug versus placebo on change from baseline in VAS pain score at 12 weeks for the Intent-to-Treat (ITT) population, assuming all patients take their assigned treatment. The estimand addresses the question 'What is the effect of receiving the treatment over the specified time period?'"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "estimands": [
    {
      "id": "Estimand_001",
      "instanceType": "Estimand",
      "extensionAttributes": null,
      "name": "Primary Estimand",
      "description": "The effect of the study drug versus placebo on change from baseline in VAS pain score at 12 weeks.",
      "label": "Treatment effect on VAS pain score",
      "populationSummary": "The effect of the study drug versus placebo on change from baseline in VAS pain score at 12 weeks for the Intent-to-Treat (ITT) population.",
      "notes": "",
      "analysisPopulation": {
        "id": "AnalysisPopulation_001",
        "instanceType": "AnalysisPopulation",
        "name": "Intent-to-Treat Population"
      },
      "variableOfInterest": {
        "id": "Endpoint_001",
        "instanceType": "Endpoint",
        "name": "Change from Baseline in VAS Pain Score"
      },
      "intercurrentEvents": [
        {
          "id": "IntercurrentEvent_001",
          "instanceType": "IntercurrentEvent",
          "name": "Treatment Discontinuation"
        }
      ],
      "interventions": [
        {
          "id": "StudyIntervention_001",
          "instanceType": "StudyIntervention",
          "name": "Study Drug"
        },
        {
          "id": "StudyIntervention_002",
          "instanceType": "StudyIntervention",
          "name": "Placebo"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Geographicscope:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the geographic scope of a study and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for GeographicScope. Understand each attribute's purpose, data type, and cardinality. Note that both type and code are objects that reference controlled terminologies.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that describe the study's location, such as "Participating Countries" or "Geographic Scope." Your goal is to extract information about the countries, regions, or the overall scope of the study.
Populate the USDM Schema: Fill the GeographicScope schema template with the relevant information extracted from the protocol. For each geographic scope, provide a unique, arbitrary identifier (e.g., GeographicScope_001). Populate the attributes type and code according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "GeographicScope").
The type attribute is a Code object that should describe the kind of geographic scope (e.g., "Country," "Region," "Global"). Use the CNCIt-001 placeholder for the code ID.
The code attribute is an AliasCode object. Its standardCode should be a nested Code object representing the country or region (e.g., "United States of America"). Use the CNCIt-001 placeholder for the code ID. The AliasCode structure is designed to handle multiple naming conventions, but for this task, focus on the primary name.
If the protocol mentions multiple countries or regions, you must create a separate GeographicScope object for each one.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Scope",
  "extracted_text": "This study will be conducted in the United States and Canada. Amendment 3.1 (US) applies only to the United States."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "geographicScopes": [
    {
      "id": "GeographicScope_001",
      "instanceType": "GeographicScope",
      "extensionAttributes": null,
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Country"
      },
      "code": {
        "id": "AliasCode_001",
        "instanceType": "AliasCode",
        "standardCode": {
          "id": "Code_CNCIt-001",
          "name": "United States of America"
        }
      }
    },
    {
      "id": "GeographicScope_002",
      "instanceType": "GeographicScope",
      "extensionAttributes": null,
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Country"
      },
      "code": {
        "id": "AliasCode_002",
        "instanceType": "AliasCode",
        "standardCode": {
          "id": "Code_CNCIt-001",
          "name": "Canada"
        }
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Governancedate:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about study governance dates and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for GovernanceDate. Understand each attribute's purpose, data type, and cardinality. Note that the type attribute is a Code object, the dateValue is a date, and geographicScopes is a relationship with a cardinality of 1..*.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on tables or sections that list document history, key milestones, or effective dates. Your goal is to extract the date, its associated type, and any relevant geographic information.
Populate the USDM Schema: Fill the GovernanceDate schema template with the relevant information extracted from the protocol. For each date, provide a unique, arbitrary identifier (e.g., GovernanceDate_001). Populate the attributes name, description, label, type, dateValue, and geographicScopes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "GovernanceDate").
The dateValue attribute must be in a valid date format (e.g., "YYYY-MM-DD").
The type attribute is a Code object that classifies the date (e.g., "Protocol Effective Date," "Amendment Date"). Use the CNCIt-001 placeholder for the code ID.
The geographicScopes attribute is a mandatory relationship to one or more GeographicScope objects. You should link to these objects by their unique identifiers (e.g., geographicScopes: [{"id": "GeographicScope_001"}]).
If a field is not explicitly mentioned, such as description or label, leave it as a blank string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "DOCUMENT HISTORY",
  "extracted_tables": [
    {
      "data": [
        ["Document", "Date"],
        ["Original Protocol", "12 May 2020"],
        ["Amendment 1", "18 Aug 2020"],
        ["Amendment 3.1 (US)", "18 Mar 2022"]
      ]
    }
  ],
  "extracted_text": "Amendment 3.1 (US) applies only to the United States."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "governanceDates": [
    {
      "id": "GovernanceDate_001",
      "instanceType": "GovernanceDate",
      "extensionAttributes": null,
      "name": "Original Protocol Date",
      "description": "",
      "label": "Original Protocol Date",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Original Protocol Date"
      },
      "dateValue": "2020-05-12",
      "geographicScopes": []
    },
    {
      "id": "GovernanceDate_002",
      "instanceType": "GovernanceDate",
      "extensionAttributes": null,
      "name": "Amendment 1 Date",
      "description": "",
      "label": "Amendment 1 Date",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Amendment Effective Date"
      },
      "dateValue": "2020-08-18",
      "geographicScopes": []
    },
    {
      "id": "GovernanceDate_003",
      "instanceType": "GovernanceDate",
      "extensionAttributes": null,
      "name": "Amendment 3.1 (US) Date",
      "description": "This amendment applies only to the United States.",
      "label": "Amendment 3.1 (US) Date",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Amendment Effective Date"
      },
      "dateValue": "2022-03-18",
      "geographicScopes": [
        {
          "id": "GeographicScope_001",
          "instanceType": "GeographicScope",
          "extensionAttributes": null,
          "type": {
            "id": "Code_CNCIt-001",
            "name": "Country"
          },
          "code": {
            "id": "AliasCode_001",
            "instanceType": "AliasCode",
            "standardCode": {
              "id": "Code_CNCIt-001",
              "name": "United States of America"
            }
          }
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Identifier:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about study identifiers and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Identifier. Understand each attribute's purpose, data type, and cardinality. Note that the scope attribute is a mandatory relationship to the Organization class.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract any official identifiers for the study, such as trial numbers, registration numbers (e.g., ClinicalTrials.gov ID), or sponsor protocol numbers.
Populate the USDM Schema: Fill the Identifier schema template with the relevant information extracted from the protocol. For each identifier, provide a unique, arbitrary identifier (e.g., Identifier_001). Populate the attributes text and scope according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Identifier").
The text attribute should contain the literal identifier string (e.g., "NCT01234567" or "ALXN1840-C-201").
The scope attribute is a mandatory relationship. You must link it to a pre-defined or newly created Organization object by its unique identifier (e.g., scope: { "id": "Organization_001" }). This object represents the assigning organization, such as a sponsor or registry.
If the protocol provides an identifier without explicitly naming the assigning organization, use a generic placeholder organization (e.g., Organization_Sponsor or Organization_Registry).
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Identification",
  "extracted_text": "Sponsor Protocol Number: ALXN1840-C-201ClinicalTrials.gov Identifier: NCT01234567"
}
**
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "identifiers": [
    {
      "id": "Identifier_001",
      "instanceType": "Identifier",
      "extensionAttributes": null,
      "text": "ALXN1840-C-201",
      "scope": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "name": "Alexion Pharmaceuticals, Inc."
      }
    },
    {
      "id": "Identifier_002",
      "instanceType": "Identifier",
      "extensionAttributes": null,
      "text": "NCT01234567",
      "scope": {
        "id": "Organization_002",
        "instanceType": "Organization",
        "name": "ClinicalTrials.gov"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Indication:
        ROLE_TEMPLATE = """
You're a clinical data management and protocol analysis expert.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the disease or condition the study's intervention is designed to address and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Indication. Understand each attribute's purpose, data type, and cardinality. Note that isRareDisease is a boolean and codes is a Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract all information related to the specific disease or condition being studied. Look for details in sections like the Synopsis, Introduction, or Study Objectives.
Populate the USDM Schema: Fill the Indication schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Indication_001). Populate the attributes name, description, label, isRareDisease, codes, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Indication").
The name attribute should be the literal name of the disease or condition (e.g., "Wilson disease").
The isRareDisease attribute must be a boolean value (true or false) based on whether the protocol identifies the condition as a rare disease.
The codes attribute is a Code object. Use the CNCIt-001 placeholder for the code ID, as multiple external coding systems can apply.
If a field, such as label or notes, is not explicitly mentioned, leave it as a blank string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "2.2 Background",
  "extracted_text": "The development of ALXN1840 is for Wilson disease, a rare inherited disorder that causes copper to accumulate in the liver, brain, and other vital organs."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "indications": [
    {
      "id": "Indication_001",
      "instanceType": "Indication",
      "extensionAttributes": null,
      "name": "Wilson disease",
      "description": "A rare inherited disorder that causes copper to accumulate in the liver, brain, and other vital organs.",
      "label": "Wilson disease",
      "isRareDisease": true,
      "codes": [
        {
          "id": "Code_CNCIt-001",
          "name": "Wilson disease"
        }
      ],
      "notes": ""
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Ingredient:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the components of a study product and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Ingredient. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationships to role (a Code object) and substance (a Substance object).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that describe the composition of the study drug or placebo. Your goal is to identify each component, its function (e.g., active, inactive), and the substance itself.
Populate the USDM Schema: Fill the Ingredient schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Ingredient_001). Populate the attributes role and substance according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Ingredient").
The role attribute is a Code object that should describe the ingredient's function (e.g., "active ingredient", "excipient"). Use the CNCIt-001 placeholder for the code ID.
The substance attribute is a mandatory relationship to a Substance object. You must create and link to this object using a unique identifier. This object will contain the details of the substance itself.
If the protocol lists multiple ingredients, create a separate Ingredient object for each one.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Drug Formulation",
  "extracted_text": "The study drug is composed of the active substance ALXN1840. The tablets also contain inactive ingredients like microcrystalline cellulose."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "ingredients": [
    {
      "id": "Ingredient_001",
      "instanceType": "Ingredient",
      "extensionAttributes": null,
      "role": {
        "id": "Code_CNCIt-001",
        "name": "Active Ingredient"
      },
      "substance": {
        "id": "Substance_001",
        "instanceType": "Substance",
        "extensionAttributes": null,
        "name": "ALXN1840"
      }
    },
    {
      "id": "Ingredient_002",
      "instanceType": "Ingredient",
      "extensionAttributes": null,
      "role": {
        "id": "Code_CNCIt-001",
        "name": "Excipient"
      },
      "substance": {
        "id": "Substance_002",
        "instanceType": "Substance",
        "extensionAttributes": null,
        "name": "Microcrystalline Cellulose"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Intercurrentevent:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about intercurrent events—events that occur after a participant begins treatment and affect the interpretation of the study results—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for IntercurrentEvent. Understand each attribute's purpose, data type, and cardinality. Note the strategy attribute, which describes how these events are managed.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any events that may disrupt the study flow or affect outcome measurements, such as medication non-adherence, premature discontinuation of treatment, or a rescue medication being administered. Also, find the protocol's plan for handling these events.
Populate the USDM Schema: Fill the IntercurrentEvent schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., IntercurrentEvent_001). Populate the attributes name, description, label, text, notes, and strategy according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "IntercurrentEvent").
The name attribute should be a concise identifier for the event (e.g., "Treatment Discontinuation").
The strategy attribute should contain the textual description of how the event is handled in the analysis (e.g., "Missing data will be imputed using a multiple imputation model").
If a field, such as label or notes, isn't explicitly mentioned, leave it as a blank string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "9.4 Estimands and Sensitivity Analyses",
  "extracted_text": "Premature discontinuation of study treatment is a common intercurrent event. The primary analysis will handle this by using the 'treatment policy strategy,' which means participants who discontinue will remain in their assigned treatment group for analysis, and any subsequent data will be included."
}
**
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "intercurrentEvents": [
    {
      "id": "IntercurrentEvent_001",
      "instanceType": "IntercurrentEvent",
      "extensionAttributes": null,
      "name": "Premature Discontinuation of Treatment",
      "description": "An event where a participant discontinues study treatment prematurely.",
      "label": "Premature Discontinuation",
      "text": "Premature discontinuation of study treatment.",
      "notes": "",
      "strategy": "The primary analysis will handle this by using the 'treatment policy strategy,' which means participants who discontinue will remain in their assigned treatment group for analysis, and any subsequent data will be included."
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Interventionalstudydesign:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the overall strategy and structure of an interventional trial and populate the schema while maintaining the original structure. This is a large class with many attributes, so pay close attention to detail.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for InterventionalStudyDesign. Understand each attribute's purpose, data type, and cardinality. Note the many optional relationships with a cardinality of 0..* or 1..*. For all attributes with a cardinality other than null, you should only provide an identifier and move on.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that describe the study's overall design, methodology, and rationale. Your goal is to extract all information related to the study's type, phase, intervention model, blinding, and key components like arms, epochs, and populations.
Populate the USDM Schema: Fill the InterventionalStudyDesign schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for the instance (e.g., InterventionalStudyDesign_001). Populate the attributes name, description, label, rationale, therapeuticAreas, studyType, characteristics, studyPhase, notes, model, subTypes, blindingSchema, and intentTypes. For all relationships with a cardinality (activities, biospecimenRetentions, encounters, estimands, indications, objectives, scheduleTimelines, arms, studyCells, documentVersions, elements, studyInterventions, epochs, population), just provide their respective unique identifiers and do not attempt to fit information into them. For example, for arms, use arms: ["StudyArm_001", "StudyArm_002"].
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "InterventionalStudyDesign").
For attributes that point to a Code or AliasCode object, use the CNCIt-001 placeholder for the code ID.
Pay close attention to the data types: studyPhase is an AliasCode, while therapeuticAreas, studyType, characteristics, model, subTypes, and intentTypes are Code objects.
When an attribute has a cardinality greater than 1 (e.g., 1..*), you must provide a unique identifier for each instance in an array. For example, arms: ["StudyArm_001", "StudyArm_002"].
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Overall Design",
  "extracted_text": "This is a Phase 2, open-label, multicenter, randomized clinical trial to assess the efficacy and safety of ALXN1840. The study population consists of adults with Wilson disease. The study includes a Screening Period, a Treatment Period, and a Follow-up Period. Patients will be randomized to one of two treatment arms: high dose or low dose."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "interventionalStudyDesign": {
    "id": "InterventionalStudyDesign_001",
    "instanceType": "InterventionalStudyDesign",
    "extensionAttributes": null,
    "name": "ALXN1840 Phase 2 Study Design",
    "description": "A Phase 2, open-label, multicenter, randomized clinical trial to assess the efficacy and safety of ALXN1840.",
    "label": "Phase 2 Clinical Trial",
    "rationale": "To assess the efficacy and safety of ALXN1840.",
    "therapeuticAreas": {
      "id": "Code_CNCIt-001",
      "name": "Wilson disease"
    },
    "studyType": {
      "id": "Code_CNCIt-001",
      "name": "Interventional"
    },
    "characteristics": [
      {
        "id": "Code_CNCIt-001",
        "name": "Multicenter"
      }
    ],
    "studyPhase": {
      "id": "AliasCode_001",
      "instanceType": "AliasCode",
      "standardCode": {
        "id": "Code_CNCIt-001",
        "name": "Phase 2"
      }
    },
    "notes": "",
    "activities": [
      {
        "id": "Activity_001"
      }
    ],
    "biospecimenRetentions": [],
    "encounters": [
      {
        "id": "Encounter_001"
      }
    ],
    "estimands": [],
    "indications": [
      {
        "id": "Indication_001"
      }
    ],
    "objectives": [
      {
        "id": "Objective_001"
      }
    ],
    "scheduleTimelines": [
      {
        "id": "ScheduleTimeline_001"
      }
    ],
    "arms": [
      {
        "id": "StudyArm_001"
      },
      {
        "id": "StudyArm_002"
      }
    ],
    "studyCells": [
      {
        "id": "StudyCell_001"
      }
    ],
    "documentVersions": [],
    "elements": [],
    "studyInterventions": [
      {
        "id": "StudyIntervention_001"
      }
    ],
    "epochs": [
      {
        "id": "StudyEpoch_001"
      },
      {
        "id": "StudyEpoch_002"
      },
      {
        "id": "StudyEpoch_003"
      }
    ],
    "population": {
      "id": "StudyDesignPopulation_001"
    },
    "model": {
      "id": "Code_CNCIt-001",
      "name": "Parallel Assignment"
    },
    "subTypes": [],
    "blindingSchema": {
      "id": "AliasCode_002",
      "instanceType": "AliasCode",
      "standardCode": {
        "id": "Code_CNCIt-001",
        "name": "Open-label"
      }
    },
    "intentTypes": []
  }
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Masking:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's masking (blinding) strategy and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Masking. Understand each attribute's purpose, data type, and cardinality. Note that isMasked is a boolean.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to find all information related to how the study is blinded. This information is often found in the design section and will describe who is unaware of the treatment assignments (e.g., patient, investigator, data analyst). Also, look for any details on how the blinding is achieved.
Populate the USDM Schema: Fill the Masking schema template with the relevant information extracted from the protocol. For each instance of masking, provide a unique, arbitrary identifier (e.g., Masking_001). Populate the attributes text and isMasked according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Masking").
The text attribute should contain the details on how the masking is performed, such as "double-blinded with identical-looking tablets."
The isMasked attribute must be a boolean value (true or false).
Remember that masking can apply to different roles. If the protocol specifies different blinding statuses for different roles (e.g., "patient is blinded, but the pharmacist is not"), you might need to create a separate Masking object for each scenario.
If a field is not explicitly mentioned, leave it as a blank string "".
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Overall Design",
  "extracted_text": "This study is an open-label trial. Patients and investigators will be aware of the treatment they are receiving."
}
**
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "masking": [
    {
      "id": "Masking_001",
      "instanceType": "Masking",
      "extensionAttributes": null,
      "text": "Patients and investigators will be aware of the treatment they are receiving.",
      "isMasked": false
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Medicaldevice:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about any medical devices used in the study and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for MedicalDevice. Understand each attribute's purpose, data type, and cardinality. Note the optional relationships to embeddedProduct and identifiers.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any details about devices, equipment, or software used for an intervention or assessment, including their name, description, and versions.
Populate the USDM Schema: Fill the MedicalDevice schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., MedicalDevice_001). Populate the attributes name, description, label, hardwareVersion, softwareVersion, sourcing, and notes according to the data you extracted. For relationships, provide unique identifiers (e.g., embeddedProduct: { "id": "AdministrableProduct_001" }).
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "MedicalDevice").
The sourcing attribute is a Code object that indicates if the device is obtained from a local or central source. Use the CNCIt-001 placeholder for the code ID.
The embeddedProduct and identifiers attributes are optional relationships. If the protocol mentions a product embedded in a device or specific device identifiers (e.g., a serial number), you should link to their respective objects by their unique identifiers.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Materials",
  "extracted_text": "The continuous glucose monitoring device (CGM), version 2.1, will be provided to all participants from a central depot. The device is used to collect glucose level data. This device is not a combination product."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "medicalDevices": [
    {
      "id": "MedicalDevice_001",
      "instanceType": "MedicalDevice",
      "extensionAttributes": null,
      "name": "Continuous Glucose Monitoring Device",
      "description": "The device is used to collect glucose level data. This device is not a combination product.",
      "label": "CGM",
      "hardwareVersion": null,
      "softwareVersion": "2.1",
      "sourcing": {
        "id": "Code_CNCIt-001",
        "name": "Central Source"
      },
      "notes": "",
      "embeddedProduct": null,
      "identifiers": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Medicaldeviceidentifier:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the identifiers for any medical devices used in a study and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for MedicalDeviceIdentifier. Understand each attribute's purpose, data type, and cardinality. Note that scope is a mandatory relationship to the Organization class and type is a Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract any official identifiers, such as serial numbers, model numbers, or UDI (Unique Device Identification) numbers, that are used to identify a medical device.
Populate the USDM Schema: Fill the MedicalDeviceIdentifier schema template with the relevant information extracted from the protocol. For each identifier, provide a unique, arbitrary identifier (e.g., MedicalDeviceIdentifier_001). Populate the attributes text, type, and scope according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "MedicalDeviceIdentifier").
The text attribute should contain the literal identifier string (e.g., "MDI-54321").
The type attribute is a Code object that classifies the identifier (e.g., "Serial Number", "Model Number"). Use the CNCIt-001 placeholder for the code ID.
The scope attribute is a mandatory relationship. You must link it to a pre-defined or newly created Organization object by its unique identifier. This organization represents the entity that assigned the identifier, such as the manufacturer or a regulatory body.
If a field is not explicitly mentioned, leave it blank.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Materials",
  "extracted_text": "The continuous glucose monitoring device has a model number CGM-X100 and a unique serial number, which will be logged for each participant."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "medicalDeviceIdentifiers": [
    {
      "id": "MedicalDeviceIdentifier_001",
      "instanceType": "MedicalDeviceIdentifier",
      "extensionAttributes": null,
      "text": "CGM-X100",
      "scope": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "name": "Device Manufacturer"
      },
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Model Number"
      }
    },
    {
      "id": "MedicalDeviceIdentifier_002",
      "instanceType": "MedicalDeviceIdentifier",
      "extensionAttributes": null,
      "text": "serial number",
      "scope": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "name": "Device Manufacturer"
      },
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Serial Number"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Narrativecontent:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the structure and organization of a document section and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for NarrativeContent. Understand each attribute's purpose, data type, and cardinality. Note the relationships to contentItem, previous, next, and children.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract the title and number of the document section, as well as the content it contains.
Populate the USDM Schema: Fill the NarrativeContent schema template with the relevant information extracted from the protocol. For each section, provide a unique, arbitrary identifier (e.g., NarrativeContent_001). Populate the attributes name, sectionNumber, sectionTitle, displaySectionTitle, and displaySectionNumber according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "NarrativeContent").
The name attribute should be a literal identifier for the narrative content (e.g., "Document History").
displaySectionTitle and displaySectionNumber must be boolean values (true or false).
The contentItem, previous, next, and children attributes are relationships. You should link to other NarrativeContent or NarrativeContentItem objects using their unique identifiers. If the protocol provides a nested structure, use the children relationship to model it.
If a field is not explicitly mentioned, leave it as a blank string "" or null as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "10.7. Protocol Amendment History",
  "extracted_text": "1: Protocol Amendment Summary of Changes Table is located directly before the Table of Contents."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "narrativeContents": [
    {
      "id": "NarrativeContent_001",
      "instanceType": "NarrativeContent",
      "extensionAttributes": null,
      "name": "Protocol Amendment History",
      "sectionNumber": "10.7",
      "sectionTitle": "Protocol Amendment History",
      "displaySectionTitle": true,
      "displaySectionNumber": true,
      "contentItem": {
        "id": "NarrativeContentItem_001",
        "instanceType": "NarrativeContentItem",
        "extensionAttributes": null,
        "text": "1: Protocol Amendment Summary of Changes Table is located directly before the Table of Contents."
      },
      "previous": null,
      "next": null,
      "children": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Narrativecontentitem:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract the core textual content of a document section and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for NarrativeContentItem. Understand each attribute's purpose, data type, and cardinality.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to extract the specific, unstructured text that forms the body of a protocol section.
Populate the USDM Schema: Fill the NarrativeContentItem schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., NarrativeContentItem_001). Populate the attributes name and text according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "NarrativeContentItem").
The text attribute should contain the exact, verbatim text from the protocol section.
The name attribute should be a concise identifier for the content item, often derived from its purpose or a key phrase.
Remember that NarrativeContentItem is a nested class within NarrativeContent. Your output should reflect this hierarchy.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "10.7. Protocol Amendment History",
  "extracted_text": "1: Protocol Amendment Summary of Changes Table is located directly before the Table of Contents."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "narrativeContentItems": [
    {
      "id": "NarrativeContentItem_001",
      "instanceType": "NarrativeContentItem",
      "extensionAttributes": null,
      "name": "Amendment Summary Table Location",
      "text": "1: Protocol Amendment Summary of Changes Table is located directly before the Table of Contents."
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Objective:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's objectives and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Objective. Understand each attribute's purpose, data type, and cardinality. Note the level attribute (a Code object) and the endpoints relationship (a cardinality of 0..*).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to find sections that state the purpose or goal of the study. This is often found in the introduction or dedicated "Objectives" section. You'll extract the core question being asked and its level of importance (e.g., primary, secondary).
Populate the USDM Schema: Fill the Objective schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Objective_001). Populate the attributes name, description, label, text, notes, and level. For the endpoints relationship, simply provide the unique identifiers of the relevant Endpoint objects (e.g., endpoints: [{"id": "Endpoint_001"}]).
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Objective").
The name attribute should be a concise identifier for the objective (e.g., "Primary Efficacy Objective").
The level attribute is a Code object that specifies the objective's importance (e.g., "Primary", "Secondary"). Use the CNCIt-001 placeholder for the code ID.
The endpoints attribute is a relationship to a list of Endpoint objects. Do not nest the full Endpoint object; just list its ID.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "8.1 Primary Objective and Endpoint",
  "extracted_text": "The primary objective is to evaluate the efficacy of the study drug. The secondary objective is to assess the drug's safety and tolerability. The primary endpoint is the change from baseline in the Visual Analog Scale (VAS) pain score."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "objectives": [
    {
      "id": "Objective_001",
      "instanceType": "Objective",
      "extensionAttributes": null,
      "name": "Efficacy Evaluation",
      "description": "To evaluate the efficacy of the study drug.",
      "label": "Primary Objective",
      "text": "The primary objective is to evaluate the efficacy of the study drug.",
      "notes": "",
      "level": {
        "id": "Code_CNCIt-001",
        "name": "Primary"
      },
      "endpoints": [
        {
          "id": "Endpoint_001"
        }
      ]
    },
    {
      "id": "Objective_002",
      "instanceType": "Objective",
      "extensionAttributes": null,
      "name": "Safety and Tolerability Assessment",
      "description": "To assess the drug's safety and tolerability.",
      "label": "Secondary Objective",
      "text": "The secondary objective is to assess the drug's safety and tolerability.",
      "notes": "",
      "level": {
        "id": "Code_CNCIt-001",
        "name": "Secondary"
      },
      "endpoints": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Observationalstudydesign:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the overall strategy and structure of an observational study and populate the schema while maintaining the original structure. This is a large class with many attributes, so pay close attention to detail.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ObservationalStudyDesign. Understand each attribute's purpose, data type, and cardinality. Note the many optional relationships with a cardinality of 0..* or 1..*. For all attributes with a cardinality other than null, you should only provide an identifier and move on.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that describe the study's overall design, methodology, and rationale. Your goal is to extract all information related to the study's type, phase, observation model, time perspective, and key components like arms, epochs, and populations.
Populate the USDM Schema: Fill the ObservationalStudyDesign schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for the instance (e.g., ObservationalStudyDesign_001). Populate the attributes name, description, label, rationale, therapeuticAreas, studyType, characteristics, studyPhase, notes, model, subTypes, timePerspective, and samplingMethod according to the data you extracted. For all relationships with a cardinality (activities, biospecimenRetentions, encounters, estimands, indications, objectives, scheduleTimelines, arms, studyCells, documentVersions, elements, studyInterventions, epochs, population), just provide their respective unique identifiers and do not attempt to fit information into them. For example, for arms, use arms: ["StudyArm_001", "StudyArm_002"].
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ObservationalStudyDesign").
For attributes that point to a Code or AliasCode object, use the CNCIt-001 placeholder for the code ID.
Pay close attention to the data types: studyPhase is an AliasCode, while therapeuticAreas, studyType, characteristics, model, subTypes, timePerspective, and samplingMethod are Code objects.
When an attribute has a cardinality greater than 1 (e.g., 1..*), you must provide a unique identifier for each instance in an array. For example, arms: ["StudyArm_001", "StudyArm_002"].
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Overall Design",
  "extracted_text": "This is a prospective, multicenter, observational cohort study to describe the natural history of Wilson disease and collect safety data. The study will follow a single cohort of patients for up to 5 years. There are no investigational interventions."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "observationalStudyDesign": {
    "id": "ObservationalStudyDesign_001",
    "instanceType": "ObservationalStudyDesign",
    "extensionAttributes": null,
    "name": "Natural History of Wilson Disease Study",
    "description": "A prospective, multicenter, observational cohort study to describe the natural history of Wilson disease and collect safety data.",
    "label": "Observational Cohort Study",
    "rationale": "To describe the natural history of Wilson disease.",
    "therapeuticAreas": {
      "id": "Code_CNCIt-001",
      "name": "Wilson disease"
    },
    "studyType": {
      "id": "Code_CNCIt-001",
      "name": "Observational"
    },
    "characteristics": [
      {
        "id": "Code_CNCIt-001",
        "name": "Multicenter"
      }
    ],
    "studyPhase": {
      "id": "AliasCode_001",
      "instanceType": "AliasCode",
      "standardCode": {
        "id": "Code_CNCIt-001",
        "name": "Not Applicable"
      }
    },
    "notes": "No investigational interventions are involved.",
    "activities": [],
    "biospecimenRetentions": [],
    "encounters": [],
    "estimands": [],
    "indications": [
      {
        "id": "Indication_001"
      }
    ],
    "objectives": [
      {
        "id": "Objective_001"
      }
    ],
    "scheduleTimelines": [
      {
        "id": "ScheduleTimeline_001"
      }
    ],
    "arms": [
      {
        "id": "StudyArm_001"
      }
    ],
    "studyCells": [
      {
        "id": "StudyCell_001"
      }
    ],
    "documentVersions": [],
    "elements": [],
    "studyInterventions": [],
    "epochs": [
      {
        "id": "StudyEpoch_001"
      }
    ],
    "population": {
      "id": "StudyDesignPopulation_001"
    },
    "model": {
      "id": "Code_CNCIt-001",
      "name": "Cohort"
    },
    "subTypes": [
      {
        "id": "Code_CNCIt-001",
        "name": "Natural History"
      }
    ],
    "timePerspective": {
      "id": "Code_CNCIt-001",
      "name": "Prospective"
    },
    "samplingMethod": null
  }
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Organization:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about any organizations involved in the study and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Organization. Understand each attribute's purpose, data type, and cardinality. Note the relationships to legalAddress (optional) and managedSites (zero or more).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract all organizations involved in the study, such as the sponsor, investigator sites, or central labs. Look for their full name, any short labels, identifiers, and their address.
Populate the USDM Schema: Fill the Organization schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Organization_001). Populate the attributes name, label, identifier, identifierScheme, and type. For relationships, just provide the unique identifiers of the related objects (e.g., legalAddress: { "id": "Address_001" }).
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Organization").
The name attribute should be the full legal name of the organization.
The type attribute is a Code object that classifies the organization's role (e.g., "Sponsor," "Study Site"). Use the CNCIt-001 placeholder for the code ID.
The legalAddress and managedSites are relationships. You should link to them using their unique identifiers. For managedSites, this will be an array of IDs.
If a field is not explicitly mentioned, leave it as a blank string "" or null as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Signature Page",
  "extracted_text": "Study Sponsor: Alexion Pharmaceuticals, Inc.Address: 121 Seaport Boulevard, Boston, MA 02210, USA"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "organizations": [
    {
      "id": "Organization_001",
      "instanceType": "Organization",
      "extensionAttributes": null,
      "name": "Alexion Pharmaceuticals, Inc.",
      "label": "Alexion",
      "identifier": null,
      "identifierScheme": null,
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Sponsor"
      },
      "legalAddress": {
        "id": "Address_001"
      },
      "managedSites": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Parametermap:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about programming tags or parameter references and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ParameterMap. Understand each attribute's purpose, data type, and cardinality. Note that tag and reference are both string attributes.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify any sections that contain programming-like tags or references, often used to link data points or variables to a protocol's content.
Populate the USDM Schema: Fill the ParameterMap schema template with the relevant information extracted from the protocol. For each instance, provide a unique, arbitrary identifier (e.g., ParameterMap_001). Populate the attributes tag and reference according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ParameterMap").
The tag attribute should contain the programming tag itself, often enclosed in brackets (e.g., "<STUDY_IDENTIFIER>").
The reference attribute should contain the textual or data-driven value that the tag points to (e.g., "ALXN1840-C-201").
If the protocol uses a table or list to map tags to their values, extract each pair and create a separate ParameterMap object for it.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Data Management Plan",
  "extracted_text": "The protocol number is referenced by the tag <PROTOCOL_ID>. The value for this tag is ALXN1840-C-201."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "parameterMaps": [
    {
      "id": "ParameterMap_001",
      "instanceType": "ParameterMap",
      "extensionAttributes": null,
      "tag": "<PROTOCOL_ID>",
      "reference": "ALXN1840-C-201"
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Populationdefinition:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the study's population definition and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for PopulationDefinition. Understand each attribute's purpose, data type, and cardinality. Note the relationships to Range and Quantity objects, the boolean includesHealthySubjects, and the relationship to criteria.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to find sections that describe the characteristics of the study participants, including age, gender, health status (healthy vs. diseased), and planned enrollment or completion numbers. This information is typically found in the Synopsis and Inclusion/Exclusion Criteria sections.
Populate the USDM Schema: Fill the PopulationDefinition schema template with the relevant information extracted from the protocol. For each population, provide a unique, arbitrary identifier (e.g., PopulationDefinition_001). Populate the attributes name, description, label, plannedSex, includesHealthySubjects, plannedAge, plannedCompletionNumberRange, plannedCompletionNumberQuantity, plannedEnrollmentNumberRange, plannedEnrollmentNumberQuantity, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "PopulationDefinition").
plannedAge, plannedCompletionNumberRange, and plannedEnrollmentNumberRange are Range objects and should contain low and high values.
plannedEnrollmentNumberQuantity and plannedCompletionNumberQuantity are Quantity objects and should contain a value and a unit.
plannedSex is a Code object. Use the CNCIt-001 placeholder for the code ID.
includesHealthySubjects is a boolean value (true or false).
criteria is a relationship to a list of EligibilityCriterion objects. You should link to them by their unique identifiers (e.g., criteria: [{ "id": "EligibilityCriterion_001" }]).
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "9.2 Sample Size Determination",
  "extracted_text": "Approximately 10 participants with Wilson disease will be enrolled. The study population consists of male and female subjects aged 18 to 65 years. The number of subjects to be randomized may be revised based on the interim analysis."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "populationDefinitions": [
    {
      "id": "PopulationDefinition_001",
      "instanceType": "PopulationDefinition",
      "extensionAttributes": null,
      "name": "Target Population",
      "description": "The study population consists of male and female subjects aged 18 to 65 years with Wilson disease.",
      "label": "Study Population",
      "plannedSex": {
        "id": "Code_CNCIt-001",
        "name": "Male and Female"
      },
      "includesHealthySubjects": false,
      "plannedAge": {
        "id": "Range_001",
        "instanceType": "Range",
        "low": 18.0,
        "high": 65.0,
        "unit": {
          "id": "AliasCode_001",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Years"
          }
        }
      },
      "plannedCompletionNumberRange": null,
      "plannedCompletionNumberQuantity": null,
      "plannedEnrollmentNumberRange": null,
      "plannedEnrollmentNumberQuantity": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "value": 10.0,
        "unit": {
          "id": "AliasCode_002",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Participants"
          }
        }
      },
      "notes": "The number of subjects to be randomized may be revised based on the interim analysis.",
      "criteria": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Populationdefinition:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the study's population definition and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for PopulationDefinition. Understand each attribute's purpose, data type, and cardinality. Note the relationships to Range and Quantity objects, the boolean includesHealthySubjects, and the relationship to criteria.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to find sections that describe the characteristics of the study participants, including age, gender, health status (healthy vs. diseased), and planned enrollment or completion numbers. This information is typically found in the Synopsis and Inclusion/Exclusion Criteria sections.
Populate the USDM Schema: Fill the PopulationDefinition schema template with the relevant information extracted from the protocol. For each population, provide a unique, arbitrary identifier (e.g., PopulationDefinition_001). Populate the attributes name, description, label, plannedSex, includesHealthySubjects, plannedAge, plannedCompletionNumberRange, plannedCompletionNumberQuantity, plannedEnrollmentNumberRange, plannedEnrollmentNumberQuantity, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "PopulationDefinition").
plannedAge, plannedCompletionNumberRange, and plannedEnrollmentNumberRange are Range objects and should contain low and high values.
plannedEnrollmentNumberQuantity and plannedCompletionNumberQuantity are Quantity objects and should contain a value and a unit.
plannedSex is a Code object. Use the CNCIt-001 placeholder for the code ID.
includesHealthySubjects is a boolean value (true or false).
criteria is a relationship to a list of EligibilityCriterion objects. You should link to them by their unique identifiers (e.g., criteria: [{ "id": "EligibilityCriterion_001" }]).
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "9.2 Sample Size Determination",
  "extracted_text": "Approximately 10 participants with Wilson disease will be enrolled. The study population consists of male and female subjects aged 18 to 65 years. The number of subjects to be randomized may be revised based on the interim analysis."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "populationDefinitions": [
    {
      "id": "PopulationDefinition_001",
      "instanceType": "PopulationDefinition",
      "extensionAttributes": null,
      "name": "Target Population",
      "description": "The study population consists of male and female subjects aged 18 to 65 years with Wilson disease.",
      "label": "Study Population",
      "plannedSex": {
        "id": "Code_CNCIt-001",
        "name": "Male and Female"
      },
      "includesHealthySubjects": false,
      "plannedAge": {
        "id": "Range_001",
        "instanceType": "Range",
        "low": 18.0,
        "high": 65.0,
        "unit": {
          "id": "AliasCode_001",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Years"
          }
        }
      },
      "plannedCompletionNumberRange": null,
      "plannedCompletionNumberQuantity": null,
      "plannedEnrollmentNumberRange": null,
      "plannedEnrollmentNumberQuantity": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "value": 10.0,
        "unit": {
          "id": "AliasCode_002",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Participants"
          }
        }
      },
      "notes": "The number of subjects to be randomized may be revised based on the interim analysis.",
      "criteria": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Productorganizationrole:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about an organization's function related to a study product and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ProductOrganizationRole. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationship to organization and the optional relationship to appliesTo.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract the names of organizations and their specific roles concerning the investigational product or a medical device (e.g., sponsor, manufacturer, supplier).
Populate the USDM Schema: Fill the ProductOrganizationRole schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ProductOrganizationRole_001). Populate the attributes name, description, label, code, appliesTo, and organization according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ProductOrganizationRole").
The code attribute is a Code object that specifies the organization's role (e.g., "Sponsor", "Manufacturer"). Use the CNCIt-001 placeholder for the code ID.
The organization attribute is a mandatory relationship to an Organization object. You must link it by its unique identifier (e.g., organization: { "id": "Organization_001" }).
The appliesTo attribute is an optional relationship to a list of AdministrableProduct or MedicalDevice objects. You should link to them by their unique identifiers (e.g., appliesTo: [{"id": "AdministrableProduct_001"}]).
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Identification",
  "extracted_text": "The study drug ALXN1840 is manufactured by Alexion Pharmaceuticals, Inc."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "productOrganizationRoles": [
    {
      "id": "ProductOrganizationRole_001",
      "instanceType": "ProductOrganizationRole",
      "extensionAttributes": null,
      "name": "Manufacturer",
      "description": "The manufacturer of the study drug ALXN1840.",
      "label": "Manufacturer",
      "code": {
        "id": "Code_CNCIt-001",
        "name": "Manufacturer"
      },
      "appliesTo": [
        {
          "id": "AdministrableProduct_001"
        }
      ],
      "organization": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "extensionAttributes": null,
        "name": "Alexion Pharmaceuticals, Inc."
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Quantity:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a measurable quantity and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Quantity. Understand each attribute's purpose, data type, and cardinality. Note that value is a float and unit is an AliasCode object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify any numerical values paired with a unit of measure, such as dosage amounts, durations, subject counts, or volumes.
Populate the USDM Schema: Fill the Quantity schema template with the relevant information extracted from the protocol. For each quantity, provide a unique, arbitrary identifier (e.g., Quantity_001). Populate the attributes value and unit according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Quantity").
The value attribute must be a number (float or integer).
The unit attribute is a nested AliasCode object. You should create this object with its own unique id and instanceType, and it should contain a nested standardCode object with a placeholder id (CNCIt-001) and a name for the unit (e.g., "mg", "weeks").
If the protocol provides a numerical range (e.g., "5 to 10 mg"), you should represent this in a Range object, which typically has nested Quantity objects for the high and low values.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "6.4 Study Intervention",
  "extracted_text": "The dose is 15 mg/day. The study duration is 12 weeks."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "quantities": [
    {
      "id": "Quantity_001",
      "instanceType": "Quantity",
      "extensionAttributes": null,
      "value": 15.0,
      "unit": {
        "id": "AliasCode_001",
        "instanceType": "AliasCode",
        "standardCode": {
          "id": "Code_CNCIt-001",
          "name": "Milligram"
        }
      }
    },
    {
      "id": "Quantity_002",
      "instanceType": "Quantity",
      "extensionAttributes": null,
      "value": 12.0,
      "unit": {
        "id": "AliasCode_002",
        "instanceType": "AliasCode",
        "standardCode": {
          "id": "Code_CNCIt-001",
          "name": "Weeks"
        }
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Range:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a numerical range and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Range. Understand each attribute's purpose, data type, and cardinality. Note that both minValue and maxValue are nested Quantity objects, and isApproximate is a boolean.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any descriptions of numerical ranges, such as age ranges, dose ranges, or time windows. Look for phrases like "between X and Y," "up to Z," or "from A to B."
Populate the USDM Schema: Fill the Range schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Range_001). Populate the attributes minValue, maxValue, and isApproximate according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Range").
Both minValue and maxValue must be nested Quantity objects. Each Quantity object needs a value (the number) and a unit (a nested AliasCode).
The isApproximate attribute must be a boolean value (true or false). Look for words like "approximately," "up to," or "about" to determine if the value is approximate.
If a range has only one boundary (e.g., "up to 12 weeks"), you should populate either minValue or maxValue and leave the other as null.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "5.1 Inclusion Criteria",
  "extracted_text": "Subjects must be between 18 and 65 years of age. Approximately 10 participants will be enrolled."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "ranges": [
    {
      "id": "Range_001",
      "instanceType": "Range",
      "extensionAttributes": null,
      "minValue": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "extensionAttributes": null,
        "value": 18.0,
        "unit": {
          "id": "AliasCode_001",
          "instanceType": "AliasCode",
          "extensionAttributes": null,
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Years"
          }
        }
      },
      "maxValue": {
        "id": "Quantity_002",
        "instanceType": "Quantity",
        "extensionAttributes": null,
        "value": 65.0,
        "unit": {
          "id": "AliasCode_002",
          "instanceType": "AliasCode",
          "extensionAttributes": null,
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Years"
          }
        }
      },
      "isApproximate": false
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Referenceidentifier:
        ROLE_TEMPLATE = """
You're an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's reference identifiers and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ReferenceIdentifier. Understand each attribute's purpose, data type, and cardinality. Note that scope is a mandatory relationship to an Organization class and type is a Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any official or internal identifiers used to reference the study, such as protocol numbers, ClinicalTrials.gov IDs, or EudraCT numbers. These identifiers are often associated with a specific organization that issued or maintains them.
Populate the USDM Schema: Fill the ReferenceIdentifier schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ReferenceIdentifier_001). Populate the attributes text, type, and scope according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ReferenceIdentifier").
The text attribute should contain the literal identifier string (e.g., "ALXN1840-C-201").
The type attribute is a nested Code object that classifies the identifier's kind (e.g., "Sponsor Protocol Number," "ClinicalTrials.gov ID"). Use the CNCIt-001 placeholder for the code ID.
The scope attribute is a mandatory relationship. You must link it to a pre-defined or newly created Organization object by its unique identifier (e.g., scope: { "id": "Organization_001" }). This organization is the entity that assigned the identifier.
If a field is not explicitly mentioned, leave it blank.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Identification",
  "extracted_text": "Sponsor Protocol Number: ALXN1840-C-201ClinicalTrials.gov Identifier: NCT01234567"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "referenceIdentifiers": [
    {
      "id": "ReferenceIdentifier_001",
      "instanceType": "ReferenceIdentifier",
      "extensionAttributes": null,
      "text": "ALXN1840-C-201",
      "scope": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "extensionAttributes": null,
        "name": "Alexion Pharmaceuticals, Inc."
      },
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Sponsor Protocol Number"
      }
    },
    {
      "id": "ReferenceIdentifier_002",
      "instanceType": "ReferenceIdentifier",
      "extensionAttributes": null,
      "text": "NCT01234567",
      "scope": {
        "id": "Organization_002",
        "instanceType": "Organization",
        "extensionAttributes": null,
        "name": "ClinicalTrials.gov"
      },
      "type": {
        "id": "Code_CNCIt-001",
        "name": "ClinicalTrials.gov Identifier"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Responsecode:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a response code and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ResponseCode. Understand each attribute's purpose, data type, and cardinality. Note that isEnabled is a boolean and code is a nested Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any information about coded responses, especially from questionnaires, forms, or data collection instruments. This includes the code itself and whether it is an active or available option.
Populate the USDM Schema: Fill the ResponseCode schema template with the relevant information extracted from the protocol. For each response code, provide a unique, arbitrary identifier (e.g., ResponseCode_001). Populate the attributes isEnabled and code according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ResponseCode").
The isEnabled attribute must be a boolean value (true or false).
The code attribute is a nested Code object. It should contain a placeholder id (CNCIt-001) and a name representing the response (e.g., "Yes," "No," "Male," "Female").
If the protocol provides a list of possible responses for a question, you should create a separate ResponseCode object for each one.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Data Collection Forms",
  "extracted_text": "The patient gender question on the Case Report Form uses a dropdown with the options 'Male' and 'Female'."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "responseCodes": [
    {
      "id": "ResponseCode_001",
      "instanceType": "ResponseCode",
      "extensionAttributes": null,
      "isEnabled": true,
      "code": {
        "id": "Code_CNCIt-001",
        "name": "Male"
      }
    },
    {
      "id": "ResponseCode_002",
      "instanceType": "ResponseCode",
      "extensionAttributes": null,
      "isEnabled": true,
      "code": {
        "id": "Code_CNCIt-001",
        "name": "Female"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Scheduletimeline:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the study's schedule timeline, including its events, conditions, and structure, and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ScheduleTimeline. Understand each attribute's purpose, data type, and cardinality. Note the relationships to ScheduledInstance, ScheduleTimelineExit, and Timing. Pay close attention to the mainTimeline boolean and the mandatory entry relationship.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any descriptions of the study's chronological flow, such as the different phases, the order of visits, and any conditions for entering a specific phase.
Populate the USDM Schema: Fill the ScheduleTimeline schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ScheduleTimeline_001). Populate the attributes name, description, label, entryCondition, and mainTimeline. For relationships (instances, entry, exits, timings), provide their respective unique identifiers and do not attempt to fit information into them.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ScheduleTimeline").
The name attribute should be a literal identifier for the timeline (e.g., "Main Study Timeline").
The mainTimeline attribute must be a boolean (true or false).
The entry relationship is mandatory. You must link it to a specific ScheduledInstance object by its unique identifier (e.g., entry: { "id": "ScheduledInstance_001" }).
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.2 Schedule of Activities",
  "extracted_text": "The study consists of three main periods: a Screening Period, a Treatment Period, and a Follow-up Period. Entry into the study begins with the Screening Visit. Participants must meet all inclusion criteria to proceed to the Treatment Period. The total duration of the study is 12 weeks."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "scheduleTimelines": [
    {
      "id": "ScheduleTimeline_001",
      "instanceType": "ScheduleTimeline",
      "extensionAttributes": null,
      "name": "Overall Study Timeline",
      "description": "The study consists of three main periods: a Screening Period, a Treatment Period, and a Follow-up Period.",
      "label": "Main Study Timeline",
      "entryCondition": "Participants must meet all inclusion criteria to proceed.",
      "mainTimeline": true,
      "instances": [
        {
          "id": "ScheduledInstance_001"
        },
        {
          "id": "ScheduledInstance_002"
        },
        {
          "id": "ScheduledInstance_003"
        }
      ],
      "entry": {
        "id": "ScheduledInstance_001"
      },
      "exits": [],
      "timings": [
        {
          "id": "Timing_001"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Scheduletimelineexit:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's schedule timeline exit and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ScheduleTimelineExit. Understand its single attribute, id, and its purpose.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify any conditions or events that lead to a participant leaving the study's schedule or a specific timeline, such as early termination, completion, or drop-out.
Populate the USDM Schema: Fill the ScheduleTimelineExit schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ScheduleTimelineExit_001).
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ScheduleTimelineExit").
The ScheduleTimelineExit class is a simple marker. It primarily serves to define an exit point from a timeline.
The ID should be a simple but unique identifier for the exit event (e.g., End_of_Study_Exit).
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Flow",
  "extracted_text": "A patient will exit the study upon completion of all follow-up procedures or upon early discontinuation for any reason."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "scheduleTimelineExits": [
    {
      "id": "ScheduleTimelineExit_001",
      "instanceType": "ScheduleTimelineExit",
      "extensionAttributes": null
    },
    {
      "id": "ScheduleTimelineExit_002",
      "instanceType": "ScheduleTimelineExit",
      "extensionAttributes": null
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Scheduledactivityinstance:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a scheduled activity instance—a single occurrence of a planned activity or event—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ScheduledActivityInstance. Understand each attribute's purpose, data type, and cardinality. Note the optional relationships to defaultCondition, epoch, activities, encounter, timeline, and timelineExit.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any descriptions of specific events on the study schedule, such as a "Screening Visit," "Randomization," or "End of Study Visit." You should also look for any associated activities, the study phase (epoch) it belongs to, and its link to the overall study timeline.
Populate the USDM Schema: Fill the ScheduledActivityInstance schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ScheduledActivityInstance_001). Populate the attributes name, description, and label. For relationships (defaultCondition, epoch, activities, encounter, timeline, timelineExit), provide their respective unique identifiers and do not attempt to fit information into them.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ScheduledActivityInstance").
The name attribute should be a literal identifier for the scheduled event.
The activities relationship is an array of links to Activity objects.
The encounter relationship links to a corresponding Encounter object (e.g., Encounter_001).
If a field is not explicitly mentioned, leave it as a blank string "" or null as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.2 Schedule of Activities",
  "extracted_text": "The study begins with a Screening Visit in the Screening Period. During this visit, we will conduct a physical examination and collect blood samples. This visit is linked to the main study timeline."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "scheduledActivityInstances": [
    {
      "id": "ScheduledActivityInstance_001",
      "instanceType": "ScheduledActivityInstance",
      "extensionAttributes": null,
      "name": "Screening Visit",
      "description": "The study begins with a Screening Visit in the Screening Period.",
      "label": "Screening Visit",
      "defaultCondition": null,
      "epoch": {
        "id": "StudyEpoch_001"
      },
      "activities": [
        {
          "id": "Activity_001"
        },
        {
          "id": "Activity_002"
        }
      ],
      "encounter": {
        "id": "Encounter_001"
      },
      "timeline": {
        "id": "ScheduleTimeline_001"
      },
      "timelineExit": null
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Scheduleddecisioninstance:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a scheduled decision instance and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ScheduledDecisionInstance. Understand each attribute's purpose, data type, and cardinality. Note the optional relationships to defaultCondition and epoch and the mandatory relationship to conditionAssignments (a cardinality of 1..*).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any descriptions of planned decision points in the study flow, such as a randomization event, a dose-escalation decision, or a go/no-go decision based on interim data. Also, find the specific conditions or rules that govern these decisions.
Populate the USDM Schema: Fill the ScheduledDecisionInstance schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ScheduledDecisionInstance_001). Populate the attributes name, description, and label. For relationships, provide their respective unique identifiers (e.g., epoch: { "id": "StudyEpoch_001" }, conditionAssignments: [{"id": "ConditionAssignment_001"}]).
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ScheduledDecisionInstance").
The name attribute should be a literal identifier for the decision event (e.g., "Randomization Decision").
The conditionAssignments attribute is a mandatory relationship to one or more ConditionAssignment objects. You must link to them by their unique identifiers (e.g., conditionAssignments: [{ "id": "ConditionAssignment_001" }]).
The defaultCondition and epoch relationships are optional. If a field is not explicitly mentioned, leave it as null.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Flow",
  "extracted_text": "Randomization to treatment groups will occur after all screening procedures are completed and the patient meets all inclusion criteria. The decision to randomize will be made at the end of the Screening Period."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "scheduledDecisionInstances": [
    {
      "id": "ScheduledDecisionInstance_001",
      "instanceType": "ScheduledDecisionInstance",
      "extensionAttributes": null,
      "name": "Randomization Decision",
      "description": "The decision to randomize patients to treatment groups.",
      "label": "Randomization",
      "defaultCondition": null,
      "epoch": {
        "id": "StudyEpoch_001"
      },
      "conditionAssignments": [
        {
          "id": "ConditionAssignment_001"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Scheduledinstance:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a scheduled instance—a generic term for any scheduled event in a study—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for ScheduledInstance. Understand each attribute's purpose, data type, and cardinality. Note the optional relationships to defaultCondition and epoch.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any discrete, scheduled events from the study timeline, such as visits, decision points, or other key temporal events.
Populate the USDM Schema: Fill the ScheduledInstance schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., ScheduledInstance_001). Populate the attributes name, description, and label. For relationships, provide their respective unique identifiers (e.g., epoch: { "id": "StudyEpoch_001" }).
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "ScheduledInstance").
The name attribute should be a literal identifier for the event (e.g., "Screening Visit").
The defaultCondition and epoch relationships are optional. If a field is not explicitly mentioned, leave it as null.
Remember that ScheduledInstance is an abstract parent class for more specific classes like ScheduledActivityInstance and ScheduledDecisionInstance. This prompt focuses on the generic parent class, so you'll be populating only its attributes.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.2 Schedule of Activities",
  "extracted_text": "The study consists of a Screening Period, a Treatment Period, and a Follow-up Period. The first event is the Screening Visit, which takes place in the Screening Period."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "scheduledInstances": [
    {
      "id": "ScheduledInstance_001",
      "instanceType": "ScheduledInstance",
      "extensionAttributes": null,
      "name": "Screening Visit",
      "description": "The first event of the study.",
      "label": "Screening",
      "defaultCondition": null,
      "epoch": {
        "id": "StudyEpoch_001"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Strength:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a substance's strength and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Strength. Understand each attribute's purpose, data type, and cardinality. Note the relationships to Range and Quantity objects for the numerator and denominator.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any information about the concentration or potency of the active substance. Look for values expressed in units like "mg/mL," "g/tablet," or a simple quantity like "15 mg."
Populate the USDM Schema: Fill the Strength schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Strength_001). Populate the attributes name, description, label, numeratorRange, numeratorQuantity, and denominator according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Strength").
The numeratorRange attribute is a nested Range object. The numeratorQuantity and denominator attributes are nested Quantity objects. These must be populated with their own unique identifiers and nested values.
If the strength is a single value (e.g., "15 mg"), use the numeratorQuantity attribute. If it is a range (e.g., "5-10 mg"), use the numeratorRange attribute. Do not use both for the same strength.
The denominator is only used when the strength is expressed as a ratio (e.g., mg/mL). If the strength is a simple quantity (e.g., mg), the denominator should be left as null.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Product Description",
  "extracted_text": "The study drug is available as a 15 mg tablet. The concentration of the solution is 100 mg/mL."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "strengths": [
    {
      "id": "Strength_001",
      "instanceType": "Strength",
      "extensionAttributes": null,
      "name": "Tablet Strength",
      "description": "The strength of the study drug per tablet.",
      "label": "15 mg Tablet",
      "numeratorRange": null,
      "numeratorQuantity": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "value": 15.0,
        "unit": {
          "id": "AliasCode_001",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Milligram"
          }
        }
      },
      "denominator": null
    },
    {
      "id": "Strength_002",
      "instanceType": "Strength",
      "extensionAttributes": null,
      "name": "Solution Concentration",
      "description": "The concentration of the study drug solution.",
      "label": "100 mg/mL",
      "numeratorRange": null,
      "numeratorQuantity": {
        "id": "Quantity_002",
        "instanceType": "Quantity",
        "value": 100.0,
        "unit": {
          "id": "AliasCode_002",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Milligram"
          }
        }
      },
      "denominator": {
        "id": "Quantity_003",
        "instanceType": "Quantity",
        "value": 1.0,
        "unit": {
          "id": "AliasCode_003",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Milliliter"
          }
        }
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Study:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a clinical study and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Study. Understand each attribute's purpose, data type, and cardinality. Note the relationships to versions and documentedBy.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract the overall study name, a brief description, and any unique identifiers or labels for the entire trial. This information is usually found in the title page or synopsis.
Populate the USDM Schema: Fill the Study schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for the instance (e.g., Study_001). Populate the attributes name, description, and label. For relationships (versions, documentedBy), provide their respective unique identifiers and do not attempt to fit information into them.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Study").
The name attribute should be the full, literal name of the study.
The versions and documentedBy relationships are arrays of linked objects. You should link to them by their unique identifiers (e.g., versions: [{ "id": "StudyVersion_001" }]).
If a field is not explicitly mentioned, leave it as a blank string "" or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol for a Phase 2, open-label, multicenter, randomized clinical trial to assess the efficacy and safety of ALXN1840",
  "extracted_text": "Protocol Title: A Study to Evaluate the Efficacy and Safety of ALXN1840 in Patients with Wilson Disease"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "study": {
    "id": "Study_001",
    "instanceType": "Study",
    "extensionAttributes": null,
    "name": "A Study to Evaluate the Efficacy and Safety of ALXN1840 in Patients with Wilson Disease",
    "description": "A Phase 2, open-label, multicenter, randomized clinical trial to assess the efficacy and safety of ALXN1840 in patients with Wilson disease.",
    "label": "ALXN1840-C-201",
    "versions": [],
    "documentedBy": []
  }
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyamendment:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about study amendments and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyAmendment. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationships to primaryReason, geographicScopes, and changes, and the optional relationships to dateValues, impacts, enrollments, secondaryReasons, and previous.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections like "Protocol Amendment History." Your goal is to extract information about each amendment, including its number, date, summary of changes, and the rationale behind those changes.
Populate the USDM Schema: Fill the StudyAmendment schema template with the relevant information extracted from the protocol. For each amendment, provide a unique, arbitrary identifier (e.g., StudyAmendment_001). Populate the attributes number, notes, summary, and the various relationships by providing the unique identifiers of the related objects. Do not nest the full object definitions.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyAmendment").
The number attribute should be a string (e.g., "1," "2").
The summary attribute should capture the high-level description of the changes.
The primaryReason relationship is mandatory. The previous relationship should link to the id of the chronologically preceding amendment.
Relationships with cardinality greater than one (e.g., geographicScopes, changes) should be represented as an array of identifiers.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "10.7. Protocol Amendment History",
  "extracted_text": "Amendment 1 was substantial, updating procedures in the Schedule of Activities, removing contradictory text on SAE reporting, and adding details on interim analysis.4: Amendment 2 was substantial, revising exclusion criteria for urine drug screen and incorporating COVID-19 vaccination guidance.",
  "extracted_tables": [
    {
      "data": [
        ["Document", "Date"],
        ["Amendment 1", "18 Aug 2020"],
        ["Amendment 2", "19 Mar 2021"]
      ]
    }
  ]
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "amendments": [
    {
      "id": "StudyAmendment_001",
      "instanceType": "StudyAmendment",
      "extensionAttributes": null,
      "number": "1",
      "notes": "",
      "summary": "Amendment 1 was substantial, updating procedures in the Schedule of Activities, removing contradictory text on SAE reporting, and adding details on interim analysis.",
      "geographicScopes": [],
      "dateValues": [
        {
          "id": "GovernanceDate_001"
        }
      ],
      "impacts": [
        {
          "id": "StudyAmendmentImpact_001"
        }
      ],
      "enrollments": [],
      "secondaryReasons": [],
      "changes": [
        {
          "id": "StudyChange_001"
        }
      ],
      "previous": null,
      "primaryReason": {
        "id": "StudyAmendmentReason_001"
      }
    },
    {
      "id": "StudyAmendment_002",
      "instanceType": "StudyAmendment",
      "extensionAttributes": null,
      "number": "2",
      "notes": "",
      "summary": "Amendment 2 was substantial, revising exclusion criteria for urine drug screen and incorporating COVID-19 vaccination guidance.",
      "geographicScopes": [],
      "dateValues": [
        {
          "id": "GovernanceDate_002"
        }
      ],
      "impacts": [
        {
          "id": "StudyAmendmentImpact_002"
        }
      ],
      "enrollments": [],
      "secondaryReasons": [],
      "changes": [
        {
          "id": "StudyChange_002"
        }
      ],
      "previous": {
        "id": "StudyAmendment_001"
      },
      "primaryReason": {
        "id": "StudyAmendmentReason_002"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyamendmentimpact:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the impact of a protocol amendment and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyAmendmentImpact. Understand each attribute's purpose, data type, and cardinality. Note that isSubstantial is a boolean and type is a Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any descriptions of the consequences or effects that an amendment has on the study. Look for phrases like "substantial amendment," "minor change," or a description of the amendment's effect on safety, procedures, or the study population.
Populate the USDM Schema: Fill the StudyAmendmentImpact schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., StudyAmendmentImpact_001). Populate the attributes text, isSubstantial, type, and notes according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyAmendmentImpact").
The isSubstantial attribute must be a boolean value (true or false).
The type attribute is a Code object that classifies the type of impact (e.g., "Significant Change," "Minor Change"). Use the CNCIt-001 placeholder for the code ID.
If a field is not explicitly mentioned, leave it as a blank string "" or null as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "10.7. Protocol Amendment History",
  "extracted_text": "Amendment 1 was substantial, updating procedures in the Schedule of Activities, removing contradictory text on SAE reporting, and adding details on interim analysis."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyAmendmentImpacts": [
    {
      "id": "StudyAmendmentImpact_001",
      "instanceType": "StudyAmendmentImpact",
      "extensionAttributes": null,
      "text": "The amendment impacted procedures in the Schedule of Activities, SAE reporting, and added details on interim analysis.",
      "isSubstantial": true,
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Substantial Amendment"
      },
      "notes": ""
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyamendmentreason:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract the core rationale for a protocol amendment and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyAmendmentReason. Understand each attribute's purpose, data type, and cardinality. Note that otherReason is a string and code is a nested Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical content. Your goal is to identify and extract the explicit rationale or justification for a protocol change. This is often found in tables that summarize changes, or in the narrative text describing the purpose of an amendment.
Populate the USDM Schema: Fill the StudyAmendmentReason schema template with the relevant information extracted from the protocol. For each reason, provide a unique, arbitrary identifier (e.g., StudyAmendmentReason_001). Populate the attributes otherReason and code according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyAmendmentReason").
The otherReason attribute is for rationales that don't have a specific code, such as a detailed explanation. If a specific code exists, this attribute may be left blank.
The code attribute is a nested Code object. Use the placeholder CNCIt-001 for the code ID.
If a field is not explicitly mentioned in the protocol, leave it blank.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "10.7. Protocol Amendment History",
  "extracted_text": "The main reason for preparation of this amendment was to update procedures outlined in the Schedule of Activities. The rationale for the change was to align the definition with the Statistical Analysis Plan."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyAmendmentReasons": [
    {
      "id": "StudyAmendmentReason_001",
      "instanceType": "StudyAmendmentReason",
      "extensionAttributes": null,
      "otherReason": "To align the definition with the Statistical Analysis Plan.",
      "code": {
        "id": "Code_CNCIt-001",
        "name": "To align with Statistical Analysis Plan"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyarm:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study arm—a planned pathway for a group of participants—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyArm. Understand each attribute's purpose, data type, and cardinality. Note the relationships, such as populations (a cardinality of 0..*).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract descriptions of the different treatment or observation groups. This information is typically found in the design overview, synopsis, or randomization sections. You need to find the name of each arm, its description, and any associated populations.
Populate the USDM Schema: Fill the StudyArm schema template with the relevant information extracted from the protocol. For each study arm, provide a unique, arbitrary identifier (e.g., StudyArm_001). Populate the attributes name, description, label, type, dataOriginType, dataOriginDescription, and notes. For the populations relationship, provide the unique identifiers of the related PopulationDefinition objects.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyArm").
The name attribute should be a concise identifier for the arm (e.g., "High-Dose Arm").
The type and dataOriginType attributes are Code objects. Use the CNCIt-001 placeholder for the code ID.
The populations relationship is a list of links. You should link to the corresponding PopulationDefinition objects by their unique IDs.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Overall Design",
  "extracted_text": "The study will have two treatment groups or arms: the 'high-dose arm' will receive 30 mg of the study drug, and the 'low-dose arm' will receive 15 mg. Both groups will consist of patients with Wilson disease. There is no placebo group."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyArms": [
    {
      "id": "StudyArm_001",
      "instanceType": "StudyArm",
      "extensionAttributes": null,
      "name": "High-Dose Arm",
      "description": "Participants in this arm will receive 30 mg of the study drug.",
      "label": "High-Dose",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Experimental"
      },
      "dataOriginType": null,
      "dataOriginDescription": null,
      "notes": "No placebo group mentioned.",
      "populations": [
        {
          "id": "PopulationDefinition_001"
        }
      ]
    },
    {
      "id": "StudyArm_002",
      "instanceType": "StudyArm",
      "extensionAttributes": null,
      "name": "Low-Dose Arm",
      "description": "Participants in this arm will receive 15 mg of the study drug.",
      "label": "Low-Dose",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Experimental"
      },
      "dataOriginType": null,
      "dataOriginDescription": null,
      "notes": "No placebo group mentioned.",
      "populations": [
        {
          "id": "PopulationDefinition_001"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studycell:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study cell—a specific segment of a study arm within an epoch—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyCell. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationships to arm, epoch, and elements (a cardinality of 1..*).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on the study design and timeline. Your goal is to identify how study arms are broken down into distinct periods or phases, and which elements or activities belong to each segment.
Populate the USDM Schema: Fill the StudyCell schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., StudyCell_001). For all relationships (arm, epoch, elements), you should only provide their respective unique identifiers and do not attempt to fit information into them.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyCell").
StudyCell objects are relationships that connect a specific StudyArm to a specific StudyEpoch and the StudyElements that occur within that combination.
The arm and epoch relationships are mandatory. You must link each StudyCell to a single StudyArm and a single StudyEpoch.
The elements relationship is mandatory and must contain an array of identifiers for StudyElement objects.
If a field is not explicitly mentioned, leave it as an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Overall Design",
  "extracted_text": "The study has a Screening Period followed by a 12-week Treatment Period. The low-dose arm will receive a 15 mg dose in the Treatment Period. The key activities during this period are daily dosing and weekly safety assessments."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyCells": [
    {
      "id": "StudyCell_001",
      "instanceType": "StudyCell",
      "extensionAttributes": null,
      "arm": {
        "id": "StudyArm_001"
      },
      "epoch": {
        "id": "StudyEpoch_001"
      },
      "elements": [
        {
          "id": "StudyElement_001"
        },
        {
          "id": "StudyElement_002"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studychange:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study change—a specific alteration or modification within a protocol amendment—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyChange. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationship to changedSections (a cardinality of 1..*).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract each individual change described in an amendment's "Summary of Changes" table or a similar section. For each change, you'll need its description, the rationale, and the specific section(s) it affects.
Populate the USDM Schema: Fill the StudyChange schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., StudyChange_001). Populate the attributes name, description, label, rationale, and summary. For the changedSections relationship, provide the unique identifiers of the related DocumentContentReference objects.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyChange").
The name attribute should be a concise identifier for the change (e.g., "SAE Reporting Clarification").
The rationale attribute should contain the explanation for why the change was made. The description can be a narrative representation of the change itself.
The changedSections attribute is a mandatory relationship to a list of DocumentContentReference objects. You must link to them by their unique identifiers (e.g., changedSections: [{ "id": "DocRef_001" }]).
If a field is not explicitly mentioned, leave it as a blank string "" or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Amendment Summary of Changes Table",
  "extracted_tables": [
    {
      "columns": [
        "Section # and Name",
        "Description of Change",
        "Brief Rationale and/or Clarifications"
      ],
      "data": [
        [
          "Section 10.3.4, Reporting of SAEs",
          "Removal of contradictory text on SAE reporting via an electronic data collection tool.",
          "SAE reporting will be via a paper safety reporting form."
        ]
      ]
    }
  ]
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyChanges": [
    {
      "id": "StudyChange_001",
      "instanceType": "StudyChange",
      "extensionAttributes": null,
      "name": "SAE Reporting Clarification",
      "description": "Removal of contradictory text on SAE reporting via an electronic data collection tool.",
      "label": "SAE Reporting Change",
      "rationale": "SAE reporting will be via a paper safety reporting form.",
      "summary": "This change clarifies the method for reporting Serious Adverse Events.",
      "changedSections": [
        {
          "id": "DocumentContentReference_001",
          "instanceType": "DocumentContentReference",
          "sectionNumber": "10.3.4",
          "sectionTitle": "Reporting of SAEs"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studycohort:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study cohort—a group of individuals with shared characteristics—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyCohort. Understand each attribute's purpose, data type, and cardinality. Note that this class inherits from PopulationDefinition and adds relationships to Characteristic and Indication.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract descriptions of specific groups of participants, their shared attributes (e.g., disease state, age, sex), and planned enrollment numbers. This is often found in the study design or inclusion/exclusion criteria.
Populate the USDM Schema: Fill the StudyCohort schema template with the relevant information extracted from the protocol. For each cohort, provide a unique, arbitrary identifier (e.g., StudyCohort_001). Populate the attributes name, description, label, plannedSex, includesHealthySubjects, plannedAge, plannedCompletionNumberRange, plannedCompletionNumberQuantity, plannedEnrollmentNumberRange, plannedEnrollmentNumberQuantity, and notes. For relationships (criteria, characteristics, indications), provide their respective unique identifiers and do not attempt to fit information into them.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyCohort").
The plannedAge attribute is a Range object. The enrollment and completion numbers are Quantity or Range objects, as appropriate.
The includesHealthySubjects attribute must be a boolean.
Relationships to criteria, characteristics, and indications should be arrays of linked object IDs.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Study Design",
  "extracted_text": "This study will enroll 10 patients with Wilson disease. The study population is comprised of adults (18 to 65 years old) who have a confirmed diagnosis of Wilson disease (Leipzig score ≥ 4). There are no healthy subjects in this cohort."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyCohorts": [
    {
      "id": "StudyCohort_001",
      "instanceType": "StudyCohort",
      "extensionAttributes": null,
      "name": "Wilson Disease Cohort",
      "description": "A group of adults with a confirmed diagnosis of Wilson disease.",
      "label": "WD Cohort",
      "plannedSex": null,
      "includesHealthySubjects": false,
      "plannedAge": {
        "id": "Range_001"
      },
      "plannedCompletionNumberRange": null,
      "plannedCompletionNumberQuantity": null,
      "plannedEnrollmentNumberRange": null,
      "plannedEnrollmentNumberQuantity": {
        "id": "Quantity_001"
      },
      "notes": "",
      "criteria": [
        {
          "id": "EligibilityCriterion_001"
        }
      ],
      "characteristics": [
        {
          "id": "Characteristic_001"
        }
      ],
      "indications": [
        {
          "id": "Indication_001"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studydefinitiondocument:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's defining document (e.g., the protocol itself) and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyDefinitionDocument. Understand each attribute's purpose, data type, and cardinality. Note the relationships to versions and the nested Code objects for type and language.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, specifically the title page and document history. Your goal is to identify and extract the document's name, type (e.g., "Protocol," "Amendment"), the template used, and its language.
Populate the USDM Schema: Fill the StudyDefinitionDocument schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for the instance (e.g., StudyDefinitionDocument_001). Populate the attributes name, description, label, type, templateName, language, and notes. For the versions relationship, just provide the unique identifiers of the related StudyDefinitionDocumentVersion objects.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyDefinitionDocument").
The name attribute should be the full, literal name of the document (e.g., "Protocol for ALXN1840").
The type and language attributes are nested Code objects. Use the CNCIt-001 placeholder for the code ID.
The versions relationship is an optional array of links. You should link to any associated versions by their unique IDs.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol for a Phase 2, open-label, multicenter, randomized clinical trial to assess the efficacy and safety of ALXN1840 in patients with Wilson disease",
  "extracted_text": "This document is a Protocol based on the Sponsor's standard template. The document is in English.DOCUMENT HISTORYOriginal Protocol dated 12 May 2020."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyDefinitionDocument": {
    "id": "StudyDefinitionDocument_001",
    "instanceType": "StudyDefinitionDocument",
    "extensionAttributes": null,
    "name": "Protocol for a Phase 2, open-label, multicenter, randomized clinical trial to assess the efficacy and safety of ALXN1840 in patients with Wilson disease",
    "description": "This document is a Protocol.",
    "label": "Protocol",
    "type": {
      "id": "Code_CNCIt-001",
      "name": "Protocol"
    },
    "templateName": "Sponsor's standard template",
    "language": {
      "id": "Code_CNCIt-001",
      "name": "English"
    },
    "notes": "",
    "versions": [
      {
        "id": "StudyDefinitionDocumentVersion_001"
      }
    ]
  }
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studydefinitiondocumentversion:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a specific version of a study document (e.g., a protocol or amendment) and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyDefinitionDocumentVersion. Understand each attribute's purpose, data type, and cardinality. Note the relationships to GovernanceDate, NarrativeContent, and children.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, specifically the document history or version control section. Your goal is to identify and extract the document's version number, its status (e.g., final, draft), and the associated dates (e.g., approval date, effective date).
Populate the USDM Schema: Fill the StudyDefinitionDocumentVersion schema template with the relevant information extracted from the protocol. For each version, provide a unique, arbitrary identifier (e.g., StudyDefinitionDocumentVersion_001). Populate the attributes status, version, and notes. For relationships (dateValues, contents, children), provide their unique identifiers and do not attempt to nest the full object definitions.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyDefinitionDocumentVersion").
The version attribute should be a string (e.g., "1.0," "Amendment 2").
The status attribute is a Code object. Use the CNCIt-001 placeholder for the code ID.
The dateValues and contents relationships are arrays of links to other objects.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "DOCUMENT HISTORY",
  "extracted_text": "Original Protocol dated 12 May 2020. This is the final version."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyDefinitionDocumentVersions": [
    {
      "id": "StudyDefinitionDocumentVersion_001",
      "instanceType": "StudyDefinitionDocumentVersion",
      "extensionAttributes": null,
      "status": {
        "id": "Code_CNCIt-001",
        "name": "Final"
      },
      "version": "Original Protocol",
      "notes": "",
      "dateValues": [
        {
          "id": "GovernanceDate_001"
        }
      ],
      "contents": [],
      "children": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studydesign:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the overall study plan and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyDesign. Understand each attribute's purpose, data type, and cardinality. Note the many optional relationships. For all attributes with a cardinality other than null, you should only provide an identifier and move on.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on sections that describe the overall design and methodology. Your goal is to extract information about the study's type, phase, rationale, therapeutic area, and key components like arms, epochs, and populations.
Populate the USDM Schema: Fill the StudyDesign schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for the instance (e.g., StudyDesign_001). Populate the attributes name, description, label, rationale, therapeuticAreas, studyType, characteristics, studyPhase, and notes. For all relationships with a cardinality (activities, biospecimenRetentions, encounters, estimands, indications, objectives, scheduleTimelines, arms, studyCells, documentVersions, elements, studyInterventions, epochs, population), just provide their respective unique identifiers and do not attempt to fit information into them. For example, for arms, use arms: [{"id": "StudyArm_001"}].
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyDesign").
For attributes that point to a Code or AliasCode object, use the CNCIt-001 placeholder for the code ID.
The studyPhase is an AliasCode, while therapeuticAreas, studyType, and characteristics are Code objects.
When an attribute has a cardinality greater than 1, you must provide a unique identifier for each instance in an array.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Overall Design",
  "extracted_text": "This is a Phase 2, open-label, multicenter, randomized clinical trial to assess the efficacy and safety of ALXN1840. The study population consists of adults with Wilson disease. The study includes a Screening Period, a Treatment Period, and a Follow-up Period. Patients will be randomized to one of two treatment arms: high dose or low dose."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyDesign": {
    "id": "StudyDesign_001",
    "instanceType": "StudyDesign",
    "extensionAttributes": null,
    "name": "ALXN1840 Phase 2 Study Design",
    "description": "A Phase 2, open-label, multicenter, randomized clinical trial to assess the efficacy and safety of ALXN1840.",
    "label": "Phase 2 Clinical Trial",
    "rationale": "To assess the efficacy and safety of ALXN1840.",
    "therapeuticAreas": {
      "id": "Code_CNCIt-001",
      "name": "Wilson disease"
    },
    "studyType": {
      "id": "Code_CNCIt-001",
      "name": "Interventional"
    },
    "characteristics": [
      {
        "id": "Code_CNCIt-001",
        "name": "Multicenter"
      },
      {
        "id": "Code_CNCIt-001",
        "name": "Randomized"
      }
    ],
    "studyPhase": {
      "id": "AliasCode_001",
      "instanceType": "AliasCode",
      "standardCode": {
        "id": "Code_CNCIt-001",
        "name": "Phase 2"
      }
    },
    "notes": "Open-label design.",
    "activities": [],
    "biospecimenRetentions": [],
    "encounters": [],
    "estimands": [],
    "indications": [
      {
        "id": "Indication_001"
      }
    ],
    "objectives": [
      {
        "id": "Objective_001"
      },
      {
        "id": "Objective_002"
      }
    ],
    "scheduleTimelines": [
      {
        "id": "ScheduleTimeline_001"
      }
    ],
    "arms": [
      {
        "id": "StudyArm_001"
      },
      {
        "id": "StudyArm_002"
      }
    ],
    "studyCells": [
      {
        "id": "StudyCell_001"
      },
      {
        "id": "StudyCell_002"
      }
    ],
    "documentVersions": [],
    "elements": [],
    "studyInterventions": [
      {
        "id": "StudyIntervention_001"
      }
    ],
    "epochs": [
      {
        "id": "StudyEpoch_001"
      },
      {
        "id": "StudyEpoch_002"
      },
      {
        "id": "StudyEpoch_003"
      }
    ],
    "population": {
      "id": "StudyDesignPopulation_001"
    }
  }
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studydesignpopulation:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the overall study design population and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyDesignPopulation. Understand each attribute's purpose, data type, and cardinality. Note that this class inherits from PopulationDefinition and adds a relationship to StudyCohort.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract descriptions of the broad population to which the study results are intended to apply. This includes general characteristics like planned enrollment numbers, age, and sex, and any criteria that define the overall group.
Populate the USDM Schema: Fill the StudyDesignPopulation schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for the instance (e.g., StudyDesignPopulation_001). Populate the attributes name, description, label, plannedSex, includesHealthySubjects, plannedAge, plannedCompletionNumberRange, plannedCompletionNumberQuantity, plannedEnrollmentNumberRange, plannedEnrollmentNumberQuantity, and notes. For relationships (criteria and cohorts), provide their respective unique identifiers and do not attempt to nest the full object definitions.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyDesignPopulation").
The plannedAge, plannedCompletionNumberRange, and plannedEnrollmentNumberRange attributes are nested Range objects.
The plannedEnrollmentNumberQuantity and plannedCompletionNumberQuantity attributes are nested Quantity objects.
The includesHealthySubjects attribute must be a boolean.
Relationships to criteria and cohorts are optional and should be represented as arrays of linked object IDs.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "5.1 Inclusion Criteria",
  "extracted_text": "The study will enroll a total of up to 10 participants. The study population consists of adults with Wilson disease (WD) between the ages of 18 and 65. All participants must meet the inclusion criteria."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyDesignPopulation": {
    "id": "StudyDesignPopulation_001",
    "instanceType": "StudyDesignPopulation",
    "extensionAttributes": null,
    "name": "General Study Population",
    "description": "The study population consists of adults with Wilson disease (WD) between the ages of 18 and 65.",
    "label": "Overall Study Population",
    "plannedSex": null,
    "includesHealthySubjects": false,
    "plannedAge": {
      "id": "Range_001",
      "instanceType": "Range",
      "extensionAttributes": null,
      "minValue": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "value": 18.0,
        "unit": {
          "id": "AliasCode_001",
          "name": "Years"
        }
      },
      "maxValue": {
        "id": "Quantity_002",
        "instanceType": "Quantity",
        "value": 65.0,
        "unit": {
          "id": "AliasCode_002",
          "name": "Years"
        }
      },
      "isApproximate": false
    },
    "plannedCompletionNumberRange": null,
    "plannedCompletionNumberQuantity": null,
    "plannedEnrollmentNumberRange": {
      "id": "Range_002",
      "instanceType": "Range",
      "extensionAttributes": null,
      "maxValue": {
        "id": "Quantity_003",
        "instanceType": "Quantity",
        "value": 10.0,
        "unit": {
          "id": "AliasCode_003",
          "name": "Participants"
        }
      },
      "minValue": null,
      "isApproximate": true
    },
    "plannedEnrollmentNumberQuantity": null,
    "notes": "",
    "criteria": [
      {
        "id": "EligibilityCriterion_001"
      }
    ],
    "cohorts": [
      {
        "id": "StudyCohort_001"
      }
    ]
  }
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyelement:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study element—a basic building block of the study timeline—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyElement. Understand each attribute's purpose, data type, and cardinality. Note the optional relationships to transitionEndRule, studyInterventions, and transitionStartRule.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content, focusing on the detailed breakdown of the study periods. Your goal is to identify and extract the name of each distinct element, its description, and any rules that govern its start and end. Also, identify any interventions that take place within this element.
Populate the USDM Schema: Fill the StudyElement schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., StudyElement_001). Populate the attributes name, description, label, and notes. For relationships (transitionEndRule, studyInterventions, transitionStartRule), provide their unique identifiers and do not attempt to fit information into them.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyElement").
The name attribute should be a concise identifier for the element (e.g., "Treatment Period - High Dose").
transitionEndRule and transitionStartRule are optional relationships to a TransitionRule object.
studyInterventions is a relationship to a list of StudyIntervention objects.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Overall Design",
  "extracted_text": "The 12-week Treatment Period is the main element of the study. It begins after randomization and ends at Week 12. Patients in the low-dose arm will receive 15 mg of ALXN1840 daily during this period."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyElements": [
    {
      "id": "StudyElement_001",
      "instanceType": "StudyElement",
      "extensionAttributes": null,
      "name": "Treatment Period",
      "description": "The main element of the study, lasting 12 weeks.",
      "label": "Treatment Period",
      "notes": "",
      "transitionEndRule": {
        "id": "TransitionRule_001"
      },
      "studyInterventions": [
        {
          "id": "StudyIntervention_001"
        }
      ],
      "transitionStartRule": {
        "id": "TransitionRule_002"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyepochandstudyidentifier:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's epochs (named time periods) and its identifiers and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schemas: Thoroughly analyze the provided USDM schemas for StudyEpoch and StudyIdentifier. Understand each attribute's purpose, data type, and cardinality. Note the relationships, particularly the next and previous links in StudyEpoch and the mandatory scope relationship in StudyIdentifier.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract all information about the study's sequential phases (e.g., Screening, Treatment, Follow-up) and the official identifiers assigned to the study by the sponsor or a registry.
Populate the USDM Schemas:
StudyEpoch: For each named time period, provide a unique, arbitrary identifier (e.g., StudyEpoch_001). Populate the attributes name, description, label, type, and notes. Use the previous and next relationships to link the epochs chronologically using their respective IDs.
StudyIdentifier: For each study identifier, provide a unique, arbitrary identifier (e.g., StudyIdentifier_001). Populate the attributes text and scope. The scope must be a mandatory relationship to an Organization object.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyEpoch").
For attributes that point to a Code object, use the CNCIt-001 placeholder for the code ID.
The type attribute for StudyEpoch is a Code object (e.g., "Treatment," "Screening").
The scope attribute for StudyIdentifier is a mandatory relationship to an Organization object.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.1 Overall Design",
  "extracted_text": "The study consists of a Screening Period, a Treatment Period, and a Follow-up Period. Screening will last up to 4 weeks. The Treatment Period is 12 weeks. The sponsor protocol ID is ALXN1840-C-201. The ClinicalTrials.gov ID is NCT01234567."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyEpochs": [
    {
      "id": "StudyEpoch_001",
      "instanceType": "StudyEpoch",
      "extensionAttributes": null,
      "name": "Screening Period",
      "description": "The period for screening participants.",
      "label": "Screening",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Screening"
      },
      "notes": "Lasts up to 4 weeks.",
      "previous": null,
      "next": {
        "id": "StudyEpoch_002"
      }
    },
    {
      "id": "StudyEpoch_002",
      "instanceType": "StudyEpoch",
      "extensionAttributes": null,
      "name": "Treatment Period",
      "description": "The period for administering the study drug.",
      "label": "Treatment",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Treatment"
      },
      "notes": "Lasts 12 weeks.",
      "previous": {
        "id": "StudyEpoch_001"
      },
      "next": {
        "id": "StudyEpoch_003"
      }
    },
    {
      "id": "StudyEpoch_003",
      "instanceType": "StudyEpoch",
      "extensionAttributes": null,
      "name": "Follow-up Period",
      "description": "The period following the end of treatment.",
      "label": "Follow-up",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Follow-up"
      },
      "notes": "",
      "previous": {
        "id": "StudyEpoch_002"
      },
      "next": null
    }
  ],
  "studyIdentifiers": [
    {
      "id": "StudyIdentifier_001",
      "instanceType": "StudyIdentifier",
      "extensionAttributes": null,
      "text": "ALXN1840-C-201",
      "scope": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "name": "Alexion Pharmaceuticals, Inc."
      }
    },
    {
      "id": "StudyIdentifier_002",
      "instanceType": "StudyIdentifier",
      "extensionAttributes": null,
      "text": "NCT01234567",
      "scope": {
        "id": "Organization_002",
        "instanceType": "Organization",
        "name": "ClinicalTrials.gov"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyidentifier:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's identifiers—a sequence of characters used to identify, name, or characterize the study—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyIdentifier. Understand each attribute's purpose, data type, and cardinality. Note that the scope attribute is a mandatory relationship to the Organization class.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any official or internal identifiers used to reference the study, such as protocol numbers, registration numbers (e.g., ClinicalTrials.gov ID), or sponsor codes. These are often explicitly listed in the title page, synopsis, or a dedicated "Study Identifiers" section.
Populate the USDM Schema: Fill the StudyIdentifier schema template with the relevant information extracted from the protocol. For each identifier, provide a unique, arbitrary identifier (e.g., StudyIdentifier_001). Populate the attributes text and scope according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyIdentifier").
The text attribute should contain the literal identifier string (e.g., "NCT01234567" or "ALXN1840-C-201").
The scope attribute is a mandatory relationship. You must link it to a pre-defined or newly created Organization object by its unique identifier (e.g., scope: { "id": "Organization_001" }). This object represents the entity that assigned the identifier, such as the sponsor or a clinical trial registry.
If the protocol provides an identifier without explicitly naming the assigning organization, use a generic placeholder organization (e.g., Organization_Sponsor or Organization_Registry).
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Identification",
  "extracted_text": "Sponsor Protocol Number: ALXN1840-C-201ClinicalTrials.gov Identifier: NCT01234567"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyIdentifiers": [
    {
      "id": "StudyIdentifier_001",
      "instanceType": "StudyIdentifier",
      "extensionAttributes": null,
      "text": "ALXN1840-C-201",
      "scope": {
        "id": "Organization_001",
        "instanceType": "Organization",
        "name": "Alexion Pharmaceuticals, Inc."
      }
    },
    {
      "id": "StudyIdentifier_002",
      "instanceType": "StudyIdentifier",
      "extensionAttributes": null,
      "text": "NCT01234567",
      "scope": {
        "id": "Organization_002",
        "instanceType": "Organization",
        "name": "ClinicalTrials.gov"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyintervention:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study intervention—any agent, device, or procedure being tested—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyIntervention. Understand each attribute's purpose, data type, and cardinality. Note the relationships to administrations and nested Code and Quantity objects.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract all details about the investigational agents, devices, or procedures. Look for the product's name, its role (e.g., experimental, placebo), type (e.g., drug, device), and any associated administration details.
Populate the USDM Schema: Fill the StudyIntervention schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., StudyIntervention_001). Populate the attributes name, description, label, role, type, codes, minimumResponseDuration, and notes. For the administrations relationship, just provide the unique identifiers of the related Administration objects.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyIntervention").
The role and type attributes are Code objects. Use the CNCIt-001 placeholder for the code ID.
The codes attribute is a list of Code objects.
The minimumResponseDuration is an optional Quantity object.
The administrations attribute is a relationship to a list of Administration objects. You should link to them by their unique identifiers.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "6.4 Study Intervention",
  "extracted_text": "The investigational medicinal product, ALXN1840, is used in this study. Its role is as a treatment. The dose is 15 mg/day administered orally. The minimum duration to assess a response is 4 weeks. A placebo will be used as a comparator."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyInterventions": [
    {
      "id": "StudyIntervention_001",
      "instanceType": "StudyIntervention",
      "extensionAttributes": null,
      "description": "The investigational medicinal product, ALXN1840, is used as a treatment.",
      "name": "ALXN1840",
      "label": "Study Drug",
      "role": {
        "id": "Code_CNCIt-001",
        "name": "Treatment"
      },
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Drug"
      },
      "codes": [
        {
          "id": "Code_CNCIt-001",
          "name": "ALXN1840"
        }
      ],
      "minimumResponseDuration": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "extensionAttributes": null,
        "value": 4.0,
        "unit": {
          "id": "AliasCode_001",
          "instanceType": "AliasCode",
          "extensionAttributes": null,
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Weeks"
          }
        }
      },
      "notes": "",
      "administrations": [
        {
          "id": "Administration_001"
        }
      ]
    },
    {
      "id": "StudyIntervention_002",
      "instanceType": "StudyIntervention",
      "extensionAttributes": null,
      "description": "A placebo will be used as a comparator to the study drug.",
      "name": "Placebo",
      "label": "Placebo",
      "role": {
        "id": "Code_CNCIt-001",
        "name": "Comparator"
      },
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Drug"
      },
      "codes": [],
      "minimumResponseDuration": null,
      "notes": "",
      "administrations": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyrole:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about the roles of study personnel and organizations and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyRole. Understand each attribute's purpose, data type, and cardinality. Note the relationships to assignedPersons, masking, organizations, and appliesTo, all of which have a cardinality of 0..* or 0..1.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract all roles defined in the study, such as "Sponsor," "Principal Investigator," or "Study Pharmacist." For each role, you'll need to identify the associated individuals, organizations, and any masking details.
Populate the USDM Schema: Fill the StudyRole schema template with the relevant information extracted from the protocol. For each role, provide a unique, arbitrary identifier (e.g., StudyRole_001). Populate the attributes name, label, description, and code. For relationships (assignedPersons, masking, organizations, appliesTo), provide their unique identifiers and do not attempt to nest the full object definitions.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyRole").
The code attribute is a nested Code object that specifies the role type (e.g., "Sponsor", "Investigator"). Use the CNCIt-001 placeholder for the code ID.
The assignedPersons and organizations relationships are optional arrays of links to AssignedPerson and Organization objects.
The masking relationship is an optional link to a Masking object.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Signature Page",
  "extracted_text": "Sponsor: Alexion Pharmaceuticals, Inc.Principal Investigator: Dr. Jane Doe, M.D."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyRoles": [
    {
      "id": "StudyRole_001",
      "instanceType": "StudyRole",
      "extensionAttributes": null,
      "name": "Sponsor",
      "label": "Sponsor",
      "description": "The sponsor of the study.",
      "code": {
        "id": "Code_CNCIt-001",
        "name": "Sponsor"
      },
      "assignedPersons": [],
      "masking": null,
      "organizations": [
        {
          "id": "Organization_001"
        }
      ],
      "appliesTo": []
    },
    {
      "id": "StudyRole_002",
      "instanceType": "StudyRole",
      "extensionAttributes": null,
      "name": "Principal Investigator",
      "label": "Principal Investigator",
      "description": "The person responsible for the conduct of the clinical trial at a study site.",
      "code": {
        "id": "Code_CNCIt-001",
        "name": "Principal Investigator"
      },
      "assignedPersons": [
        {
          "id": "AssignedPerson_001"
        }
      ],
      "masking": null,
      "organizations": [],
      "appliesTo": []
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studysite:
        ROLE_TEMPLATE = """
You're a clinical data management and protocol analysis expert.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study site—a physical location where study activities are conducted—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudySite. Understand each attribute's purpose, data type, and cardinality. Note that country is a nested Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract the names of participating study centers or locations. You should also find any descriptions, labels, or country information associated with these sites.
Populate the USDM Schema: Fill the StudySite schema template with the relevant information extracted from the protocol. For each site, provide a unique, arbitrary identifier (e.g., StudySite_001). Populate the attributes name, description, label, and country according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudySite").
The name attribute should be the literal name of the study site (e.g., "Massachusetts General Hospital").
The country attribute is a nested Code object. Use the CNCIt-001 placeholder for the code ID, and the name should be the country's full name.
If a field, such as description or label, is not explicitly mentioned, leave it as a blank string "".
If the protocol lists multiple sites, you must create a separate StudySite object for each.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "List of Study Sites",
  "extracted_text": "Study activities will be performed at the following locations: Boston Medical Center (United States) and the University of Toronto Hospital (Canada)."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studySites": [
    {
      "id": "StudySite_001",
      "instanceType": "StudySite",
      "extensionAttributes": null,
      "name": "Boston Medical Center",
      "description": "",
      "label": "Boston Medical Center",
      "country": {
        "id": "Code_CNCIt-001",
        "name": "United States of America"
      }
    },
    {
      "id": "StudySite_002",
      "instanceType": "StudySite",
      "extensionAttributes": null,
      "name": "University of Toronto Hospital",
      "description": "",
      "label": "University of Toronto Hospital",
      "country": {
        "id": "Code_CNCIt-001",
        "name": "Canada"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studytitle:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's title and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyTitle. Understand each attribute's purpose, data type, and cardinality. Note that type is a nested Code object.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract the official title of the study, which may be a short title, a formal title, or a public title. This information is typically found on the cover page or in the synopsis.
Populate the USDM Schema: Fill the StudyTitle schema template with the relevant information extracted from the protocol. For each title, provide a unique, arbitrary identifier (e.g., StudyTitle_001). Populate the attributes type and text according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyTitle").
The text attribute should contain the literal, full text of the study title.
The type attribute is a nested Code object that classifies the type of title (e.g., "Official Title," "Short Title," "Public Title"). Use the CNCIt-001 placeholder for the code ID.
If the protocol lists multiple titles (e.g., both a public and a scientific title), you should create a separate StudyTitle object for each.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Protocol Title Page",
  "extracted_text": "Protocol Title: A Phase 2 Study to Evaluate the Efficacy and Safety of ALXN1840 in Wilson Disease"
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyTitles": [
    {
      "id": "StudyTitle_001",
      "instanceType": "StudyTitle",
      "extensionAttributes": null,
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Official Title"
      },
      "text": "A Phase 2 Study to Evaluate the Efficacy and Safety of ALXN1840 in Wilson Disease"
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Studyversion:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study version—a specific plan for a study at a given point in time—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for StudyVersion. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationships to studyIdentifiers and titles, and the many optional relationships to other classes. For all attributes with a cardinality other than null, you should only provide an identifier and move on.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract the version identifier (e.g., "Version 1.0"), the study's overall rationale, and its business therapeutic area. You also need to link this version to its various components, such as identifiers, titles, and amendments.
Populate the USDM Schema: Fill the StudyVersion schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for the instance (e.g., StudyVersion_001). Populate the attributes versionIdentifier, businessTherapeuticAreas, rationale, and notes. For all relationships, provide the unique identifiers of the related objects in an array.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "StudyVersion").
The versionIdentifier is a string. The businessTherapeuticAreas is a nested Code object. Use the CNCIt-001 placeholder for the code ID.
The relationships studyIdentifiers and titles are mandatory and must be an array of linked object IDs.
Relationships to abbreviations, dateValues, referenceIdentifiers, amendments, documentVersions, and studyDesigns are optional arrays of linked object IDs.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "PROTOCOL",
  "extracted_text": "Protocol Version 1.0, dated 12 May 2020. This is a study on Wilson disease with a primary focus on the business unit's rare disease portfolio. The rationale is to evaluate a new treatment in this indication. The sponsor protocol number is ALXN1840-C-201."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "studyVersions": [
    {
      "id": "StudyVersion_001",
      "instanceType": "StudyVersion",
      "extensionAttributes": null,
      "versionIdentifier": "1.0",
      "businessTherapeuticAreas": {
        "id": "Code_CNCIt-001",
        "name": "Rare Disease"
      },
      "rationale": "The rationale is to evaluate a new treatment in this indication.",
      "notes": "",
      "abbreviations": [],
      "dateValues": [
        {
          "id": "GovernanceDate_001"
        }
      ],
      "referenceIdentifiers": [
        {
          "id": "ReferenceIdentifier_001"
        }
      ],
      "amendments": [],
      "documentVersions": [
        {
          "id": "StudyDefinitionDocumentVersion_001"
        }
      ],
      "studyDesigns": [
        {
          "id": "StudyDesign_001"
        }
      ],
      "studyIdentifiers": [
        {
          "id": "StudyIdentifier_001"
        }
      ],
      "titles": [
        {
          "id": "StudyTitle_001"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Subjectenrollment:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about subject enrollment and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for SubjectEnrollment. Understand each attribute's purpose, data type, and cardinality. Note the relationships to Quantity, GeographicScope, StudyCohort, and StudySite.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any information regarding the number of subjects enrolled. This information may be broken down by a specific geographic location (e.g., country), a particular study cohort, or an individual study site.
Populate the USDM Schema: Fill the SubjectEnrollment schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., SubjectEnrollment_001). Populate the attributes name, description, label, and quantity. For relationships, provide the unique identifiers of the related objects and do not attempt to nest the full object definitions.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "SubjectEnrollment").
The quantity attribute is a nested Quantity object and should include both a value (a number) and a unit (a nested AliasCode).
The relationships to forGeographicScope, forStudyCohort, and forStudySite are all optional (0..1) and should link to a specific instance of those classes using its unique id.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "9.2 Patient Recruitment",
  "extracted_text": "The planned enrollment is a total of 100 subjects. The first 50 subjects will be enrolled in the United States, and the remaining subjects in Canada."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "subjectEnrollments": [
    {
      "id": "SubjectEnrollment_001",
      "instanceType": "SubjectEnrollment",
      "extensionAttributes": null,
      "name": "United States Enrollment",
      "description": "Planned enrollment of 50 subjects in the United States.",
      "label": "US Enrollment",
      "quantity": {
        "id": "Quantity_001",
        "instanceType": "Quantity",
        "extensionAttributes": null,
        "value": 50.0,
        "unit": {
          "id": "AliasCode_001",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Subjects"
          }
        }
      },
      "forGeographicScope": {
        "id": "GeographicScope_001"
      },
      "forStudyCohort": null,
      "forStudySite": null
    },
    {
      "id": "SubjectEnrollment_002",
      "instanceType": "SubjectEnrollment",
      "extensionAttributes": null,
      "name": "Canada Enrollment",
      "description": "Planned enrollment of the remaining subjects in Canada.",
      "label": "Canada Enrollment",
      "quantity": {
        "id": "Quantity_002",
        "instanceType": "Quantity",
        "extensionAttributes": null,
        "value": 50.0,
        "unit": {
          "id": "AliasCode_002",
          "instanceType": "AliasCode",
          "standardCode": {
            "id": "Code_CNCIt-001",
            "name": "Subjects"
          }
        }
      },
      "forGeographicScope": {
        "id": "GeographicScope_002"
      },
      "forStudyCohort": null,
      "forStudySite": null
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Substance:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a substance—any matter with a defined composition—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Substance. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationship to strengths (a cardinality of 1..*), the optional relationship to referenceSubstance, and the nested Code objects for codes.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any details about the active or inactive components of a study drug, including their names, descriptions, and their strengths.
Populate the USDM Schema: Fill the Substance schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Substance_001). Populate the attributes name, description, label, codes, strengths, and referenceSubstance. For the strengths and referenceSubstance relationships, just provide the unique identifiers of the related objects and do not attempt to nest the full object definitions.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Substance").
The codes attribute is an array of Code objects. Use the CNCIt-001 placeholder for the code ID.
The strengths attribute is a mandatory relationship to a list of Strength objects. You must link to them by their unique identifiers (e.g., strengths: [{ "id": "Strength_001" }]).
The referenceSubstance is an optional relationship to another Substance object.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Study Product Description",
  "extracted_text": "The active substance in the study drug is ALXN1840. The drug is available as 15 mg tablets."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "substances": [
    {
      "id": "Substance_001",
      "instanceType": "Substance",
      "extensionAttributes": null,
      "name": "ALXN1840",
      "description": "The active substance in the study drug.",
      "label": "Active Substance",
      "codes": [
        {
          "id": "Code_CNCIt-001",
          "name": "ALXN1840"
        }
      ],
      "strengths": [
        {
          "id": "Strength_001"
        }
      ],
      "referenceSubstance": null
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Syntaxtemplate:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a syntax template—a standardized pattern used for structured text—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for SyntaxTemplate. Understand each attribute's purpose, data type, and cardinality. Note the optional relationship to dictionary.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any standardized text patterns or rules, particularly those that use variables or placeholders to define content. These can be found in sections that describe standardized boilerplate language.
Populate the USDM Schema: Fill the SyntaxTemplate schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., SyntaxTemplate_001). Populate the attributes name, description, label, text, and notes. For the dictionary relationship, provide the unique identifier of the related SyntaxTemplateDictionary object if applicable.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "SyntaxTemplate").
The text attribute should contain the core structured text string, including any placeholders or variables.
The name attribute should be a concise identifier for the template.
The dictionary attribute is an optional relationship. If it's not present, leave it as null.
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Adverse Event Reporting",
  "extracted_text": "The protocol states that all adverse events should be reported if they are 'related to study drug' and 'at least severity level <SEVERITY_LEVEL>'. The severity level is defined in the medical dictionary."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "syntaxTemplates": [
    {
      "id": "SyntaxTemplate_001",
      "instanceType": "SyntaxTemplate",
      "extensionAttributes": null,
      "name": "Adverse Event Reporting Rule",
      "description": "A template for reporting adverse events.",
      "label": "AE Reporting Rule",
      "text": "related to study drug and at least severity level <SEVERITY_LEVEL>",
      "notes": "",
      "dictionary": {
        "id": "SyntaxTemplateDictionary_001"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Syntaxtemplatedictionary:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a syntax template dictionary and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for SyntaxTemplateDictionary. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationship to parameterMaps (a cardinality of 1..*).
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any sections that define a set of valid parameters, values, or codes used within a standardized text template. This could be a list of severity levels, a set of dose values, or other structured look-up information.
Populate the USDM Schema: Fill the SyntaxTemplateDictionary schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., SyntaxTemplateDictionary_001). Populate the attributes name, description, and label. For the parameterMaps relationship, you must provide the unique identifiers of the related ParameterMap objects.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "SyntaxTemplateDictionary").
The name attribute should be a concise identifier for the dictionary (e.g., "Severity Level Dictionary").
The parameterMaps attribute is a mandatory relationship to a list of ParameterMap objects. You must link to them by their unique identifiers (e.g., parameterMaps: [{"id": "ParameterMap_001"}]).
If a field is not explicitly mentioned, leave it as a blank string "", null, or an empty array [] as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "Adverse Event Reporting",
  "extracted_text": "The severity level is defined in the medical dictionary. The possible values are: 1 (Mild), 2 (Moderate), 3 (Severe)."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "syntaxTemplateDictionaries": [
    {
      "id": "SyntaxTemplateDictionary_001",
      "instanceType": "SyntaxTemplateDictionary",
      "extensionAttributes": null,
      "name": "Severity Level Dictionary",
      "description": "A dictionary defining the severity levels for adverse events.",
      "label": "Severity Dictionary",
      "parameterMaps": [
        {
          "id": "ParameterMap_001"
        },
        {
          "id": "ParameterMap_002"
        },
        {
          "id": "ParameterMap_003"
        }
      ]
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Timing:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a study's timing—the chronological relationship between events—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for Timing. Understand each attribute's purpose, data type, and cardinality. Note the mandatory relationship to relativeFromScheduledInstance and the optional relationship to relativeToScheduledInstance. Also, pay attention to the attributes that define time windows and their labels.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any temporal details, such as event schedules, time windows for assessments, or the relationship between two events (e.g., "30 days after the last dose").
Populate the USDM Schema: Fill the Timing schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., Timing_001). Populate the attributes name, description, label, type, relativeToFrom, value, valueLabel, windowLabel, windowLower, and windowUpper. For relationships, provide their unique identifiers and do not attempt to nest the full object definitions.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "Timing").
The type and relativeToFrom attributes are Code objects. Use the CNCIt-001 placeholder for the code ID.
The relativeFromScheduledInstance relationship is mandatory and should link to the event from which the timing is measured. The relativeToScheduledInstance is for the event being timed.
The value attribute contains the central time point (e.g., "30 days"), and windowLower/windowUpper contain the boundaries of a time window (e.g., "Day -28" and "Day -1").
If a field is not explicitly mentioned, leave it as a blank string "" or null as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "4.2 Schedule of Activities",
  "extracted_text": "The first treatment visit (Visit 2) occurs exactly 7 days after the screening visit (Visit 1). The screening visit has a window of Day -28 to Day -1."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "timings": [
    {
      "id": "Timing_001",
      "instanceType": "Timing",
      "extensionAttributes": null,
      "name": "Screening Window",
      "description": "The time window for the screening visit.",
      "label": "Screening Window",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Offset from Reference"
      },
      "relativeToFrom": {
        "id": "Code_CNCIt-001",
        "name": "Study Day"
      },
      "value": null,
      "valueLabel": null,
      "windowLabel": "Screening",
      "windowLower": "Day -28",
      "windowUpper": "Day -1",
      "relativeToScheduledInstance": {
        "id": "ScheduledInstance_001"
      },
      "relativeFromScheduledInstance": null
    },
    {
      "id": "Timing_002",
      "instanceType": "Timing",
      "extensionAttributes": null,
      "name": "Visit 2 Timing",
      "description": "Visit 2 occurs exactly 7 days after Visit 1.",
      "label": "Visit 2",
      "type": {
        "id": "Code_CNCIt-001",
        "name": "Offset from Reference"
      },
      "relativeToFrom": {
        "id": "Code_CNCIt-001",
        "name": "Day"
      },
      "value": "7",
      "valueLabel": "7 days",
      "windowLabel": null,
      "windowLower": null,
      "windowUpper": null,
      "relativeToScheduledInstance": {
        "id": "ScheduledInstance_002"
      },
      "relativeFromScheduledInstance": {
        "id": "ScheduledInstance_001"
      }
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""

class Transitionrule:
        ROLE_TEMPLATE = """
You are an expert in clinical data management and protocol analysis.
"""

        INSTRUCTION_TEMPLATE = """
Meticulously map the provided unstructured clinical protocol content to a structured Unified Study Definition Model (USDM) schema. You must extract key information about a transition rule—a rule that governs the movement of subjects within a study—and populate the schema while maintaining the original structure.

Chain of Command
Analyze the USDM Schema: Thoroughly analyze the provided USDM schema template for TransitionRule. Understand each attribute's purpose, data type, and cardinality.
Analyze the Clinical Protocol Content: Carefully read and analyze the provided clinical protocol content. Your goal is to identify and extract any specific rules or conditions that dictate how a subject moves from one part of the study to another (e.g., from screening to treatment, or from a treatment arm to discontinuation).
Populate the USDM Schema: Fill the TransitionRule schema template with the relevant information extracted from the protocol. Provide a unique, arbitrary identifier for each instance (e.g., TransitionRule_001). Populate the attributes name, description, label, and text according to the data you extracted.
Final Output: Present the final output in a valid JSON format.

Notes to Keep in Mind
Every class should have an extensionAttributes attribute which must be null, and an instanceType attribute that explicitly declares what the JSON object represents (e.g., "instanceType": "TransitionRule").
The name attribute should be a concise identifier for the rule (e.g., "Randomization Rule").
The text attribute should contain the literal, verbatim text of the rule from the protocol.
If a field is not explicitly mentioned, leave it as a blank string "" or null as appropriate.
Review the example provided to understand how the input is interpreted and how the output JSON should be structured.
"""

        EXAMPLE_INPUT = """
JSON
{
  "title": "5.1 Inclusion Criteria",
  "extracted_text": "To be randomized into the treatment period, subjects must meet all inclusion criteria and have no exclusionary findings from the screening visit."
}
"""

        EXAMPLE_OUTPUT = """
JSON
{
  "transitionRules": [
    {
      "id": "TransitionRule_001",
      "instanceType": "TransitionRule",
      "extensionAttributes": null,
      "name": "Entry to Treatment Period",
      "description": "Rule for a subject to transition from screening to the treatment period.",
      "label": "Randomization Criteria",
      "text": "To be randomized into the treatment period, subjects must meet all inclusion criteria and have no exclusionary findings from the screening visit."
    }
  ]
}
"""

        INPUT_TEMPLATE = """
{INPUT_DATA}
"""
