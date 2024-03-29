import os
import shutil
import json
from util import jread, hash_generator, makedir, fread, fwrite
from nx import get_connected_nodes, saveProject, absolute, warning, alert, get_node_path
from vina import get_ranges, get_last_frame, videovina_data


def main(thisParam, thisNode, thisGroup, app, userEdited):

    if not userEdited:
        if not 'VRender' in thisNode.getScriptName():
            # script name unico para identificar el nodo cuando renderizamos
            name = 'VRender_' + str(hash_generator(3))
            thisNode.setScriptName(name)

            # ya que el label por defecto es 'VinaRender1...', solo le cambiamos
            # el label solo si es el por defecto, para que cuando cambiemos
            # el label por fuera, no lo cambie a 'VinaRender'.
            if 'VinaRender' in thisNode.getLabel():
                thisNode.setLabel('VinaRender')

        return

    knob_name = thisParam.getScriptName()

    if knob_name == 'render':
        render(thisNode, app)

    elif knob_name == 'multi_project_render':
        multi_project_render(thisNode, app)

    elif knob_name == 'range' or knob_name == 'readfile':
        change_paramaters(thisNode)

    elif knob_name == 'project_frame_range':
        frame_range = app.frameRange.get()
        thisNode.range.set(frame_range[0], frame_range[1])


def change_paramaters(thisNode):
    frame_range = thisNode.getNode('frame_range')
    if not frame_range:
        return
    first_frame = frame_range.getParam('frameRange').getValue(0)
    last_frame = frame_range.getParam('frameRange').getValue(1)

    thisNode.reading.firstFrame.setValue(first_frame)
    thisNode.reading.lastFrame.setValue(last_frame)

    thisNode.reading.before.setValue(3)
    thisNode.reading.after.setValue(3)

    # cambia el premult de salida para que los .png no queden
    # con el borde negro.
    thisNode.reading.outputPremult.setValue(0)


def check_project(thisNode):
    path_list = jread('/opt/vinarender/etc/preferences_s.json').paths.system
    paths = []
    for r in path_list:
        if os.path.isdir(r):
            paths.append(r)
    if not paths:
        paths.append("#none#")

    local_filename = ''
    disconnect_filename = ''

    ok = True

    for node in get_connected_nodes(thisNode):
        if node.getPluginID() == 'vv.vinarender':
            continue

        filename_param = node.getParam("filename")
        if filename_param:
            filename = filename_param.get()

            dirname = os.path.dirname(filename)
            relative = '[Project]'

            if relative in filename:
                None
            elif not os.path.isdir(dirname):
                disconnect_filename += node.getLabel() + ' = ' + filename + '\n'
                ok = False
            else:
                is_in_vinarender_paths = False
                for p in paths:
                    if p in filename:
                        is_in_vinarender_paths = True
                if not is_in_vinarender_paths:
                    ok = False
                    local_filename += node.getLabel() + ' = ' + filename + '\n'

    if ok:
        return True
    else:
        line1 = ''
        line2 = ''
        if local_filename:
            line1 = "These files are on your PC:"
        if disconnect_filename:
            line2 = "These files are disconnected:"

        message = line1 + '\n\n' + local_filename + '\n\n' + line2 + '\n\n' + disconnect_filename
        warning('FileName Error', message)
        return False


def divide_projects(thisNode):

    # lista de proyectos divididos
    divided_projects = []

    divided_project_folder = absolute(thisNode.getParam('project_folder').get())
    prefix = thisNode.getParam('prefix').get()

    # crea lista solo con proyectos .ntp
    ntp_list = []
    for proj in os.listdir(divided_project_folder):
        ext = proj[-3:]
        if ext == 'ntp':
            ntp_list.append(proj)

    # obtiene el index de la ultima slide, extrayendola del nombre del ntp
    last_slide = 0
    for proj in ntp_list:
        _last_slide = int(proj.split('-')[-1][:-4])

        if _last_slide > last_slide:
            last_slide = _last_slide
    # ----------------------

    ranges = get_ranges(last_slide + 1, transition=False)

    for proj in ntp_list:
        project_path = divided_project_folder + '/' + proj

        slides_range = proj.split('_')[-1][:-4]
        first_slide = int(slides_range.split('-')[0])
        last_slide = int(slides_range.split('-')[-1])

        first_frame = ranges[first_slide][0]
        last_frame = ranges[last_slide][-1]

        divided_projects.append({
            'project': project_path,
            'first_frame': first_frame,
            'last_frame': last_frame
        })

    return divided_projects


def multi_project_render(thisNode, app):
    videovina_node = thisNode.getInput(0)
    if not videovina_node:
        warning('VinaRender', '!You must connect the VideoVina Node.')
        return

    render(thisNode, app, divided_project=True)


def duplicate_project(project):

    dirname = os.path.dirname(project)
    basename = os.path.basename(project)

    renders_project = dirname + '/renders'
    makedir(renders_project)

    # copia el proyecto con un nombre que no exista
    for i in range(1000):
        # encuentra version disponible
        new_project = renders_project + '/__' + basename[:-4] + '_render_' + str(i + 1) + '.ntp'
        if not os.path.isfile(new_project):
            break

    shutil.copy(project, new_project)
    #
    #

    # modifica el proyecto con rutas relativas ../ a ../../
    # adicional ya que el proyecto estara una carpeta mas adentro
    project_read = fread(new_project)
    project_read = project_read.replace('[Project]/../', '[Project]/../../')
    fwrite(new_project, project_read)
    #
    #

    return new_project


def render(thisNode, app, divided_project=False):
    videovina_node = thisNode.getInput(0)
    if not videovina_node:
        warning('VinaRender', '!You must connect the image.')
        return

    if not check_project(thisNode):
        return

    filename = thisNode.filename.get()
    output_node = 'Source'

    submit = '/opt/vinarender/bin/submit'

    project_name = app.projectName.get()

    job_name = thisNode.job_name.get()
    if not job_name:
        job_name = project_name.split('.')[0]
    server_group = 'Natron'
    task_size = thisNode.task_size.get()
    software = 'Natron'

    node_path = get_node_path(thisNode)
    if node_path:
        node_path += '.'
    render = node_path + thisNode.getScriptName() + '.' + output_node

    output = absolute(thisNode.filename.getValue())
    instances = thisNode.instances.getValue()
    project = saveProject()

    if not divided_project:
        first_frame = thisNode.getParam('range').getValue(0)
        last_frame = thisNode.getParam('range').getValue(1)

        if thisNode.duplicate_project.get():
            project = duplicate_project(project)

        extra = {
            'divided_project': False,
            'production': False,
            'divided_projects': []
        }
    else:
        divided_projects = divide_projects(thisNode)
        first_frame = 0
        last_frame = get_last_frame()
        vina = videovina_data()
        extra = {
            'production': True,
            'divided_project': divided_project,
            'divided_projects': divided_projects,
            'song': vina.song,
            'user': vina.user,
            'user_id': vina.user_id,
            'project_name': vina.project_name,
            'ranges': get_ranges(7)  # estos rangos son para las muestras
        }

    # extras adicionales
    extra = dict(extra, **{
        'output': output,
        'output_quality': thisNode.getParam('output_quality').get(),
        'fps': thisNode.getParam('fps').get(),
        'rgb_only': thisNode.rgbonly.get()
    })

    cmd = (submit
           + ' -jobName "' + job_name + '"'
           + ' -serverGroup ' + server_group
           + ' -firstFrame ' + str(first_frame)
           + ' -lastFrame ' + str(last_frame)
           + ' -taskSize ' + str(task_size)
           + ' -project "' + project + '"'
           + ' -software ' + software
           + ' -render ' + render
           + ' -extra \'' + json.dumps(extra) + "'"
           + ' -instances ' + str(instances)
           )

    os.system(cmd)

    if not thisNode.no_show_message.get():
        alert('Render Sended.', 'VinaRender')
