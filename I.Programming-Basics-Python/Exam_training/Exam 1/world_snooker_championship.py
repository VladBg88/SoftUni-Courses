# total_sum > 4000 = - 25% + free trophy picture
# total_sum > 2500 = - 10%

STANDARD_FINAL = 110.10
STANDARD_SEMI_FINAL = 75.88
STANDARD_QUARTER_FINAL = 55.50
PREMIUM_FINAL = 160.66
PREMIUM_SEMI_FINAL = 125.22
PREMIUM_QUARTER_FINAL = 105.20
VIP_FINAL = 400
VIP_SEMI_FINAL = 300.40
VIP_QUARTER_FINAL = 118.90

stage = str(input())
ticket_type = str(input())
ticket_number = int(input())
trophy_picture = str(input())
total_sum = 0

if stage == "Final" and ticket_type == "Standard":
    total_sum = ticket_number * STANDARD_FINAL
elif stage == "Semi final" and ticket_type == "Standard":
    total_sum = ticket_number * STANDARD_SEMI_FINAL
elif stage == "Quarter final" and ticket_type == "Standard":
    total_sum = ticket_number * STANDARD_QUARTER_FINAL
elif stage == "Final" and ticket_type == "Premium":
    total_sum = ticket_number * PREMIUM_FINAL
elif stage == "Semi final" and ticket_type == "Premium":
    total_sum = ticket_number * PREMIUM_SEMI_FINAL
elif stage == "Quarter final" and ticket_type == "Premium":
    total_sum = ticket_number * PREMIUM_QUARTER_FINAL
elif stage == "Final" and ticket_type == "VIP":
    total_sum = ticket_number * VIP_FINAL
elif stage == "Semi final" and ticket_type == "VIP":
    total_sum = ticket_number * VIP_SEMI_FINAL
elif stage == "Quarter final" and ticket_type == "VIP":
    total_sum = ticket_number * VIP_QUARTER_FINAL

if total_sum > 4000:
    total_sum -= total_sum * 0.25
    if trophy_picture == "Y":
        total_sum -= ticket_number * 40
elif total_sum > 2500:
    total_sum -= total_sum * 0.1

if trophy_picture == "Y":
    total_sum += ticket_number * 40

print(f"{total_sum:.2f}")
