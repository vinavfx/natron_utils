# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named VinaRenderExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from VinaRenderExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.vinarender"

def getLabel():
    return "VinaRender"

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
        param.setValue("vinarender.main")
        del param


    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createBooleanParam("readfile", "Read Render")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.readfile = param
    del param

    param = lastNode.createBooleanParam("rgbonly", "RGB Only")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    param.setValue(True)
    lastNode.rgbonly = param
    del param

    param = lastNode.createBooleanParam("no_dialog", "No Show Message")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.no_dialog = param
    del param

    param = lastNode.createSeparatorParam("sep4", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep4 = param
    del param

    param = lastNode.createSeparatorParam("sep7", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep7 = param
    del param

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

    param = lastNode.createIntParam("instances", "Instances")
    param.setMinimum(1, 0)
    param.setMaximum(10, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 0)
    lastNode.instances = param
    del param

    param = lastNode.createIntParam("task_size", "Task Size")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    param.setValue(10, 0)
    lastNode.task_size = param
    del param

    param = lastNode.createSeparatorParam("sep8", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep8 = param
    del param

    param = lastNode.createOutputFileParam("filename", "Filename")
    param.setSequenceEnabled(False)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setValue("[Project]/../renders/video.mov")
    lastNode.filename = param
    del param

    param = lastNode.createDoubleParam("fps", "FPS")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    param.setValue(30, 0)
    lastNode.fps = param
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

    param = lastNode.createStringParam("one_project_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    ONE PROJECT :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.one_project_label = param
    del param

    param = lastNode.createInt2DParam("range", "Frame Range")
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    param.setValue(797, 1)
    lastNode.range = param
    del param

    param = lastNode.createButtonParam("project_frame_range", "Project Frame Range")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.project_frame_range = param
    del param

    param = lastNode.createBooleanParam("duplicate_project", "Duplicate Project")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("Duplica el proyecto y hace el renderizado sobre ese nuevo proyecto.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(True)
    lastNode.duplicate_project = param
    del param

    param = lastNode.createButtonParam("render", "Render")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.render = param
    del param

    param = lastNode.createSeparatorParam("sep5", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep5 = param
    del param

    param = lastNode.createSeparatorParam("sep6", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep6 = param
    del param

    param = lastNode.createStringParam("multi_project_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    MULTI PROJECT :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.multi_project_label = param
    del param

    param = lastNode.createPathParam("project_folder", "Project Folder")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setValue("[Project]/ntp")
    lastNode.project_folder = param
    del param

    param = lastNode.createStringParam("prefix", "NTP Prefix")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeDefault)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue("testing")
    lastNode.prefix = param
    del param

    param = lastNode.createButtonParam("multi_project_render", "Render")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.multi_project_render = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output")
    lastNode.setPosition(309, 156)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "reading"
    lastNode = app.createNode("fr.inria.built-in.Read", 1, group)
    lastNode.setScriptName("reading")
    lastNode.setLabel("reading")
    lastNode.setPosition(297, -197)
    lastNode.setSize(128, 78)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupreading = lastNode

    param = lastNode.getParam("decodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.ReadFFmpeg")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(video.mov)</Natron>")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("[Project]/../renders/video.mov")
        del param

    param = lastNode.getParam("firstFrame")
    if param is not None:
        param.setValue(30, 0)
        del param

    param = lastNode.getParam("before")
    if param is not None:
        param.set("black")
        del param

    param = lastNode.getParam("lastFrame")
    if param is not None:
        param.setValue(100, 0)
        del param

    param = lastNode.getParam("after")
    if param is not None:
        param.set("black")
        del param

    param = lastNode.getParam("outputPremult")
    if param is not None:
        param.set("opaque")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "reading"

    # Start of node "Switch1"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch1")
    lastNode.setLabel("Switch1")
    lastNode.setPosition(309, -34)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch1"

    # Start of node "to_rgb"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("to_rgb")
    lastNode.setLabel("to_rgb")
    lastNode.setPosition(-225, -34)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupto_rgb = lastNode

    param = lastNode.getParam("outputComponents")
    if param is not None:
        param.set("rgb")
        del param

    del lastNode
    # End of node "to_rgb"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(-18, -26)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(-63, -176)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupSwitch1)
    groupSwitch1.connectInput(0, groupDot1)
    groupSwitch1.connectInput(1, groupreading)
    groupto_rgb.connectInput(0, groupDot1)
    groupDot1.connectInput(0, groupSource)

    param = groupreading.getParam("filename")
    param.setExpression("thisGroup.filename.get()", False, 0)
    del param
    param = groupSwitch1.getParam("which")
    param.setExpression("thisGroup.readfile.get()", False, 0)
    del param

    try:
        extModule = sys.modules["VinaRenderExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
