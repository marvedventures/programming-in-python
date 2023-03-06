###########################################################################################################################################
# WHAT IS TESTING?
###########################################################################################################################################

# CATEGORIZING TEST TYPES:

# 1. White-Box tests
# -> tester has knowledge of the code design and functionalities

# 2. Black-Box TESTS
# -> tester has no idea of internal implementation

###########################################################################################################################################

# OTHER WAYS TO CATEGORIZE DIFFERENT TESTS:

# 1. Functional Tests
# -> based on the business requirements stated
# -> features and functionalities are in line with the expectations

# 2. Non-Functional Tests
# ->  more complex to define and involve metrics such as overall performance and quality of the product

# 3. Maintenance Tests
# -> occur when the system and its operational environment is corrected, changed or extended

###########################################################################################################################################

# MOST BROADLY ACCEPTED CATEGORIZATION -> LEVELS OF TESTING

# 4 MAIN LEVELS OF TESTING (FUNCTIONAL TESTING)

# 1. Unit/Component Testing
# -> program tests specific individual components by isolating them
# -> components are low level: they are closer to the actual written code
# -> devs write tests while writing code
# -> PyTest


# 2. Integration Testing
# -> combines the unit tests and test the flow of data from one component to another
# -> 'interface': if the data is correctly fetched from a database within python code -> sent to webpage
# -> approaches:  top down, bottom up and sandwich approaches.


# 3. System Testing
# -> tests all the software you tested against the set requirements and expectations to ensure completeness.
# -> also known as end-to-end testing
# -> reliability, performance, security and load balancing
# -> measures operability in the working env. such as platform and operating system
# -> shipping of software to stakeholders and end-users happen after this phase


# 4. Acceptance Testing
# -> ready for deployment
# -> expected to be bug free and meet the set standards
# -> stakeholders and the select few end users are involved in acceptance testing
# -> normally involves alpha, beta and regression testing
# -> approach : pre-written scenarios -> use results to find bugs that were missed earlier

###########################################################################################################################################

# AGILE MODEL
# -> release iteratively and perform acceptance testing regularly

###########################################################################################################################################
