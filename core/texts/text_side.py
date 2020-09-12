from base import link_to_parent
from text_fit import refresh_text_fit
from nx import getNode, get_bbox, bbox_bake, createNode, autocrop, alert
from vina import value_by_durations


def main(thisParam, thisNode, thisGroup, app, userEdited):
    if not userEdited:
        return

    knob_name = thisParam.getScriptName()
    link_to_parent(thisNode, thisParam, thisGroup)

    if knob_name == 'refresh':
        refresh(thisNode)


def update_rectangle(thisNode, text_fit):
    rscale = thisNode.rscale.get()

    rectangle_separation = 20 * rscale
    rectangle_width = thisNode.rectangle_width.get() * rscale

    bbox = get_bbox(text_fit)

    rectangle = getNode(thisNode, 'rectangle')
    size_x = rectangle_width
    size_y = bbox.y2 - bbox.y1

    if thisNode.align.get() == 0:
        pos_x = bbox.x2 + rectangle_separation
        pos_y = bbox.y1
    else:
        pos_x = bbox.x1 - rectangle_width - rectangle_separation
        pos_y = bbox.y1

    rectangle.getParam('bottomLeft').set(pos_x, pos_y)
    rectangle.getParam('size').set(size_x, size_y)

    # actualiza movimiento del rectangulo
    getNode(thisNode, 'rectangle_move').getParam('refresh').trigger()

    # promedio de color del titulo y subtitulo para el rectangulo
    title_color = thisNode.getParam('title_color').get()
    subtitle_color = thisNode.getParam('subtitle_color').get()
    for i in range(3):
        color = (title_color[i] + subtitle_color[i]) / 2
        rectangle.getParam('color1').setValue(color, i)

    return [rectangle_separation, rectangle_width]


def update_animation(thisNode):
    # cambia la direccion del movimiento del titulo y subtitulo
    subtitle_move = getNode(thisNode, 'subtitle_move')
    title_move = getNode(thisNode, 'title_move')

    index_move = 1
    if thisNode.align.get() == 0:
        index_move = 2
    else:
        index_move = 1

    subtitle_move.getParam('input_move').set(index_move)
    subtitle_move.getParam('output_move').set(index_move)
    title_move.getParam('input_move').set(index_move)
    title_move.getParam('output_move').set(index_move)

    #
    #

    # desfase de tiempo
    durations = thisNode.getParam('durations')
    title_durations = title_move.getParam('durations')
    subtitle_durations = subtitle_move.getParam('durations')

    speed = thisNode.speed.get()
    duration = durations.getValue(speed)

    #
    #

    # desfase
    _title_gap = value_by_durations(thisNode.title_gap.get(), durations.get())
    _subtitle_gap = value_by_durations(thisNode.subtitle_gap.get(), durations.get())

    title_gap = _title_gap[speed] / 2
    subtitle_gap = _subtitle_gap[speed] / 2

    title_durations.restoreDefaultValue(speed)
    subtitle_durations.restoreDefaultValue(speed)

    title_duration = duration - title_gap
    title_durations.setValue(title_duration, speed)

    subtitle_duration = duration - subtitle_gap
    subtitle_durations.setValue(subtitle_duration, speed)

    #
    #

    # start frame
    start_frame = thisNode.start_frame.get()

    title_start_frame = title_move.getParam('start_frame')
    subtitle_start_frame = subtitle_move.getParam('start_frame')

    title_start_frame.restoreDefaultValue()
    subtitle_start_frame.restoreDefaultValue()

    start_frame_title = title_gap / 2
    title_start_frame.set(start_frame_title + start_frame)

    start_frame_subtitle = subtitle_gap / 2
    subtitle_start_frame.set(start_frame_subtitle + start_frame)

    #
    #

    # actualiza los nodos de movimiento
    subtitle_move.getParam('refresh').trigger()
    title_move.getParam('refresh').trigger()


def refresh(thisNode):
    title_node, subtitle_node = refresh_text_fit(thisNode)

    title_color = thisNode.title_color
    subtitle_color = thisNode.subtitle_color

    title_node.getParam('color').copy(title_color)
    subtitle_node.getParam('color').copy(subtitle_color)

    text_fit = getNode(thisNode, 'TextFit0')

    rectangle_separation, rectangle_width = update_rectangle(thisNode, text_fit)

    crop = createNode('crop', 'croping', thisNode, force=False)
    autocrop(thisNode, text_fit, crop)

    crop_size = crop.getParam('size')
    crop_bottom_left = crop.getParam('bottomLeft')

    crop_added = rectangle_separation + (rectangle_width / 2)

    crop_size_x = crop_size.getValue(0) + (crop_added * 2)
    crop_pos_x = crop_bottom_left.getValue(0) - crop_added

    crop_size.setValue(crop_size_x, 0)
    crop_bottom_left.setValue(crop_pos_x, 0)

    # centrar transform para el skew
    skew_node = getNode(thisNode, 'skew_node')
    skew_node.getParam('resetCenter').trigger()
    skew_node.getParam('translate').set(0, 0)

    update_animation(thisNode)