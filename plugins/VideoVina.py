# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named VideoVinaExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from VideoVinaExt import *
except ImportError:
    pass

def getPluginID():
    return "vv.VideoVina"

def getLabel():
    return "VideoVina"

def getVersion():
    return 1

def getIconPath():
    return "VideoVina.png"

def getGrouping():
    return "videovina/Templates"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)
    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("videovina.main")
        del param


    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "Control")
    param = lastNode.createPathParam("videovina_root", "VideoVina Root Folder")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("Carpeta raiz de videovina, donde esta toda la web y archivos privados que contienen las plantillas base, fotos de muestra y la musica.")
    param.setAddNewLine(True)
    param.setValue("/home/pancho/Documents/GitHub/videovina")
    lastNode.videovina_root = param
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

    param = lastNode.createButtonParam("save_production", "Save Production Projects")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("Guarda una versión de producción, elimina todo\nlo innecesario, y procesa las capas que no serán modificadas")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    lastNode.save_production = param
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

    param = lastNode.createSeparatorParam("sep10", "")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep10 = param
    del param

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
    param.set("Slow")
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

    param = lastNode.createStringParam("production_slide_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    PRODUCTION SLIDE :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.production_slide_label = param
    del param

    param = lastNode.createFileParam("videovina_project", "VideoVina Project")
    param.setSequenceEnabled(False)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    param.setValue("/home/pancho/Documents/GitHub/videovina/tmp/as3/private/admin/projects/testing/project.json")
    lastNode.videovina_project = param
    del param

    param = lastNode.createButtonParam("update_videovina_project", "Update VideoVina Project")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("Actualiza datos, a partir de los datos del proyecto videovina.json")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.update_videovina_project = param
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
    lastNode.durations = param
    del param

    param = lastNode.createIntParam("transition_duration", "Transition Duration")
    param.setMinimum(0, 0)
    param.setMaximum(100, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("esta velocidad de frames corresponde a la velocidad normal,\ny calculta la velocidad final dependiendo de la velocidad de la slide ( Slow, Normal, Fast )\n")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(30, 0)
    lastNode.transition_duration = param
    del param

    param = lastNode.createChoiceParam("default_color", "Default Color")
    entries = [ ("-", ""),
    ("Color 1", ""),
    ("Color 2", ""),
    ("Color 3", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.set("Color 3")
    lastNode.default_color = param
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
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    param.setValue(1, 1)
    param.setValue(0.5725490196078431, 2)
    lastNode.color = param
    del param

    param = lastNode.createFileParam("song", "Song")
    param.setSequenceEnabled(False)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    param.setValue("/home/pancho/Documents/GitHub/videovina/private/music/love/Redwood Trail.mp3")
    lastNode.song = param
    del param

    param = lastNode.createFileParam("font", "Font")
    param.setSequenceEnabled(False)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    param.setValue("/home/pancho/Documents/GitHub/videovina/private/fonts/Delius Swash Caps.ttf")
    lastNode.font = param
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

    param = lastNode.createStringParam("develop_slide", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("- - - - - - - >    DEVELOP SLIDE :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.develop_slide = param
    del param

    param = lastNode.createChoiceParam("slide", "Slide")
    entries = [ ("GlassSlide", ""),
    ("SlideBase", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.set("SlideBase")
    lastNode.slide = param
    del param

    param = lastNode.createChoiceParam("transition", "Transition")
    entries = [ ("FlareTransition", ""),
    ("GlassTransition", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.transition = param
    del param

    param = lastNode.createIntParam("amount_slide", "Base Slide")
    param.setMinimum(0, 0)
    param.setMaximum(20, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(5, 0)
    lastNode.amount_slide = param
    del param

    param = lastNode.createButtonParam("generate_slides", "Generate Base")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.generate_slides = param
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

    lastNode.sim_tab = lastNode.createPageParam("sim_tab", "Production Simulation")
    param = lastNode.createPathParam("reference_pictures", "Reference Pictures Folder")

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("Carpeta donde estan las fotos, estas solo se usaran como referencia para hacer la plantilla base.")
    param.setAddNewLine(True)
    param.setValue("/home/pancho/Documents/GitHub/videovina/private/photos/travel")
    lastNode.reference_pictures = param
    del param

    param = lastNode.createBooleanParam("reformat", "Reformat")

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(True)
    lastNode.reformat = param
    del param

    param = lastNode.createBooleanParam("random_pictures", "Random")

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.random_pictures = param
    del param

    param = lastNode.createButtonParam("generate_pictures", "Generate Pictures")

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.generate_pictures = param
    del param

    param = lastNode.createSeparatorParam("sep9", "")

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep9 = param
    del param

    param = lastNode.createInt2DParam("production_slides", "Production Slides Range")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)
    param.setDefaultValue(0, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(3, 0)
    param.setValue(7, 1)
    lastNode.production_slides = param
    del param

    param = lastNode.createButtonParam("generate_production_slides", "Generate Production")

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.generate_production_slides = param
    del param

    param = lastNode.createIntParam("last_slide", "Last Slide")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(100, 0)
    lastNode.last_slide = param
    del param

    param = lastNode.createButtonParam("last_slide_delete", "Delete")

    # Add the param to the page
    lastNode.sim_tab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.last_slide_delete = param
    del param

    lastNode.project_rab = lastNode.createPageParam("project_rab", "Output Project")
    param = lastNode.createColorParam("color_1", "Color 1", False)
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
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.6375969648361206, 0)
    param.setValue(0.5088813304901123, 1)
    param.setValue(0.2746773660182953, 2)
    lastNode.color_1 = param
    del param

    param = lastNode.createColorParam("color_2", "Color 2", False)
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
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 0)
    param.setValue(0.278894305229187, 1)
    param.setValue(0.05126946419477463, 2)
    lastNode.color_2 = param
    del param

    param = lastNode.createColorParam("color_3", "Color 3", False)
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
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.2345505952835083, 0)
    param.setValue(0.5332764983177185, 1)
    param.setValue(0.0176419522613287, 2)
    lastNode.color_3 = param
    del param

    param = lastNode.createSeparatorParam("sep7", "")

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep7 = param
    del param

    param = lastNode.createChoiceParam("default_song", "Song")
    entries = [ ("Sitcom Joy  -  Kid", "Sitcom Joy"),
    ("African Bliss  -  Kid", "African Bliss"),
    ("Jingle Bells  -  Christmas", "Jingle Bells"),
    ("Jingle Bells Jazz  -  Christmas", "Jingle Bells Jazz"),
    ("Deck the Halls  -  Christmas", "Deck the Halls"),
    ("Deck the Halls Jazz  -  Christmas", "Deck the Halls Jazz"),
    ("We Wish You a Merry Christmas Jazz  -  Christmas", "We Wish You a Merry Christmas Jazz"),
    ("Earning Happiness  -  Wedding", "Earning Happiness"),
    ("Green Leaves  -  Wedding", "Green Leaves"),
    ("Penny Whistle  -  Wedding", "Penny Whistle"),
    ("Solo Acoustic  -  Others", "Solo Acoustic"),
    ("Mountain Sun  -  Others", "Mountain Sun"),
    ("Bouncy Gypsy Beats  -  Others", "Bouncy Gypsy Beats"),
    ("Jazzy Detective  -  Others", "Jazzy Detective"),
    ("Careful Tiptoe  -  Others", "Careful Tiptoe"),
    ("Happy African Village  -  Others", "Happy African Village"),
    ("Iyanetha  -  Others", "Iyanetha"),
    ("Interstellar Space  -  Others", "Interstellar Space"),
    ("Rhastafarian  -  Others", "Rhastafarian"),
    ("Heading West  -  Others", "Heading West"),
    ("Bustin Loose  -  Others", "Bustin Loose"),
    ("Acoustic Guitar  -  Love", "Acoustic Guitar"),
    ("Brides Ballad  -  Love", "Brides Ballad"),
    ("Cool Steel Breeze  -  Love", "Cool Steel Breeze"),
    ("One Fine Day  -  Love", "One Fine Day"),
    ("Redwood Trail  -  Love", "Redwood Trail"),
    ("West in Africa  -  Baby", "West in Africa"),
    ("Pepper The Pig  -  Baby", "Pepper The Pig"),
    ("Balkan Gypsy Party  -  Baby", "Balkan Gypsy Party"),
    ("Mad Hatter Tea Party  -  Baby", "Mad Hatter Tea Party"),
    ("Walk In The Park  -  Travels", "Walk In The Park"),
    ("Acoustic Rock  -  Travels", "Acoustic Rock"),
    ("Gameshow Brazz  -  Travels", "Gameshow Brazz"),
    ("African Moon  -  Travels", "African Moon"),
    ("Crazy Balloons  -  Birthday", "Crazy Balloons"),
    ("Robot Gypsy Jazz  -  Birthday", "Robot Gypsy Jazz"),
    ("Happy Clappy  -  Birthday", "Happy Clappy")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.set("Rhastafarian  -  Others")
    lastNode.default_song = param
    del param

    param = lastNode.createButtonParam("play", "Play")

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.play = param
    del param

    param = lastNode.createButtonParam("stop", "Stop")

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.stop = param
    del param

    param = lastNode.createChoiceParam("default_font", "Font")
    entries = [ ("Great Vibes", "Great Vibes"),
    ("Dancing Script", "Dancing Script"),
    ("Delius Swash Caps", "Delius Swash Caps"),
    ("Kingthings Trypewriter", "Kingthings Trypewriter"),
    ("Major Shift", "Major Shift"),
    ("Note This", "Note This"),
    ("Open Sans Bold", "Open Sans Bold"),
    ("Open Sans Light", "Open Sans Light"),
    ("Pompiere Regular", "Pompiere Regular"),
    ("Tinos", "Tinos"),
    ("Licenses", "Licenses")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.set("Delius Swash Caps")
    lastNode.default_font = param
    del param

    param = lastNode.createSeparatorParam("sep8", "")

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep8 = param
    del param

    param = lastNode.createStringParam("default_json_project", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("SAVE PROJECT IN:       static/templates/.../project.json")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("Proyecto guardado en el directorio static de la carpeta base de videovina")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.default_json_project = param
    del param

    param = lastNode.createButtonParam("export_default_project", "Export Project to Static")

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("Exporta todos los datos por defecto a un archivo \'project.json\' y copia  el contenido de resources a la carpeta static de videovina.")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    lastNode.export_default_project = param
    del param

    param = lastNode.createButtonParam("transfer_to_static", "Transfer To Static")

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("Transfiere todos los recursos generados, a la carpeta estatica de videovina, con las imagenes y videos comprimidos para mayor rapides de la pagina.")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.transfer_to_static = param
    del param

    param = lastNode.createButtonParam("videovina_info", "Export VIdeoVina Info")

    # Add the param to the page
    lastNode.project_rab.addParam(param)

    # Set param properties
    param.setHelp("Genera 1 imagen por cada slide, renderizandola\njusto en el centro del tiempo de la slide, la imagen queda en alpha y sin textos, lo copia a la carpeta estatica de videovina \'static/templates/<template_name>\'/resources/overlap\'")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.videovina_info = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'sim_tab', 'project_rab', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "LastNode"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("LastNode")
    lastNode.setLabel("LastNode")
    lastNode.setPosition(0, 0)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupLastNode = lastNode

    del lastNode
    # End of node "LastNode"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(0, 0)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupLastNode)

    try:
        extModule = sys.modules["VideoVinaExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
