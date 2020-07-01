# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named ShadowExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from ShadowExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.DropShadow"

def getLabel():
    return "Shadow"

def getVersion():
    return 1

def getIconPath():
    return "DropShadow.png"

def getGrouping():
    return "videovina/Filter"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)

    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createChoiceParam("format", "Format")
    entries = [ ("Quarter HD - 480 x 270", ""),
    ("Half HD - 960 x 540", ""),
    ("Full HD - 1920 x 1080", ""),
    ("4K - 3840 x 2160", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("Full HD - 1920 x 1080")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.format = param
    del param

    param = lastNode.createDoubleParam("angle", "Angle")
    param.setMinimum(0, 0)
    param.setMaximum(360, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(360, 0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(90, 0)
    lastNode.angle = param
    del param

    param = lastNode.createIntParam("distance", "Distance")
    param.setMinimum(0, 0)
    param.setMaximum(100, 0)
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
    lastNode.distance = param
    del param

    param = lastNode.createDoubleParam("opacity", "Opacity")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.5, 0)
    lastNode.opacity = param
    del param

    param = lastNode.createIntParam("blur", "Blur")
    param.setMinimum(0, 0)
    param.setMaximum(100, 0)
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
    param.setValue(1, 0)
    lastNode.blur = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output")
    lastNode.setPosition(764, 444)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(764, 138)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(1093, 137)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("0")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("0")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("0")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(764, 345)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("under")
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(0.5, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Transform1"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform1")
    lastNode.setLabel("Transform1")
    lastNode.setPosition(1093, 192)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupTransform1 = lastNode

    param = lastNode.getParam("translate")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("rotate")
    if param is not None:
        param.setValue(90, 0)
        del param

    param = lastNode.getParam("black_outside")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Transform1"

    # Start of node "Transform2"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform2")
    lastNode.setLabel("Transform2")
    lastNode.setPosition(1093, 252)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupTransform2 = lastNode

    param = lastNode.getParam("rotate")
    if param is not None:
        param.setValue(-90, 0)
        del param

    param = lastNode.getParam("black_outside")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Transform2"

    # Start of node "Crop1"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop1")
    lastNode.setLabel("Crop1")
    lastNode.setPosition(1093, 298)
    lastNode.setSize(104, 32)
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

    # Start of node "Blur1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur1")
    lastNode.setLabel("Blur1")
    lastNode.setPosition(1093, 356)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        del param

    del lastNode
    # End of node "Blur1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupMerge1)
    groupShuffle1.connectInput(0, groupSource)
    groupMerge1.connectInput(0, groupSource)
    groupMerge1.connectInput(1, groupBlur1)
    groupTransform1.connectInput(0, groupShuffle1)
    groupTransform2.connectInput(0, groupTransform1)
    groupCrop1.connectInput(0, groupTransform2)
    groupBlur1.connectInput(0, groupCrop1)

    param = groupMerge1.getParam("mix")
    param.setExpression("thisGroup.opacity.get()", False, 0)
    del param
    param = groupTransform1.getParam("translate")
    param.setExpression("format = thisGroup.format.get()\nret = thisGroup.distance.get() * general.rscale[format]", True, 0)
    del param
    param = groupTransform1.getParam("rotate")
    param.setExpression("thisGroup.angle.get()", False, 0)
    del param
    param = groupTransform2.getParam("rotate")
    param.setExpression("-thisGroup.angle.get()", False, 0)
    del param
    param = groupCrop1.getParam("size")
    param.setExpression("format_index = thisGroup.format.get()\nformat = general.formats[format_index]\n\nif dimension == 0:\n\tret = format[0]\nelse:\n\tret = format[1]", True, 0)
    param.setExpression("format_index = thisGroup.format.get()\nformat = general.formats[format_index]\n\nif dimension == 0:\n\tret = format[0]\nelse:\n\tret = format[1]", True, 1)
    del param
    param = groupBlur1.getParam("size")
    param.setExpression("format = thisGroup.format.get()\nret = thisGroup.blur.get()  * general.rscale[format]", True, 0)
    param.setExpression("format = thisGroup.format.get()\nret = thisGroup.blur.get()  * general.rscale[format]", True, 1)
    del param

    try:
        extModule = sys.modules["ShadowExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
