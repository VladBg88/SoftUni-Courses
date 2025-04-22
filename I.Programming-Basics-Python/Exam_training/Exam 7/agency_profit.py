company_name = str(input())
number_tickets = int(input())
children_tickets = int(input())
regular_price_ticket = float(input())
tax_service = float(input())

price_children_ticket = regular_price_ticket * 0.3 + tax_service
regular_price_ticket += tax_service
all_tickets_total_sum = number_tickets * regular_price_ticket + children_tickets * price_children_ticket
earning = all_tickets_total_sum * 0.2

print(f'The profit of your agency from {company_name} tickets is {earning:.2f} lv.')
