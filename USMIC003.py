"""-----------------------------------------------------------------------------
| File: USMIC003.py                                                            |
| Author: Brandon Feder                                                        |
| Date: 04/02/24 -                                                             |
| Title: CodeCademy Business Intelligence Data Analyst Career Path             |
|              Portfolio Project: U.S. Medical Insurance Costs                 |
|                                                                              |
| Description: Analysis of trends amongst different groups of given ages,      |
| binary genders, BMIs, quantity of children, nicotine use, quadrant of the    |
| country, and cost of insurance per period.                                   |
-----------------------------------------------------------------------------"""

#import modules
import csv # import CSV module

# Convert CSV document to usable data in Python system
with open("insurance.csv", "r") as insurance_csv:
  insurance = csv.DictReader(insurance_csv)
  
  #Import header row    
  headers = insurance.fieldnames
  #print(headers)
  
  #Create empty lists for each row  
  ages = []
  sexes = []
  bmis = []
  kids = []
  nicotine = []
  regions = []
  costs = []
  id_num = []
  
  #Import values from csv rows to lists
  for row in insurance:
    ages.append(int(row['age']))
    sexes.append(row['sex'])
    bmis.append(float(row['bmi']))
    kids.append(int(row['children']))
    nicotine.append(row['smoker'])
    regions.append(row['region'])
    costs.append(float(row['charges']))


#Create dictionaries from imported rows
year_of_age = {headers[0]: ages}
genders = {headers[1]: sexes}
mass = {headers[2]: bmis}
offspring = {headers[3]: kids}
marlboros = {headers[4]: nicotine}
geography = {headers[5]: regions}
expenses = {headers[6]: costs}

#Create dictionary of all clients
clients = dict()
def create_clients(ages, sexes, bmis, kids, nicotine, regions, costs):
    num_clients = len(ages)
    for i in range(num_clients):
        clients[i] = {
            "ID Number": i + 1,
            "Age": ages[i],
            "Sex": sexes[i],
            "BMI": bmis[i],
            "Number of Children": kids[i],
            "Smoker": nicotine[i],
            "Region": regions[i],
            "Insurance cost": "${:,.2f}".format(costs[i])
        }
    return clients

clients = create_clients(ages, sexes, bmis, kids, nicotine, regions, costs)

#Calculate quantity of genders
women = 0
men = 0
for gender in sexes:
  if gender == 'female':
    women += 1
  elif gender == 'male':
    men += 1

#Group BMIs
underweight = 0
healthy = 0
overweight = 0
obese = 0
for pounds in bmis:
    if pounds <= 18.5:
      underweight += 1
    if pounds > 18.5 and pounds <= 24.9:
      healthy += 1
    if pounds > 24.9 and pounds <= 29.9:
      overweight += 1
    if pounds > 29.9:
      obese += 1

#Qualify average BMI
avg_bmi = round(sum(bmis) / len(bmis), 2)
quantifier = ""
if avg_bmi <= 18.5:
  quantifier =  "underweight"
if avg_bmi > 18.5 and avg_bmi <= 24.9:
  quantifier =  "healthy"
if avg_bmi > 24.9 and avg_bmi <= 29.9:
  quantifier =  "overweight"
if avg_bmi > 29.9:
  quantifier =  "obese"

#Number of smokers vs non-smokers
_puff = 0
_pass = 0
for puffer in nicotine:
  if puffer == 'yes':
    _puff += 1
  elif puffer == 'no':
    _pass += 1

#Samples by region
NE = 0
NW = 0
SE = 0
SW = 0
for area in regions:
  if area == 'northeast':
    NE +=1
  if area == 'northwest':
    NW += 1  
  if area == 'southeast':
    SE += 1
  if area == 'southwest':
    SW += 1
#average insurance cost
avg_cost = round(sum(costs) / len(costs), 2)

print("There are " + str(len(ages)) +  " people in this data sample.")
print("They range from " + str(min(ages)) + " to " + str(max(ages)) + " in age, with an average age of " + str(int(sum(ages) / len(ages))) + ".")
print("The sample polled " + str(women) + " women and " + str(men) + " men.")
print("The polled people are " + str(_puff) + " smokers and " + str(_pass) + " non-smokers.")
print("They have a BMI ranging from " + str(min(bmis)) + " to " + str(max(bmis)) + " with an average BMI of " + str(avg_bmi) + ", which is " + quantifier + ".")
print("The surveyed sample have anywhere from " + str(min(kids)) + " to " + str(max(kids)) + " children, with an average of " + str(round(sum(kids) / len(kids), 0)) + " children.")
print("The data sampled {} people from the northeast region, {} people from northwest, {} people from the southeast, and {} people from the southwest.".format(NE, NW, SE, SW))
print("The average cost of medical insurance is ${:,.2f}.".format(avg_cost))