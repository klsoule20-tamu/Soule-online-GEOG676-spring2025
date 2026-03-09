#Kaleb Soule Lab 05 Toolbox

import arcpy

class Toolbox(object):
    """Define the toolbox (the name of the toolbox is the name of the .pyt file)"""
    self.label = "Toolbox"
    self.alias = ""

    #list of tool classes associated with this toolbox 
    self.tools = [GarageBuildingIntersection]


class GarageBuildingIntersection(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)"""
        self.label = "Lab5 Toolbox"
        self.description = "Determines which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False #Only used in ArcMap
        self.category = "Building Tools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        