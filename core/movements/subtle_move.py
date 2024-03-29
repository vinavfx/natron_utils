from nx import getNode
import NatronEngine
from math import cos, sin
from base import link_to_parent, get_duration, get_format, get_rscale
from movements_common import center_from_input_bbox
from shaker import shaker


def main(thisParam, thisNode, thisGroup, app, userEdited):
    if not userEdited:
        return

    knob_name = thisParam.getScriptName()

    link_to_parent(thisNode, thisParam, thisGroup)

    if knob_name == 'refresh':
        refresh(thisNode)


def animation(param, start_frame, duration, values, break_point, break_duration, exaggeration=0, dimension=None):

    if dimension == None:
        dimensions = range(param.getNumDimensions())
    else:
        dimensions = [dimension]

    for dimension in dimensions:

        horizontal = NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeHorizontal
        lineal = NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeLinear
        smooth = NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeSmooth

        first_frame = start_frame
        last_frame = first_frame + duration

        value_a = float(values[0])
        value_b = float(values[1])

        param.restoreDefaultValue(dimension)

        param.setValueAtTime(value_a, first_frame, dimension)
        param.setValueAtTime(value_b, last_frame, dimension)
        param.setInterpolationAtTime(first_frame, lineal, dimension)
        param.setInterpolationAtTime(last_frame, lineal, dimension)

        break_point_duration = (break_duration * duration) / 100
        first_frame_break = (break_point * duration) / 100
        last_frame_break = first_frame_break + break_point_duration

        # resta la mitad de la duracion del quebre para que quede centrado
        first_frame_break -= break_point_duration / 2
        last_frame_break -= break_point_duration / 2

        break_point_value_a = param.getValueAtTime(first_frame_break, dimension)
        break_point_value_b = param.getValueAtTime(last_frame_break, dimension)

        if not exaggeration:
            continue

        # exaggeration
        exagg_a = abs(value_a - break_point_value_a) * exaggeration
        exagg_b = abs(value_b - break_point_value_b) * exaggeration

        if value_a > value_b:
            break_point_value_a += exagg_a
            break_point_value_b -= exagg_b
        else:
            break_point_value_a -= exagg_a
            break_point_value_b += exagg_b

        param.setValueAtTime(break_point_value_a, first_frame_break, dimension)
        param.setValueAtTime(break_point_value_b, last_frame_break, dimension)

        # deja en lineal los 2 key del punto de quebre
        param.setInterpolationAtTime(first_frame_break, lineal, dimension)
        param.setInterpolationAtTime(last_frame_break, lineal, dimension)

        # le suma un frame antes y despues del punto de quebre, para que solo el
        # punto de quebre tenga interpolacion horizontal y el resto lineal
        after_frame = last_frame_break + 1
        after_value = param.getValueAtTime(after_frame, dimension)
        param.setValueAtTime(after_value, after_frame, dimension)

        before_frame = first_frame_break - 1
        before_value = param.getValueAtTime(before_frame, dimension)
        param.setValueAtTime(before_value, before_frame, dimension)

        # cambia a 'smooth' la interpolacion del punto de quebre, por que ya se crearon los key 'after' y 'before'
        param.setInterpolationAtTime(first_frame_break, smooth, dimension)
        param.setInterpolationAtTime(last_frame_break, smooth, dimension)


def shaker_move(thisNode, scale_param, rotate_param, translate_param):
    frequency = thisNode.frequency.get()

    scale = thisNode.scale_shaker.get()
    translate = thisNode.translate_shaker.get()
    rotate = thisNode.rotate_shaker.get()
    seed_activate = thisNode.getParam('seed_activate')
    seed = None
    if seed_activate:
        if seed_activate.get():
            seed = thisNode.getParam('seed').get()

    if scale:
        shaker(thisNode, scale_param, frequency, scale=scale, restore=False, seed=seed)
    if translate:
        shaker(thisNode, translate_param, frequency, translate=translate, restore=False, seed=seed)
    if rotate:
        shaker(thisNode, rotate_param, frequency, rotate=rotate, restore=False, seed=seed)


def refresh(thisNode):
    duration = get_duration(thisNode)
    start_frame = 1
    rscale = get_rscale(thisNode)
    current_format = get_format(thisNode)

    transform = getNode(thisNode, 'Transform')
    scale = transform.getParam('scale')
    rotate = transform.getParam('rotate')
    translate = transform.getParam('translate')
    center = transform.getParam('center')

    movement = thisNode.getParam('movement').get()
    level = thisNode.getParam('level').get()

    break_point = thisNode.getParam('break_point').get()
    break_duration = thisNode.getParam('break_point_duration').get()
    exaggeration = thisNode.getParam('exaggeration').get()
    center_from_input = thisNode.getParam('center').get()
    offset = thisNode.scale_offset.get()

    width = current_format[0]
    height = current_format[1]

    scale.restoreDefaultValue(0)
    scale.restoreDefaultValue(1)
    rotate.restoreDefaultValue(0)
    translate.restoreDefaultValue(0)
    translate.restoreDefaultValue(1)

    # centra el pivote a partir del bounding box de entrada
    if center_from_input:
        center_from_input_bbox(thisNode, center)
    else:
        center.set(width / 2, height / 2)

    # Movimiento de translacion
    if movement <= 3:
        param = translate
        translate_level = level * 50 * rscale

        if thisNode.image_within_format.get():
            scale_for_translate_x = 1 - ((translate_level * 2) / width)
            scale_for_translate_y = 1 - ((translate_level * 2) / height)
        else:
            # calcula la escala para que la translacion siempre quede dentro de cuadro
            scale_for_translate_x = ((translate_level * 2) / width) + 1
            scale_for_translate_y = ((translate_level * 2) / height) + 1

        scale_for_translate_x += offset
        scale_for_translate_y += offset

        if movement == 0:
            values = [-translate_level, translate_level, 0, scale_for_translate_x]
        if movement == 1:
            values = [translate_level, -translate_level, 0, scale_for_translate_x]
        if movement == 2:
            values = [translate_level, -translate_level, 1, scale_for_translate_y]
        if movement == 3:
            values = [-translate_level, translate_level, 1, scale_for_translate_y]

        scale.set(values[3], values[3])

    # Movimiento de escala
    if thisNode.image_within_format.get():
        from_scale_level = 1
        to_scale_level = 1 - (level * 0.2)
    else:
        from_scale_level = 1 + (level * 0.2)
        to_scale_level = 1

    from_scale_level += offset
    to_scale_level += offset

    if movement == 4:
        values = [to_scale_level, from_scale_level, None]
        param = scale
    if movement == 5:
        values = [from_scale_level, to_scale_level, None]
        param = scale

    # Movimiento de rotacion
    if movement >= 6:
        rotate_level = 4.5 * level

        # calcula la escala a partir de la rotacion, para que
        # la imagen quede siempre dentro de cuadro
        rotate_quarter = abs(rotate_level / 55.0)
        new_width = height * cos(rotate_quarter) + width * sin(rotate_quarter)
        scale_for_rotate = abs(new_width / height)

        scale_for_rotate += offset

        if thisNode.image_within_format.get():
            None
        else:
            scale.set(scale_for_rotate, scale_for_rotate)

        if movement == 6:
            values = [rotate_level, -rotate_level, None]
            param = rotate
        if movement == 7:
            values = [-rotate_level, rotate_level, None]
            param = rotate

    animation(param, start_frame, duration, [
        values[0], values[1]], break_point, break_duration,
        exaggeration=exaggeration, dimension=values[2]
    )

    shaker_move(thisNode, scale, rotate, translate)
