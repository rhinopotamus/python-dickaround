import xml.etree.ElementTree as ET

# figure out what time it is
from datetime import datetime, timezone
nowstr = datetime.now(timezone.utc).strftime("%m/%d/%Y at %I:%M UTC")

# find all the .ptx files in the current directory
import glob
for ptx in glob.glob("*.ptx"):
    # start making the def file
    # these seem to be the only set info that are strictly required
    buffer = []
    buffer.append("assignmentType = default")
    buffer.append("openDate = " + nowstr)
    buffer.append("dueDate = " + nowstr)
    buffer.append("answerDate = " + nowstr)

    buffer.append("problemListV2")
    # read the supplied ptx file (basically xml)
    tree = ET.parse(ptx)
    root = tree.getroot()
    # find the webwork elements
    webworks = root.iter('webwork')
    # check if there's no webworks
    if all(webworks):
        break
    for webwork in webworks:
        buffer.append("problem_start")
        buffer.append("source_file = " + webwork.get("source"))
        buffer.append("problem_end")
    # filename of def file matches ptx file
    outfile = ptx[:-3]+"def"
    f = open(outfile, 'w')
    f.writelines("\n".join(buffer))
    f.close()
    buffer.clear()

print("Please remember to rename your .def files starting with 'set'!")