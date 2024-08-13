# read a ptx file (which is basically xml)
# grab out anything that looks like <webwork source="..." />
import xml.etree.ElementTree as ET
tree = ET.parse("S-mv-fns-functions.ptx")
root = tree.getroot()
exercises = tree.find("exercises")
print(exercises)
for webwork in exercises.iterfind("webwork"):
    print("hi")
    source = webwork.get("source")
    print(webwork)

# write out like this:
# assignmentType      = default
# openDate          = 08/20/2024 at 11:59pm MDT
# reducedScoringDate = 12/31/1969 at 05:00pm MST
# dueDate           = 08/27/2024 at 11:59pm MDT
# answerDate        = 08/29/2024 at 11:59pm MDT
# enableReducedScoring = N
# paperHeaderFile   = defaultHeader
# screenHeaderFile  = defaultHeader
# description       = 
# restrictProbProgression = 0
# emailInstructor   = 0

# problemListV2
# problem_start
# problem_id = 1 <- this is a counter
# source_file = Library/WHFreeman/Rogawski_Calculus_Early_Transcendentals_Second_Edition/14_Differentiation_in_Several_Variables/14.1_Functions_of_Two_or_More_Variables/14.1.1.pg
# value = 1
# max_attempts = -1
# showMeAnother = -1
# prPeriod = -1
# counts_parent_grade = 0
# att_to_open_children = 0 
# problem_end