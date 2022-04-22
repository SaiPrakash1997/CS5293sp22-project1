# cs5293sp22-project1

## Minimum system requirements:

Machine configuration:

Machine type: e2-standard-2

vCPU: 2

Memory: 8GB

CPU Platform: Intel Broadwell


Note: These are minimum system requirements needed for compute engine to run my application without any issues.


## Changes

### Small amount of Features Found - Gender:

* I have added more gender revealing terms to the list that I have pre-defined in the method redactGenders().

* Initially, one of my regex was causing few unwanted redactions in the file like 'her' in 'other' and 'her' in 'mother'. To overcome this issue, I have re-written regular expressions that solve this issue effectively.
  

                    content = re.sub("^"+toReplace+"\s", "█"*len(toReplace) + " ", content)
                    content = re.sub("\s"+toReplace+"\s", " "+"█"*len(toReplace)+" ", content)
                    content = re.sub("\s"+toReplace+"[.]", " " + "█"*len(toReplace)+".", content)
                    content = re.sub(toReplace + "[/]", "█" * len(toReplace) + "/", content)
                    content = re.sub("[/]"+toReplace+"\W", "/" + "█" * len(toReplace), content)


                    Example: 
                       regex 1: When String starts with gender revealing terms like 'She is good at baseball.'
                       regex 2: when gender revealing term appears in the middle of a string like 'Karen is known for her cooking skills.'
                       regex 3: When gender revealing term appears at the end of the sentence like 'I am in love with her.' and at the end of signature like /she/ or /he/
                       regex 4: when gender revealing term appears below the signature of an email like he/ or she/
                       regex 5: When gender revealing term appears at the end of the signature like /him or /them


### Moderate amount of Features Found - Concept

* Now, I am considering the capitalized word for the concept passed, lower case word of the concept, and uppercase of the concept. 

* Let's say, if word 'kid' is passed then I am getting all the synonyms first and doing the same as storing the capitalized word, lower case word, and uppercase word in a list and if a sentence contains a word similar to one in the list. The whole sentence will be redacted.

                    
 
                    Changed Code: 
                        _lowerCase = words.lower()
                        _capitalize = words.capitalize()
                        _upperCase = words.upper()
                        conceptWords.append(_lowerCase)
                        conceptWords.append(_capitalize)
                        conceptWords.append(_upperCase)


### Small amount of Features Found - Addresses

* Like earlier, I am using pyap library to identify addresses in a file. Rather than splitting the string into multiple strings based on ',' character to perform redaction.

* Now, I am using below regular expression to redact the string in a file.

                
                Regex:
                  content = re.sub(addressStartWord+".*[\n]*.*[\n]*.*[\n]*.*[\n]*.*"+addressEndWord, "█" * len(address), content)

                Example:
                  2236 Houston Ave
                  Norman,
                  OK 73071
                  
                Code: 
                    addressStartWord = address[0]+address[1]+address[2]
                    addressEndWord = address[-5]+address[-4]+address[-3]+address[-2]+address[-1]

* Above code gathers the first 3 letters of an address string to store in 'addressStartWord' and last 5 letters of an address string to store in 'addressEndWord'.

* Finally, it performs redaction using re.sub() method.


### Tests

* The changed code doesn't require to re-write any test functions.


