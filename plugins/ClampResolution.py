# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named ClampResolutionExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from ClampResolutionExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.ClampResolution"

def getLabel():
    return "ClampResolution"

def getVersion():
    return 1

def getGrouping():
    return "videovina"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)

    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createInt2DParam("resolution", "Resolution")
    param.setMinimum(0, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10000, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(0, 1)
    param.setMaximum(10000, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(10000, 1)
    param.setDefaultValue(0, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1920, 0)
    param.setValue(1080, 1)
    lastNode.resolution = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output")
    lastNode.setPosition(1046, 379)
    lastNode.setSize(100, 29)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Input1")
    lastNode.setPosition(764, 82)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Crop1"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop1")
    lastNode.setLabel("Crop1")
    lastNode.setPosition(1316, 82)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupCrop1 = lastNode

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1920, 0)
        param.setValue(1080, 1)
        del param

    del lastNode
    # End of node "Crop1"

    # Start of node "Reformat1"
    lastNode = app.createNode("net.sf.openfx.Reformat", 1, group)
    lastNode.setScriptName("Reformat1")
    lastNode.setLabel("Reformat1")
    lastNode.setPosition(1316, 231)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupReformat1 = lastNode

    param = lastNode.getParam("useRoD")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("reformatType")
    if param is not None:
        param.set("scale")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("boxSize")
    if param is not None:
        param.setValue(960, 0)
        param.setValue(540, 1)
        del param

    param = lastNode.getParam("boxFixed")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Reformat1"

    # Start of node "Copy_RoD1"
    lastNode = app.createNode("fr.inria.built-in.Group", 1, group)
    lastNode.setScriptName("Copy_RoD1")
    lastNode.setLabel("Copy_RoD1")
    lastNode.setPosition(1046, 231)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupCopy_RoD1 = lastNode


    # Create the user parameters
    lastNode.custom = lastNode.createPageParam("custom", "Custom")
    param = lastNode.createBooleanParam("crop_format", "Crop Format")

    # Add the param to the page
    lastNode.custom.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(True)
    lastNode.crop_format = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['custom', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode
    # End of node "Copy_RoD1"

    groupgroup = groupCopy_RoD1
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = groupgroup
    lastNode.setColor(0.7, 0.7, 0.7)

    # Create the user parameters
    lastNode.custom = lastNode.createPageParam("custom", "Custom")
    param = lastNode.createBooleanParam("crop_format", "Crop Format")

    # Add the param to the page
    lastNode.custom.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(True)
    lastNode.crop_format = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['custom', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, groupgroup)
    lastNode.setLabel("Output")
    lastNode.setPosition(805, 302)
    lastNode.setSize(100, 29)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupgroupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "A"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, groupgroup)
    lastNode.setScriptName("A")
    lastNode.setLabel("A")
    lastNode.setPosition(1053, 75)
    lastNode.setSize(100, 29)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupgroupA = lastNode

    del lastNode
    # End of node "A"

    # Start of node "B"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, groupgroup)
    lastNode.setScriptName("B")
    lastNode.setLabel("B")
    lastNode.setPosition(805, 64)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupgroupB = lastNode

    del lastNode
    # End of node "B"

    # Start of node "Crop1"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, groupgroup)
    lastNode.setScriptName("Crop1")
    lastNode.setLabel("Crop1")
    lastNode.setPosition(805, 186)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupgroupCrop1 = lastNode

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("bottomLeft")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1920, 0)
        param.setValue(1080, 1)
        del param

    param = lastNode.getParam("intersect")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("blackOutside")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Crop1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupgroupOutput1.connectInput(0, groupgroupCrop1)
    groupgroupCrop1.connectInput(0, groupgroupB)

    param = groupgroupCrop1.getParam("bottomLeft")
    param.setExpression("a = thisGroup.getInput(0)\n\nx = 0\ny = 0\nif a:\n\tx = a.getRegionOfDefinition(frame, 1).x1\n\ty = a.getRegionOfDefinition(frame, 1).y1\n\nif dimension == 0:\n\tret = x\nelse:\n\tret = y", True, 0)
    param.setExpression("a = thisGroup.getInput(0)\n\nx = 0\ny = 0\nif a:\n\tx = a.getRegionOfDefinition(frame, 1).x1\n\ty = a.getRegionOfDefinition(frame, 1).y1\n\nif dimension == 0:\n\tret = x\nelse:\n\tret = y", True, 1)
    del param
    param = groupgroupCrop1.getParam("size")
    param.setExpression("a = thisGroup.getInput(0)\nb = thisGroup.getInput(0)\n\nx, y, w, h = 0,0,0,0\nif a:\n\tx = a.getRegionOfDefinition(frame, 1).x1\n\ty = a.getRegionOfDefinition(frame, 1).y1\n\tw = a.getRegionOfDefinition(frame, 1).x2\n\th = a.getRegionOfDefinition(frame, 1).y2\n\nif dimension == 0:\n\tret = w - x\nelse:\n\tret = h - y", True, 0)
    param.setExpression("a = thisGroup.getInput(0)\nb = thisGroup.getInput(0)\n\nx, y, w, h = 0,0,0,0\nif a:\n\tx = a.getRegionOfDefinition(frame, 1).x1\n\ty = a.getRegionOfDefinition(frame, 1).y1\n\tw = a.getRegionOfDefinition(frame, 1).x2\n\th = a.getRegionOfDefinition(frame, 1).y2\n\nif dimension == 0:\n\tret = w - x\nelse:\n\tret = h - y", True, 1)
    del param
    param = groupgroupCrop1.getParam("intersect")
    param.setExpression("thisGroup.crop_format.get()", False, 0)
    del param


    # Start of node "Crop_Default"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop_Default")
    lastNode.setLabel("Crop Default")
    lastNode.setPosition(764, 231)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupCrop_Default = lastNode

    param = lastNode.getParam("extent")
    if param is not None:
        param.set("default")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    del lastNode
    # End of node "Crop_Default"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupCopy_RoD1)
    groupCrop1.connectInput(0, groupInput1)
    groupReformat1.connectInput(0, groupCrop1)
    groupCopy_RoD1.connectInput(0, groupCrop_Default)
    groupCopy_RoD1.connectInput(1, groupReformat1)
    groupCrop_Default.connectInput(0, groupInput1)

    param = groupCrop1.getParam("size")
    param.setExpression("ret = thisGroup.resolution.getValue(dimension)", False, 0)
    param.setExpression("ret = thisGroup.resolution.getValue(dimension)", False, 1)
    del param

    try:
        extModule = sys.modules["ClampResolutionExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)