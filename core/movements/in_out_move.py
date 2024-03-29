import NatronEngine
from nx import getNode, get_bbox
from base import link_to_parent, get_duration, get_start_frame, get_rscale, get_format
from movements_common import center_from_input_bbox


def main(thisParam, thisNode, thisGroup, app, userEdited):
    if not userEdited:
        return
    knob_name = thisParam.getScriptName()

    link_to_parent(thisNode, thisParam, thisGroup)

    if knob_name == 'refresh':
        refresh(thisNode)
    elif knob_name == 'input_move' or knob_name == 'output_move':
        disable_scale_dimension(thisNode)
    elif knob_name == 'use_bbox':
        thisNode.bbox_extra.setEnabled(thisParam.get())


def disable_scale_dimension(thisNode):

    scale_dimension_param = thisNode.getParam('scale_dimension')

    input_move = thisNode.getParam('input_move').get()
    output_move = thisNode.getParam('output_move').get()

    # si no hay ninguna opcion en 'scale' desabilita el parametro
    if input_move == 5 or output_move == 5:
        scale_dimension_param.setEnabled(True)
    else:
        scale_dimension_param.setEnabled(False)


def animation(param, values, start_frame, duration, bound, direction, exaggeration, dimension=None):
    lineal = NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeLinear
    horizontal = NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeHorizontal

    value_a = float(values[0])
    value_b = float(values[1])

    first_frame = start_frame
    last_frame = first_frame + duration

    if dimension == None:
        dimensions = range(param.getNumDimensions())
    else:
        dimensions = [dimension]

    for dimension in dimensions:
        param.setValueAtTime(value_a, first_frame, dimension)
        param.setValueAtTime(value_b, last_frame, dimension)

        if bound:
            # bound key frame
            bound_value = (abs(value_a - value_b) / 3) * bound
            bound_duration = duration / 2

            def bound_animation(value, reverse):
                if reverse:
                    bound_value_b = value - bound_value

                else:
                    bound_value_b = value + bound_value

                bound_key = last_frame - bound_duration
                param.setValueAtTime(bound_value_b, bound_key, dimension)

                if exaggeration:
                    post_bound_key = last_frame - duration / 4
                    post_bound_value = param.getValueAtTime(post_bound_key, dimension)
                    exaggeration_add = abs(post_bound_value - bound_value_b) * exaggeration
                    if reverse:
                        post_bound_value -= exaggeration_add
                    else:
                        post_bound_value += exaggeration_add

                    param.setValueAtTime(post_bound_value, post_bound_key, dimension)

                    pre_bound_key = bound_key - duration / 4
                    pre_bound_value = param.getValueAtTime(pre_bound_key, dimension)
                    exaggeration_add = abs(pre_bound_value - bound_value_b) * exaggeration
                    if reverse:
                        pre_bound_value -= exaggeration_add
                    else:
                        pre_bound_value += exaggeration_add

                    param.setValueAtTime(pre_bound_value, pre_bound_key, dimension)

            if direction == 'input':
                param.setInterpolationAtTime(first_frame, lineal, dimension)
                param.setInterpolationAtTime(last_frame, horizontal, dimension)

                reverse = value_b < value_a
                bound_animation(value_b, reverse)

            if direction == 'output':
                param.setInterpolationAtTime(first_frame, horizontal, dimension)
                param.setInterpolationAtTime(last_frame, lineal, dimension)

                reverse = value_b > value_a
                bound_animation(value_a, reverse)
        else:
            if direction == 'input':
                param.setInterpolationAtTime(first_frame, lineal, dimension)
                param.setInterpolationAtTime(last_frame, horizontal, dimension)
            else:
                param.setInterpolationAtTime(first_frame, horizontal, dimension)
                param.setInterpolationAtTime(last_frame, lineal, dimension)


def refresh(thisNode):
    rscale = get_rscale(thisNode)
    duration = get_duration(thisNode)
    current_format = get_format(thisNode)
    start_frame = get_start_frame(thisNode)

    transform = getNode(thisNode, 'transform')
    translate = transform.getParam('translate')
    rotate = transform.getParam('rotate')
    scale = transform.getParam('scale')
    center = transform.getParam('center')

    speed = thisNode.getParam('speed').get()
    input_move = thisNode.getParam('input_move').get()
    output_move = thisNode.getParam('output_move').get()
    exaggeration = thisNode.getParam('exaggeration').get()
    bound = thisNode.getParam('bound').get()
    transition_duration_percent = thisNode.getParam('transition_duration').get()
    initial_rotate = thisNode.getParam('initial_rotate').get()
    use_bbox = thisNode.getParam('use_bbox').get()
    bbox_extra = thisNode.getParam('bbox_extra').get()
    scale_dimension_param = thisNode.getParam('scale_dimension')
    scale_dimension = scale_dimension_param.get()

    width = current_format[0]
    height = current_format[1]

    # restaurar valores
    translate.restoreDefaultValue(0)
    translate.restoreDefaultValue(1)
    rotate.restoreDefaultValue(0)
    scale.restoreDefaultValue(0)
    scale.restoreDefaultValue(1)

    # calcula la duracion de la transicion
    transition_duration = ((transition_duration_percent / 2) * duration) / 100

    # bounding box input
    center_from_input_bbox(thisNode, center)

    bbox = get_bbox(thisNode.getInput(0))
    input_width = abs(bbox.x1 - bbox.x2)
    input_height = abs(bbox.y1 - bbox.y2)

    if use_bbox:
        bbox_extra *= rscale
        input_width += bbox_extra
        input_height += bbox_extra

        value_x1 = -input_width
        value_x2 = input_width
        value_y1 = -input_height
        value_y2 = input_height
    else:
        value_x1 = -bbox.x2
        value_x2 = (width - bbox.x2) + input_width
        value_y1 = -bbox.y2
        value_y2 = (height - bbox.y2) + input_height

    if input_move:
        def translate_input_anim(value, dimension=0):
            animation(translate, [value, 0], start_frame, transition_duration, bound, 'input', exaggeration, dimension=dimension)
            animation(rotate, [initial_rotate, 0], start_frame, transition_duration, bound, 'input', exaggeration)

        def scale_input_anim(value_a, value_b):
            if scale_dimension == 2:
                animation(scale, [value_a, value_b], start_frame, transition_duration, bound, 'input', exaggeration)
            else:
                animation(scale, [value_a, value_b], start_frame, transition_duration, bound, 'input', exaggeration, dimension=scale_dimension)
            animation(rotate, [initial_rotate, 0], start_frame, transition_duration, bound, 'input', exaggeration)

        if input_move == 1:
            translate_input_anim(value_x1)
        elif input_move == 2:
            translate_input_anim(value_x2)
        elif input_move == 3:
            translate_input_anim(value_y1, 1)
        elif input_move == 4:
            translate_input_anim(value_y2, 1)
        elif input_move == 5:
            scale_input_anim(0, 1)

    if output_move:
        start_frame_output = start_frame + duration - transition_duration

        def translate_output_anim(value, dimension=0):
            animation(translate, [0, value], start_frame_output, transition_duration, bound, 'output', exaggeration, dimension=dimension)
            animation(rotate, [0, initial_rotate], start_frame_output, transition_duration, bound, 'output', exaggeration)

        def scale_output_anim(value_a, value_b):
            if scale_dimension == 2:
                animation(scale, [value_a, value_b], start_frame_output, transition_duration, bound, 'output', exaggeration)
            else:
                animation(scale, [value_a, value_b], start_frame_output, transition_duration, bound, 'output', exaggeration, dimension=scale_dimension)

            animation(rotate, [0, initial_rotate], start_frame_output, transition_duration, bound, 'output', exaggeration)

        if output_move == 1:
            translate_output_anim(value_x1)
        elif output_move == 2:
            translate_output_anim(value_x2)
        elif output_move == 3:
            translate_output_anim(value_y1, 1)
        elif output_move == 4:
            translate_output_anim(value_y2, 1)
        elif output_move == 5:
            scale_output_anim(1, 0)
