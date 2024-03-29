# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named SlideBaseExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from SlideBaseExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.SlideBase"

def getLabel():
    return "SlideBase"

def getVersion():
    return 1

def getIconPath():
    return "Slide.png"

def getGrouping():
    return "videovina/Slides"

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
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.state_label = param
    del param

    param = lastNode.createChoiceParam("format", "Format")
    param.setDefaultValue(2)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.format = param
    del param

    param = lastNode.createChoiceParam("speed", "Speed")
    param.setDefaultValue(1)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.speed = param
    del param

    param = lastNode.createButtonParam("clean", "Clean")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.clean = param
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

    param = lastNode.createIntParam("input_amount", "Extra Pictures Inputs")
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
    lastNode.input_amount = param
    del param

    param = lastNode.createButtonParam("generate_inputs", "Generate")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.generate_inputs = param
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

    param = lastNode.createStringParam("text_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    TEXT :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.text_label = param
    del param

    param = lastNode.createBooleanParam("include_text", "Include Texts")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.include_text = param
    del param

    param = lastNode.createFileParam("font", "Font")
    param.setSequenceEnabled(False)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.font = param
    del param

    param = lastNode.createStringParam("title", "Title")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeDefault)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.title = param
    del param

    param = lastNode.createStringParam("subtitle", "Subtitle")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeDefault)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(True)
    lastNode.subtitle = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
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

    del lastNode
    # End of node "TimeOffset"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(1567, 453)
    lastNode.setSize(104, 45)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    del lastNode
    # End of node "Merge1"

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

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(1567, 561)
    lastNode.setSize(104, 45)
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
    lastNode.setPosition(1992, 576)
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

    # Start of node "Constant1"
    lastNode = app.createNode("net.sf.openfx.ConstantPlugin", 1, group)
    lastNode.setScriptName("Constant1")
    lastNode.setLabel("Constant1")
    lastNode.setPosition(1947, 198)
    lastNode.setSize(104, 30)
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
    lastNode.setSize(104, 30)
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

    # Start of node "TwelveRender"
    lastNode = app.createNode("vv.TwelveRender", 1, group)
    lastNode.setScriptName("TwelveRender")
    lastNode.setLabel("TwelveRender")
    lastNode.setPosition(1210, 229)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupTwelveRender = lastNode

    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("twelve_render.main")
        del param


    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createStringParam("state_label", "State")
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
    param.setEnabled(False, 0)
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
    param.setEnabled(False, 0)
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
    param.setEnabled(False, 0)
    lastNode.speed = param
    del param

    param = lastNode.createButtonParam("link", "Link To Parent")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.link = param
    del param

    param = lastNode.createButtonParam("link_to_connected", "Link To Connected")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("Vincula todos los nodos conectados que tengan,\nlos atributos de videovina.")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.link_to_connected = param
    del param

    param = lastNode.createSeparatorParam("sep5", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    param.setEnabled(False, 0)
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
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(150, 0)
    param.setValue(100, 1)
    param.setValue(50, 2)
    param.setEnabled(False, 0)
    param.setEnabled(False, 1)
    param.setEnabled(False, 2)
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
    param.setEnabled(False, 0)
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

    param = lastNode.createChoiceParam("sequence_type", "Sequence Type")
    entries = [ ("PNG", ""),
    ("JPG", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.set("JPG")
    lastNode.sequence_type = param
    del param

    param = lastNode.createChoiceParam("filter", "Reformat Filter")
    entries = [ ("Cubic", ""),
    ("Impulse", ""),
    ("Notch", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.filter = param
    del param

    param = lastNode.createStringParam("prefix", "Prefix")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeDefault)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue("slide_01")
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

    param = lastNode.createBooleanParam("current_speed", "Current Speed")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("Renderiza solo una velocidad con los 3 formatos.")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.current_speed = param
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

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode
    # End of node "TwelveRender"

    # Start of node "TwelveRead"
    lastNode = app.createNode("vv.TwelveRead", 1, group)
    lastNode.setScriptName("TwelveRead")
    lastNode.setLabel("TwelveRead")
    lastNode.setPosition(1210, 359)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupTwelveRead = lastNode

    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("twelve_read.main")
        del param


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
    param.setEnabled(False, 0)
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
    param.setEnabled(False, 0)
    lastNode.speed = param
    del param

    param = lastNode.createButtonParam("link", "Link To Parent")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.link = param
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

    param = lastNode.createChoiceParam("sequence_type", "Sequence Type")
    entries = [ ("PNG", ""),
    ("JPG", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.set("JPG")
    param.setEnabled(False, 0)
    lastNode.sequence_type = param
    del param

    param = lastNode.createStringParam("prefix", "Prefix")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeDefault)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue("slide_01")
    param.setEnabled(False, 0)
    lastNode.prefix = param
    del param

    param = lastNode.createChoiceParam("before", "Before")
    entries = [ ("Hold", ""),
    ("Loop", ""),
    ("Bounce", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.before = param
    del param

    param = lastNode.createChoiceParam("after", "After")
    entries = [ ("Hold", ""),
    ("Loop", ""),
    ("Bounce", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.after = param
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

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode
    # End of node "TwelveRead"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupFrameRange)
    groupFrameRange.connectInput(0, groupTimeOffset)
    groupTimeOffset.connectInput(0, groupMerge2)
    groupMerge1.connectInput(0, groupImage)
    groupMerge1.connectInput(1, groupDot1)
    groupDot1.connectInput(0, groupTwelveRead)
    groupMerge2.connectInput(0, groupMerge1)
    groupMerge2.connectInput(1, groupDot2)
    groupDot2.connectInput(0, groupTransform)
    groupTransform.connectInput(0, groupConstant1)
    groupTwelveRender.connectInput(0, groupDot4)

    param = groupMerge2.getParam("mix")
    param.setExpression("thisGroup.include_text.get()", False, 0)
    del param
    param = groupTwelveRender.getParam("state_label")
    group.getParam("state_label").setAsAlias(param)
    del param
    param = groupTwelveRender.getParam("format")
    group.getParam("format").setAsAlias(param)
    del param
    param = groupTwelveRender.getParam("speed")
    group.getParam("speed").setAsAlias(param)
    del param
    param = groupTwelveRender.getParam("sep5")
    group.getParam("sep5").setAsAlias(param)
    del param
    param = groupTwelveRender.getParam("durations")
    group.getParam("durations").setAsAlias(param)
    del param
    param = groupTwelveRender.getParam("sep6")
    group.getParam("sep6").setAsAlias(param)
    del param
    param = groupTwelveRead.getParam("format")
    group.getParam("format").setAsAlias(param)
    del param
    param = groupTwelveRead.getParam("speed")
    group.getParam("speed").setAsAlias(param)
    del param
    param = groupTwelveRead.getParam("sequence_type")
    param.slaveTo(groupTwelveRender.getParam("sequence_type"), 0, 0)
    del param
    param = groupTwelveRead.getParam("prefix")
    param.slaveTo(groupTwelveRender.getParam("prefix"), 0, 0)
    del param

    try:
        extModule = sys.modules["SlideBaseExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
