parent_name = input("Enter the parent member's name: ")
has_child = input("Does the parent member have child members? (Y/N): ")
scheme_amount = 5000
parent_commission_rate = 0.10
child_commission_rate = 0.05
if has_child == 'Y':
    child_names = input("Enter names of child members separated by commas: ")