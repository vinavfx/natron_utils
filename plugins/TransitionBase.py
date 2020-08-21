# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named TransitionBaseExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from TransitionBaseExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.TransitionBase"

def getLabel():
    return "TransitionBase"

def getVersion():
    return 1

def getIconPath():
    return "Transition.png"

def getGrouping():
    return "videovina/Transitions"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)
    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("slide_base.main")
        del param


    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createStringParam("state_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    STATE :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.state_label = param
    del param

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

    param = lastNode.createChoiceParam("speed", "Speed")
    entries = [ ("Slow", ""),
    ("Normal", ""),
    ("Fast", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("Normal")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.speed = param
    del param

    param = lastNode.createButtonParam("refresh", "Refresh")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.refresh = param
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

    param = lastNode.createStringParam("time_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    TIME :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.time_label = param
    del param

    param = lastNode.createIntParam("start_frame", "Start Frame")
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
    lastNode.start_frame = param
    del param

    param = lastNode.createInt3DParam("durations", "Durations")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)
    param.setDefaultValue(0, 1)
    param.restoreDefaultValue(1)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(100, 2)
    param.setDefaultValue(0, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    param.setValue(150, 0)
    param.setValue(100, 1)
    param.setValue(50, 2)
    lastNode.durations = param
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

    param = lastNode.createStringParam("settings_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    SETTINGS :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.settings_label = param
    del param

    param = lastNode.createColorParam("color", "Color", False)
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1, 1)
    param.setMinimum(-2147483648, 2)
    param.setMaximum(2147483647, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(1, 2)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.color = param
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

    param = lastNode.createStringParam("prerender_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    PRE-RENDER :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.prerender_label = param
    del param

    param = lastNode.createIntParam("seed", "Random Seed")
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
    lastNode.seed = param
    del param

    param = lastNode.createDoubleParam("motion_blur", "Motion Blur")
    param.setMinimum(0, 0)
    param.setMaximum(4, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(4, 0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.motion_blur = param
    del param

    param = lastNode.createStringParam("prefix", "Prefix")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeDefault)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.prefix = param
    del param

    param = lastNode.createBooleanParam("current_state", "Current State")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.current_state = param
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

    lastNode.exp = lastNode.createPageParam("exp", "Exp")
    param = lastNode.createInt2DParam("current_format", "Current Format")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)
    param.setDefaultValue(0, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.exp.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1920, 0)
    param.setValue(1080, 1)
    lastNode.current_format = param
    del param

    param = lastNode.createIntParam("duration", "Current Duration")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.exp.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(100, 0)
    lastNode.duration = param
    del param

    param = lastNode.createDoubleParam("rscale", "Rscale")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)

    # Add the param to the page
    lastNode.exp.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 0)
    lastNode.rscale = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'exp', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output_2")
    lastNode.setPosition(1567, 822)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Image"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Image")
    lastNode.setLabel("Image")
    lastNode.setPosition(1567, -250)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupImage = lastNode

    del lastNode
    # End of node "Image"

    # Start of node "FrameRange"
    lastNode = app.createNode("net.sf.openfx.FrameRange", 1, group)
    lastNode.setScriptName("FrameRange")
    lastNode.setLabel("FrameRange")
    lastNode.setPosition(1567, 739)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupFrameRange = lastNode

    param = lastNode.getParam("frameRange")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(100, 1)
        del param

    param = lastNode.getParam("before")
    if param is not None:
        param.set("hold")
        del param

    param = lastNode.getParam("after")
    if param is not None:
        param.set("hold")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(1 - 1)</Natron>")
        del param

    del lastNode
    # End of node "FrameRange"

    # Start of node "TimeOffset"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("TimeOffset")
    lastNode.setLabel("TimeOffset")
    lastNode.setPosition(1567, 664)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupTimeOffset = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "TimeOffset"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(1567, 448)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "FX"
    lastNode = app.createNode("fr.inria.built-in.Group", 1, group)
    lastNode.setScriptName("FX")
    lastNode.setLabel("FX")
    lastNode.setPosition(1210, 213)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupFX = lastNode

    del lastNode
    # End of node "FX"

    groupgroup = groupFX
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = groupgroup
    lastNode.setColor(0.7, 0.7, 0.7)
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, groupgroup)
    lastNode.setLabel("Output")
    lastNode.setPosition(1180, 609)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupgroupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, groupgroup)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Input1")
    lastNode.setPosition(1180, 509)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupgroupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupgroupOutput1.connectInput(0, groupgroupInput1)


    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(1255, 468)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Backdrop1"
    lastNode = app.createNode("fr.inria.built-in.BackDrop", 1, group)
    lastNode.setScriptName("Backdrop1")
    lastNode.setLabel("Backdrop1")
    lastNode.setPosition(1049, 127)
    lastNode.setSize(317, 268)
    lastNode.setColor(0.45, 0.45, 0.45)
    groupBackdrop1 = lastNode

    param = lastNode.getParam("Label")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">Efectos, formas y otros que no necesitan la imagen de entrada</font>")
        del param

    del lastNode
    # End of node "Backdrop1"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(1567, 561)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    del lastNode
    # End of node "Merge2"

    # Start of node "Backdrop2"
    lastNode = app.createNode("fr.inria.built-in.BackDrop", 1, group)
    lastNode.setScriptName("Backdrop2")
    lastNode.setLabel("Backdrop2")
    lastNode.setPosition(1830, 111)
    lastNode.setSize(329, 302)
    lastNode.setColor(0.45, 0.45, 0.45)
    groupBackdrop2 = lastNode

    param = lastNode.getParam("Label")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">Textos</font>")
        del param

    del lastNode
    # End of node "Backdrop2"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(1990, 581)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(1255, -34)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(1612, -34)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Constant1"
    lastNode = app.createNode("net.sf.openfx.ConstantPlugin", 1, group)
    lastNode.setScriptName("Constant1")
    lastNode.setLabel("Constant1")
    lastNode.setPosition(1947, 198)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupConstant1 = lastNode

    param = lastNode.getParam("extent")
    if param is not None:
        param.set("size")
        del param

    param = lastNode.getParam("reformat")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("color")
    if param is not None:
        param.setValue(0.5, 0)
        param.setValue(0.5, 1)
        param.setValue(1, 2)
        param.setValue(1, 3)
        del param

    del lastNode
    # End of node "Constant1"

    # Start of node "Transform"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform")
    lastNode.setLabel("Transform")
    lastNode.setPosition(1947, 262)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupTransform = lastNode

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(0.5, 0)
        param.setValue(0.5, 1)
        del param

    param = lastNode.getParam("transformCenterChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Transform"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupFrameRange)
    groupFrameRange.connectInput(0, groupTimeOffset)
    groupTimeOffset.connectInput(0, groupMerge2)
    groupMerge1.connectInput(0, groupDot5)
    groupMerge1.connectInput(1, groupDot1)
    groupFX.connectInput(0, groupDot4)
    groupDot1.connectInput(0, groupFX)
    groupMerge2.connectInput(0, groupMerge1)
    groupMerge2.connectInput(1, groupDot2)
    groupDot2.connectInput(0, groupTransform)
    groupDot4.connectInput(0, groupDot5)
    groupDot5.connectInput(0, groupImage)
    groupTransform.connectInput(0, groupConstant1)

    param = groupFrameRange.getParam("frameRange")
    param.setExpression("start_frame = thisGroup.start_frame.get()\nduration = thisGroup.duration.get()\nrange = [start_frame, start_frame + duration]\n\nret = range[dimension]\n\n", True, 0)
    param.setExpression("start_frame = thisGroup.start_frame.get()\nduration = thisGroup.duration.get()\nrange = [start_frame, start_frame + duration]\n\nret = range[dimension]\n\n", True, 1)
    del param
    param = groupTimeOffset.getParam("timeOffset")
    param.setExpression("thisGroup.start_frame.get()", False, 0)
    del param
    param = groupMerge2.getParam("mix")
    param.setExpression("thisGroup.include_text.get()", False, 0)
    del param

    param = group.getParam("current_format")
    param.setExpression("index = thisNode.format.get()\nret = general.formats[index][dimension]", True, 0)
    param.setExpression("index = thisNode.format.get()\nret = general.formats[index][dimension]", True, 1)
    del param
    param = group.getParam("duration")
    param.setExpression("index = thisNode.speed.get()\nret = thisNode.durations.get()[index]", True, 0)
    del param
    param = group.getParam("rscale")
    param.setExpression("index = thisNode.format.get()\nret = general.rscale[index]", True, 0)
    del param
    try:
        extModule = sys.modules["TransitionBaseExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
