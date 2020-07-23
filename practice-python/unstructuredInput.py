# Objective
# Take unstructured input from a user, and turn it into structured data that is ready for an application to work on.

# We're not interested in higher level design for this question, so don't spend extra time on data models.

# Write a function that given an array structured like:

# [
#   [
#     "1",
#     "Gregory Gwilliam",
#     "2"
#   ],
#   [
#     "2",
#     "Brice Martin",
#     ""
#   ]
# ]
 

# will return structured JSON like:

# [{"id":1,"name":"Gregory Gwilliam","manager_id":2},{"id":2,"name": "Brice Martin","manager_id":null}]
#  For readability, here is that same output pretty printed.

# [
#   {
#     "id": 1,
#     "name": "Gregory Gwilliam",
#     "manager_id": 2
#   },
#   {
#     "id": 2,
#     "name": "Brice Martin",
#     "manager_id": null
#   }
# ]

# NOTE:
# Do not pretty print the JSON. 
# Use whatever tools for generating JSON exist in your preferred language.
# manager_id is the only nullable field.

# Language Notes:
# Python's default json generation tool includes spaces in the output, but has parameters that allow you to output the json without spaces.





import json

data = [ 
  [
    "1",
    "Gregory Gwilliam",
    "2"
  ],
  [
    "2",
    "Brice Martin",
    ""
  ]
]

list = [{"id": x[0], "name": x[1], "manager_ID": x[2]} for x in data]

json.dumps(list)

print(list)
  