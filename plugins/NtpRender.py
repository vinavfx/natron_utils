# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named NtpRenderExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from NtpRenderExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.NtpRender"

def getLabel():
    return "NtpRender"

def getVersion():
    return 1

def getIconPath():
    return "VinaRender.png"

def getGrouping():
    return "videovina/Render"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)
    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("ntp_render.main")
        del param


    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createStringParam("job_name", "Job Name")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeDefault)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.job_name = param
    del param

    param = lastNode.createIntParam("instances", "Servers Instances")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(2, 0)
    lastNode.instances = param
    del param

    param = lastNode.createSeparatorParam("sep1", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep1 = param
    del param

    param = lastNode.createStringParam("base_slide", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    BASE :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.base_slide = param
    del param

    param = lastNode.createIntParam("slides_count", "Slides Count")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(10, 0)
    lastNode.slides_count = param
    del param

    param = lastNode.createIntParam("slides_by_project", "Slides By Project")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(3, 0)
    lastNode.slides_by_project = param
    del param

    param = lastNode.createPathParam("output_folder", "Output Folder")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setValue("[Project]/ntp")
    lastNode.output_folder = param
    del param

    param = lastNode.createButtonParam("send", "Send To VinaRender")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.send = param
    del param

    param = lastNode.createSeparatorParam("sep2", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep2 = param
    del param

    param = lastNode.createSeparatorParam("sep3", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep3 = param
    del param

    param = lastNode.createStringParam("production_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    PRODUCTION :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.production_label = param
    del param

    param = lastNode.createIntParam("slide_amount", "Slides Amount")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(100, 0)
    lastNode.slide_amount = param
    del param

    param = lastNode.createPathParam("output_production_folder", "Output Folder")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setValue("[Project]")
    lastNode.output_production_folder = param
    del param

    param = lastNode.createButtonParam("send_as_production", "Send To VinaRender")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.send_as_production = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output")
    lastNode.setPosition(764, 294)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(764, 194)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupSource)

    try:
        extModule = sys.modules["NtpRenderExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
