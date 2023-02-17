###########################################################################################################################################
# MATCH STATEMENT (SWITCH STATEMENT)
###########################################################################################################################################

# Match Statement - python v. 3.10
# compares a value to several different conditions until one is met.
# default is (_)
# or is (|)

###########################################################################################################################################

# Convert this if statement to match statement

http_status = 500

# If statement
if http_status == 200 or http_status == 201:
    print('Success!')
elif http_status == 400:
    print('Bad Request!')
elif http_status == 404:
    print('Not Found!')
elif http_status == 500 or http_status == 501:
    print('Server Error!')
else:
    print('Unknown.')


# Match Statement
match http_status:
    case 200 | 201:
        print('Success!')
    case 400:
        print('Bad Request!')
    case 404:
        print('Not Found!')
    case 500 | 501:
        print('Server Error!')
    case _:
        print('Unknown.')

###########################################################################################################################################
