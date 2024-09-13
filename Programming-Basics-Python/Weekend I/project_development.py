#Напишете програма, която изчислява колко часа ще са необходими на един архитект,
# за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.
#"The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."

architect_name = input()
projects = int(input())

total_time = projects * 3

print(f'The architect {architect_name} will need {total_time} hours to complete {projects} project/s.')