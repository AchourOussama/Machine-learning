import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv", index_col ="Ticket No")



# Add seconds : sometimes we fall into having datetime1 with seconds and datetime2 without seconds
# Therefore, we always add seconds so that calculations could be done with out erros
data['Create Date']=data['Create Date'].apply(lambda x: x + ":00" if len(x.split(':')) == 2 else x)
data['Completed Date']=data['Completed Date'].apply(lambda x: x + ":00" if len(x.split(':')) == 2 else x)

# Correct badly formatted inputs : 
data['Create Time'] = pd.to_datetime(data['Create Date'], errors='coerce', format='%m/%d/%Y %H:%M:%S')
data['Completed Time'] = pd.to_datetime(data['Completed Date'], errors='coerce', format='%m/%d/%Y %H:%M:%S')


# Identify rows with incorrect datetime formats
incorrect_completed_time = data['Completed Time'].isnull()
incorrect_create_time = data['Create Time'].isnull()
print("Incorrect values in Create Time\n",incorrect_create_time[incorrect_create_time==True])
print("Incorrect values in Completed Time\n",incorrect_completed_time[incorrect_completed_time==True])

# Delete rows where datetime values are badly formatted
print("remaining data :\n",data.dropna(subset=['Create Time','Completed Time'],inplace=True))

### Script to fix bad formats
# # If there are rows with incorrect formats, try to fix them
# print(data.loc[incorrect_date_mask, 'Completed Date'])
# if incorrect_date_mask.any():
#     for ticket in data.loc[incorrect_date_mask, 'Completed Date']:
#         try:
#         #     corrected_ticket = pd.to_datetime(ticket, format='%m/%d/%Y %H:%M:%S')
#             # corrected_ticket =pd.to_datetime(ticket,format='%m-%d-%Y\s+%H:%M:%S', errors='coerce').strftime(format='%m/%d/%Y %H:%M')
#             # # corrected_ticket =ticket.strftime(format='%m/%d/%Y %H:%M:%S')
#             # print("right format",corrected_ticket)
#             # data.at[data.loc[data==ticket].index(), 'Completed Date'] = corrected_ticket
#             formatted_ticket = ticket.replace('-','/')
#             formatted_ticket = formatted_ticket.replace('  ',' ')

#             #checking the formatting results
#             print(f"Original Date: {ticket}")
#             print(f"Formatted Date: {formatted_ticket}")
#             print(data.loc[data['Completed Date']==ticket].index[0])
#             data.at[data.loc[data['Completed Date']==ticket].index[0], 'Completed Date'] = formatted_ticket

#         except ValueError:
#             print("error formatting the data")
#             # Handle cases where the value cannot be corrected
#             pass

# # Now 'date_column' should have correct datetime format for all values

# ### End

# use the errors attribute :  make any datetime which is badly formatted as NaN . Therefore, no time_difference
# calculation would be made
 
data['begin']=pd.to_datetime(data['Create Date'],format='%m/%d/%Y %H:%M:%S',errors='coerce')
data['end']=pd.to_datetime(data['Completed Date'],format='%m/%d/%Y %H:%M:%S',errors='coerce')

# Calculate the time difference between 't2' and 't1'
data['time_difference'] = data['end'] - data['begin']

# Check results
print(data['time_difference'])

# Calculate the average time difference
average_time_difference = data['time_difference'].mean()
print(f"Average Time Difference: {average_time_difference}")
