# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named LoopDissolveExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from LoopDissolveExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.LoopDissolve"

def getLabel():
    return "LoopDissolve"

def getVersion():
    return 1

def getIconPath():
    return "LoopDissolve.png"

def getGrouping():
    return "videovina/Time"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)
    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("loop_dissolve.main")
        del param


    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createButtonParam("refresh", "Refresh")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    lastNode.refresh = param
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

    param = lastNode.createIntParam("input_frames", "Input Frames")
    param.setMinimum(10, 0)
    param.setDisplayMinimum(10, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(100, 0)
    lastNode.input_frames = param
    del param

    param = lastNode.createIntParam("output_frames", "Output Frames")
    param.setMinimum(10, 0)
    param.setDisplayMinimum(10, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(500, 0)
    lastNode.output_frames = param
    del param

    param = lastNode.createIntParam("transition_duration", "Transition Duration")
    param.setMinimum(1, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(30, 0)
    lastNode.transition_duration = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output")
    lastNode.setPosition(746, 1163)
    lastNode.setSize(100, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Image"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Image")
    lastNode.setLabel("Image")
    lastNode.setPosition(2064, -569)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupImage = lastNode

    del lastNode
    # End of node "Image"

    # Start of node "offset_b"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("offset_b")
    lastNode.setLabel("offset_b")
    lastNode.setPosition(921, -426)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupoffset_b = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(20, 0)
        del param

    del lastNode
    # End of node "offset_b"

    # Start of node "offset_a"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("offset_a")
    lastNode.setLabel("offset_a")
    lastNode.setPosition(613, -433)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupoffset_a = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(-50, 0)
        del param

    del lastNode
    # End of node "offset_a"

    # Start of node "dissolve"
    lastNode = app.createNode("net.sf.openfx.DissolvePlugin", 1, group)
    lastNode.setScriptName("dissolve")
    lastNode.setLabel("dissolve")
    lastNode.setPosition(763, -280)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupdissolve = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValueAtTime(0, 20, 0)
        param.setValueAtTime(1, 50, 0)
        del param

    del lastNode
    # End of node "dissolve"

    # Start of node "frame_range"
    lastNode = app.createNode("net.sf.openfx.FrameRange", 1, group)
    lastNode.setScriptName("frame_range")
    lastNode.setLabel("frame_range")
    lastNode.setPosition(763, -159)
    lastNode.setSize(100, 50)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupframe_range = lastNode

    param = lastNode.getParam("frameRange")
    if param is not None:
        param.setValue(70, 1)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(1 - 70)</Natron>")
        del param

    del lastNode
    # End of node "frame_range"

    # Start of node "output_switch"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("output_switch")
    lastNode.setLabel("output_switch")
    lastNode.setPosition(763, 514)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupoutput_switch = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValueAtTime(0, 1, 0)
        param.setValueAtTime(1, 71, 0)
        param.setValueAtTime(2, 141, 0)
        param.setValueAtTime(3, 211, 0)
        param.setValueAtTime(4, 281, 0)
        param.setValueAtTime(5, 351, 0)
        param.setValueAtTime(6, 421, 0)
        param.setValueAtTime(7, 491, 0)
        param.setValueAtTime(8, 561, 0)
        del param

    del lastNode
    # End of node "output_switch"

    # Start of node "offset_a2"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("offset_a2")
    lastNode.setLabel("offset_a2")
    lastNode.setPosition(503, 773)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupoffset_a2 = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(-265, 0)
        del param

    del lastNode
    # End of node "offset_a2"

    # Start of node "offset_b2"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("offset_b2")
    lastNode.setLabel("offset_b2")
    lastNode.setPosition(946, 758)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupoffset_b2 = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(235, 0)
        del param

    del lastNode
    # End of node "offset_b2"

    # Start of node "dissolve2"
    lastNode = app.createNode("net.sf.openfx.DissolvePlugin", 1, group)
    lastNode.setScriptName("dissolve2")
    lastNode.setLabel("dissolve2")
    lastNode.setPosition(746, 893)
    lastNode.setSize(100, 32)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupdissolve2 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValueAtTime(0, 235, 0)
        param.setValueAtTime(1, 265, 0)
        del param

    del lastNode
    # End of node "dissolve2"

    # Start of node "final_range"
    lastNode = app.createNode("net.sf.openfx.FrameRange", 1, group)
    lastNode.setScriptName("final_range")
    lastNode.setLabel("final_range")
    lastNode.setPosition(746, 974)
    lastNode.setSize(100, 55)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupfinal_range = lastNode

    param = lastNode.getParam("frameRange")
    if param is not None:
        param.setValue(500, 1)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(1 - 1)</Natron>")
        del param

    del lastNode
    # End of node "final_range"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(807, -561)
    lastNode.setSize(14, 14)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "output_dot"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("output_dot")
    lastNode.setLabel("output_dot")
    lastNode.setPosition(806, 678)
    lastNode.setSize(14, 14)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupoutput_dot = lastNode

    del lastNode
    # End of node "output_dot"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupfinal_range)
    groupoffset_b.connectInput(0, groupDot1)
    groupoffset_a.connectInput(0, groupDot1)
    groupdissolve.connectInput(0, groupoffset_a)
    groupdissolve.connectInput(1, groupoffset_b)
    groupframe_range.connectInput(0, groupdissolve)
    groupoffset_a2.connectInput(0, groupoutput_dot)
    groupoffset_b2.connectInput(0, groupoutput_dot)
    groupdissolve2.connectInput(0, groupoffset_a2)
    groupdissolve2.connectInput(1, groupoffset_b2)
    groupfinal_range.connectInput(0, groupdissolve2)
    groupDot1.connectInput(0, groupImage)
    groupoutput_dot.connectInput(0, groupImage)

    try:
        extModule = sys.modules["LoopDissolveExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
