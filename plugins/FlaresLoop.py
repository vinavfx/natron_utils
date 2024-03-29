# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named FlaresLoopExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from FlaresLoopExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.FlaresLoop"

def getLabel():
    return "FlaresLoop"

def getVersion():
    return 1

def getIconPath():
    return "FlaresLoop.png"

def getGrouping():
    return "videovina/Draw"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)
    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("flares_loop.main")
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

    param = lastNode.createButtonParam("link", "Link To Parent")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.link = param
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

    param = lastNode.createPathParam("flares_folder", "Flares Folder")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setValue("/home/pancho/Documents/develop/videovina/private/assets/flares")
    lastNode.flares_folder = param
    del param

    param = lastNode.createChoiceParam("flares", "Flares")
    entries = [ ("1 - Colourful optical flares", "colourful_optical_flares"),
    ("2 - Cool flare bokeh wipes", "cool_flare_bokeh_wipes"),
    ("3 - Corner flares bokeh", "corner_flares_bokeh"),
    ("4 - Flare bokeh wipes", "flare_bokeh_wipes"),
    ("5 - Flare color gradient", "flare_color_gradient"),
    ("6 - Frantic wipes transitions", "frantic_wipes_transitions"),
    ("7 - More spectral colour flares", "more_spectral_colour_flares"),
    ("8 - Red flare", "red_flare"),
    ("9 - Spectral colour flares", "spectral_colour_flares"),
    ("10 - Two flares blue and red", "two_flares_blue_and_red"),
    ("11 - Warm artifacts", "warm_artifacts"),
    ("12 - Warm rays", "warm_rays")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.flares = param
    del param

    param = lastNode.createButtonParam("reload_flares", "Reload Flares")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.reload_flares = param
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

    param = lastNode.createColorParam("flare_color", "Color", False)
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(4, 0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(4, 1)
    param.setMinimum(-2147483648, 2)
    param.setMaximum(2147483647, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(4, 2)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 0)
    param.setValue(1, 1)
    param.setValue(1, 2)
    lastNode.flare_color = param
    del param

    param = lastNode.createDoubleParam("flare_gamma", "Gamma")
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
    param.setValue(1, 0)
    lastNode.flare_gamma = param
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

    param = lastNode.createDoubleParam("flare_blur", "Blur")
    param.setMinimum(0, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.flare_blur = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output")
    lastNode.setPosition(1299, 876)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "read"
    lastNode = app.createNode("fr.inria.built-in.Read", 1, group)
    lastNode.setScriptName("read")
    lastNode.setLabel("read")
    lastNode.setPosition(1287, 622)
    lastNode.setSize(128, 78)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupread = lastNode

    param = lastNode.getParam("decodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.ReadOIIO")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(colourful_optical_flares_0346.jpg)</Natron>")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/home/pancho/Documents/develop/videovina/private/assets/flares/colourful_optical_flares/colourful_optical_flares_####.jpg")
        del param

    param = lastNode.getParam("before")
    if param is not None:
        param.set("loop")
        del param

    param = lastNode.getParam("after")
    if param is not None:
        param.set("loop")
        del param

    param = lastNode.getParam("filePremult")
    if param is not None:
        param.set("opaque")
        del param

    param = lastNode.getParam("outputPremult")
    if param is not None:
        param.set("opaque")
        del param

    param = lastNode.getParam("outputComponents")
    if param is not None:
        param.set("RGB")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("ocioInputSpace")
    if param is not None:
        param.setValue("sRGB")
        del param

    param = lastNode.getParam("outputLayerChoice")
    if param is not None:
        param.setValue("Color.RGB")
        del param

    del lastNode
    # End of node "read"

    # Start of node "transform"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("transform")
    lastNode.setLabel("transform")
    lastNode.setPosition(1299, 794)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.3, 0.1)
    grouptransform = lastNode

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        del param

    param = lastNode.getParam("center")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("transformCenterChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "transform"

    # Start of node "CropFormat1"
    lastNode = app.createNode("vv.CropFormat", 1, group)
    lastNode.setScriptName("CropFormat1")
    lastNode.setLabel("CropFormat1")
    lastNode.setPosition(1299, 834)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupCropFormat1 = lastNode

    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("crop_format.main")
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

    param = lastNode.createButtonParam("link", "Link To Parent")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.link = param
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
    # End of node "CropFormat1"

    # Start of node "Grade1"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade1")
    lastNode.setLabel("Grade1")
    lastNode.setPosition(1299, 710)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade1 = lastNode

    param = lastNode.getParam("white")
    if param is not None:
        param.setValue(0, 3)
        del param

    del lastNode
    # End of node "Grade1"

    # Start of node "Blur1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur1")
    lastNode.setLabel("Blur1")
    lastNode.setPosition(1299, 752)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur1 = lastNode

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("nearest")
        del param

    del lastNode
    # End of node "Blur1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupCropFormat1)
    grouptransform.connectInput(0, groupBlur1)
    groupCropFormat1.connectInput(0, grouptransform)
    groupGrade1.connectInput(0, groupread)
    groupBlur1.connectInput(0, groupGrade1)

    param = groupCropFormat1.getParam("state_label")
    group.getParam("state_label").setAsAlias(param)
    del param
    param = groupCropFormat1.getParam("format")
    group.getParam("format").setAsAlias(param)
    del param
    param = groupGrade1.getParam("white")
    param.slaveTo(group.getParam("flare_color"), 0, 0)
    param.slaveTo(group.getParam("flare_color"), 1, 1)
    param.slaveTo(group.getParam("flare_color"), 2, 2)
    del param
    param = groupGrade1.getParam("gamma")
    param.slaveTo(group.getParam("flare_gamma"), 0, 0)
    param.slaveTo(group.getParam("flare_gamma"), 1, 0)
    param.slaveTo(group.getParam("flare_gamma"), 2, 0)
    param.slaveTo(group.getParam("flare_gamma"), 3, 0)
    del param
    param = groupBlur1.getParam("size")
    param.slaveTo(group.getParam("flare_blur"), 0, 0)
    param.slaveTo(group.getParam("flare_blur"), 1, 0)
    del param

    try:
        extModule = sys.modules["FlaresLoopExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
