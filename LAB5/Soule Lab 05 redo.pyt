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
        param0 = arcpy.Parameter(
            displayName="GDB Folder",
            name="GDBFolder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )
        param1 = arcpy.Parameter(
            displayName="GDB Name",
            name="GDBName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param2 = arcpy.Parameter(
            displayName="Garage CSV File",
            name="GarageCSVFile",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        param3 = arcpy.Parameter(
            displayName="Garage Layer Name",
            name="GarageLayerName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param4 = arcpy.Parameter(
            displayName="CampusGDB",
            name="CampusGDB",
            datatype="DEType",
            parameterType="Required",
            direction="Input"
        )
        param5 = arcpy.Parameter(
            displayName="Buffer Distance",
            name="BufferDistance",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3, param4, param5]
        return params
    
    def isLicensed(self):
        """Set whether tool is licensed to execute"""
        return True
    
    def updateParameters(self, parameters):
        """"""
        