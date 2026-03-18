#Kaleb Soule Lab 04 Resubmittal

#Create a gdb and garage features

import arcpy

arcpy.env.workspace = r"C:\Users\klsoule20\Documents\GitHub\Soule-online-GEOG676-spring2025\LAB4\codes_env"
folder_path = r"C:\Users\klsoule20\Documents\GitHub\Soule-online-GEOG676-spring2025\LAB4"
gdb_name = 'ResubmittalTest.gdb'
gdb_path = folder_path + '\\' +gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r"C:\Users\klsoule20\Documents\GitHub\Soule-online-GEOG676-spring2025\LAB4\garages.csv"
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

#open campud gdb, copy building feature to our gdb
campus = r"C:\Users\klsoule20\Documents\GitHub\Soule-online-GEOG676-spring2025\LAB4\Campus.gdb"
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

#Re-Projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

#Buffer the Garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

#Intersect our Buffer with the Buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\\Garage_Building_Intersection.dbf', r"C:\Users\klsoule20\Documents\GitHub\Soule-online-GEOG676-spring2025\LAB4", 'nearbyBuildings.csv')
