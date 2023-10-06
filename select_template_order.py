import re

import re

# Your list of strings
string_list = ["TEMPLATE_TTREL", "TEMPLATE_UUREL", "TEMPLATE_SSREL", "TEMPLATE_MR1_RRREL", "TEMPLATE_MR2_RRREL", "TEMPLATE_MR20123_SSREL", "TEMPLATE_UTAH", "TEMPLATE_MR1213123_UUREL"]

# Filter strings that end with {alphabet letter repeated twice}REL
filtered_list = [s for s in string_list if re.match(r'TEMPLATE_.*[A-Z]{2}REL', s)]

print(sorted(filtered_list))

# Sort the filtered list based on "TEMPLATE_MR" and the following number
filtered_list.sort(key=lambda s: (re.search(r'TEMPLATE_MR(\d+)_', s).group(1) if re.search(r'TEMPLATE_MR(\d+)_', s) else '', s))


# Select the most recent one
if filtered_list:
    most_recent = filtered_list[-1]
    print(most_recent)
else:
    print("No matching strings found.")

