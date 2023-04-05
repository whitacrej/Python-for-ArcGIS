class ToolValidator:
  # Class to add custom behavior and properties to the tool and tool parameters.

    def __init__(self):
        # set self.params for use in other function
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        # Customize parameter properties. 
        # This gets called when the tool is opened.

        # Disable the optional alias parameter
        self.params[3].enabled = False

        return

    def updateParameters(self):
        # Modify parameter values and properties.
        # This gets called each time a parameter is modified, before 
        # standard validation.
        
        # Check if the parameters have a value and have been validated
        if self.params[0].value and not self.params[0].hasBeenValidated:
            try:
                # Create a describe object for 'Input Table'
                desc = arcpy.Describe(self.params[0].value)

                # Check if 'Input Table' contains aliases, and if so enable Add Field Aliases to CSV Table (optional)' parameter
                aliases = [field.aliasName for field in desc.fields if field.aliasName != field.name]
                if aliases:
                    self.params[3].enabled = True
                else:
                    self.params[3].enabled = False

            except:
                pass

        return

    def updateMessages(self):
        # Customize messages for the parameters.
        # This gets called after standard validation.
        return

    # def isLicensed(self):
    #     # set tool isLicensed.
    # return True

    # def postExecute(self):
    #     # This method takes place after outputs are processed and
    #     # added to the display.
    # return
