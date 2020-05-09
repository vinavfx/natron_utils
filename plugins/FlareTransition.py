# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named FlareTransitionExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from FlareTransitionExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.flare_transition"

def getLabel():
    return "FlareTransition"

def getVersion():
    return 1

def getIconPath():
    return "Transition.png"

def getGrouping():
    return "videovina"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)
    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("transition.main")
        del param


    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createIntParam("start_frame", "Start Frame")
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    param.setValue(1, 0)
    lastNode.start_frame = param
    del param

    param = lastNode.createDouble2DParam("value_range", "A to B")
    param.setDisplayMinimum(-10000, 0)
    param.setDisplayMaximum(10000, 0)
    param.setDisplayMinimum(-10000, 1)
    param.setDisplayMaximum(10000, 1)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 1)
    lastNode.value_range = param
    del param

    param = lastNode.createIntParam("duration", "Duration")
    param.setMinimum(1, 0)
    param.setMaximum(100, 0)
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
    param.setValue(20, 0)
    lastNode.duration = param
    del param

    param = lastNode.createDoubleParam("exaggeration", "Exaggeration Time")
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
    param.setValue(0.7, 0)
    lastNode.exaggeration = param
    del param

    param = lastNode.createDoubleParam("exaggeration_value", "Exaggeration Value")
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
    param.setValue(0.7, 0)
    lastNode.exaggeration_value = param
    del param

    param = lastNode.createIntParam("blur_transition", "Blur")
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
    lastNode.blur_transition = param
    del param

    param = lastNode.createColorParam("Grade1white", "Flare Color", True)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(4, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(4, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(4, 2)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)
    param.setDisplayMinimum(0, 3)
    param.setDisplayMaximum(4, 3)
    param.setDefaultValue(1, 3)
    param.restoreDefaultValue(3)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Grade1white = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output")
    lastNode.setPosition(825, 665)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "A"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("A")
    lastNode.setLabel("A")
    lastNode.setPosition(599, 238)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupA = lastNode

    del lastNode
    # End of node "A"

    # Start of node "B"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("B")
    lastNode.setLabel("B")
    lastNode.setPosition(821, 79)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupB = lastNode

    del lastNode
    # End of node "B"

    # Start of node "Dissolve1"
    lastNode = app.createNode("net.sf.openfx.DissolvePlugin", 1, group)
    lastNode.setScriptName("Dissolve1")
    lastNode.setLabel("Dissolve1")
    lastNode.setPosition(825, 237)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupDissolve1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValueAtTime(0, 1, 0)
        param.setValueAtTime(0.15, 8, 0)
        param.setValueAtTime(0.85, 14, 0)
        param.setValueAtTime(1, 21, 0)
        del param

    del lastNode
    # End of node "Dissolve1"

    # Start of node "flare_merge"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("flare_merge")
    lastNode.setLabel("flare_merge")
    lastNode.setPosition(825, 524)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupflare_merge = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("plus")
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValueAtTime(0, 1, 0)
        param.setValueAtTime(1, 11, 0)
        param.setValueAtTime(0, 21, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    del lastNode
    # End of node "flare_merge"

    # Start of node "Grade1"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade1")
    lastNode.setLabel("Grade1")
    lastNode.setPosition(1284, 419)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade1 = lastNode

    del lastNode
    # End of node "Grade1"

    # Start of node "Blur"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur")
    lastNode.setLabel("Blur")
    lastNode.setPosition(825, 311)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValueAtTime(0, 1, 0)
        param.setValueAtTime(10, 11, 0)
        param.setValueAtTime(0, 21, 0)
        param.setValueAtTime(0, 1, 1)
        param.setValueAtTime(10, 11, 1)
        param.setValueAtTime(0, 21, 1)
        del param

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("nearest")
        del param

    del lastNode
    # End of node "Blur"

    # Start of node "flares_time_offset"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("flares_time_offset")
    lastNode.setLabel("flares_time_offset")
    lastNode.setPosition(1284, 524)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupflares_time_offset = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "flares_time_offset"

    # Start of node "Reformat2"
    lastNode = app.createNode("net.sf.openfx.Reformat", 1, group)
    lastNode.setScriptName("Reformat2")
    lastNode.setLabel("Reformat2")
    lastNode.setPosition(1284, 360)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupReformat2 = lastNode

    param = lastNode.getParam("NatronParamFormatSize")
    if param is not None:
        param.setValue(1920, 0)
        param.setValue(1080, 1)
        del param

    del lastNode
    # End of node "Reformat2"

    # Start of node "Flare"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Flare")
    lastNode.setLabel("Flare")
    lastNode.setPosition(1284, 287)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupFlare = lastNode

    del lastNode
    # End of node "Flare"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupflare_merge)
    groupDissolve1.connectInput(0, groupA)
    groupDissolve1.connectInput(1, groupB)
    groupflare_merge.connectInput(0, groupBlur)
    groupflare_merge.connectInput(1, groupflares_time_offset)
    groupGrade1.connectInput(0, groupReformat2)
    groupBlur.connectInput(0, groupDissolve1)
    groupflares_time_offset.connectInput(0, groupGrade1)
    groupReformat2.connectInput(0, groupFlare)

    param = groupGrade1.getParam("white")
    group.getParam("Grade1white").setAsAlias(param)
    del param
    param = groupflares_time_offset.getParam("timeOffset")
    param.setExpression("thisGroup.start_frame.get()", False, 0)
    del param

    try:
        extModule = sys.modules["FlareTransitionExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
