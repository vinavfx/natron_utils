from base import link_to_parent, get_rscale, get_duration, get_format, get_start_frame
from nx import getNode
from text_fit import separate_text, get_bbox_format


def main(thisParam, thisNode, thisGroup, app, userEdited):
    if not userEdited:
        return

    knob_name = thisParam.getScriptName()
    link_to_parent(thisNode, thisParam, thisGroup)

    if knob_name == 'refresh':
        refresh(thisNode)


def refresh(thisNode):
    rscale = get_rscale(thisNode)
    duration = get_duration(thisNode)
    current_format = get_format(thisNode)
    start_frame = get_start_frame(thisNode)

    corner_radius = thisNode.corner_radius.get() * rscale
    bottom_margin = current_format[1] * thisNode.bottom_margin.get() / 100

    rectangle = getNode(thisNode, 'rectangle')
    rectangle_height = current_format[1] + bottom_margin
    rectangle.getParam('cornerRadius').set(corner_radius, corner_radius)

    rectangle.getParam('size').set(current_format[0], rectangle_height)
    rectangle.getParam('bottomLeft').set(0, -bottom_margin)

    #
    #

    frame_width = 100 - (thisNode.frame_width.get() / 2)

    photo_mask = getNode(thisNode, 'photo_mask')
    photo_mask_width = current_format[0] * frame_width / 100
    width_residue = current_format[0] - photo_mask_width
    photo_mask_height = current_format[1] - width_residue

    photo_mask_left = (current_format[0] - photo_mask_width) / 2
    photo_mask_bottom = (current_format[1] - photo_mask_height) / 2

    photo_mask.getParam('size').set(photo_mask_width, photo_mask_height)
    photo_mask.getParam('bottomLeft').set(photo_mask_left, photo_mask_bottom)
    photo_mask.getParam('cornerRadius').set(corner_radius, corner_radius)

    #
    #

    text_bbox = getNode(thisNode, 'text_bbox')
    text_width = photo_mask_width
    text_height = bottom_margin

    text_left = photo_mask_left
    text_bottom = -bottom_margin

    bottom_height = abs(text_bottom - photo_mask_bottom)

    text_bottom += (bottom_height - text_height) / 2

    text_bbox.getParam('size').set(text_width, text_height)
    text_bbox.getParam('bottomLeft').set(text_left, text_bottom)

    text_fit = getNode(thisNode, 'text_fit')
    text_fit.getParam('refresh').trigger()
    separate_text(text_fit, thisNode)

    set_text_color(thisNode)

    adjust_photo_transform(thisNode, photo_mask_width, current_format)
    adjust_output_transform(thisNode, current_format)


def set_text_color(thisNode):
    getNode(thisNode, 'title_node').getParam('color').copy(thisNode.title_color)
    getNode(thisNode, 'subtitle_node').getParam('color').copy(thisNode.subtitle_color)


def adjust_photo_transform(thisNode, photo_mask_width, current_format):
    transform = getNode(thisNode, 'photo_transform')

    scale = float(photo_mask_width) / current_format[0]
    transform.getParam('scale').set(scale, scale)

    transform.getParam('center').set(current_format[0] / 2, current_format[1] / 2)


def adjust_output_transform(thisNode, current_format):

    merge = getNode(thisNode, 'merge')
    transform = getNode(thisNode, 'transform')

    height_format = current_format[1]
    width, height = get_bbox_format(merge)

    scale = float(height_format) / float(height)
    transform.getParam('scale').set(scale, scale)

    residue = height - height_format
    translate_y = (residue / 2) * scale
    transform.getParam('translate').set(0, translate_y)

    transform.getParam('center').set(current_format[0] / 2, current_format[1] / 2)