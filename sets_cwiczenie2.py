list_of_emails = []


for a in range(10):
    user_email = input('Podaj mi swój email: ')
    if user_email == '@' and (user_email == '.com' or user_email == '.pl'):
        list_of_emails.append(user_email)

print(list_of_emails)
print ('---'* 20)

unique_list_of_emails = set(list_of_emails)
print(unique_list_of_emails)





