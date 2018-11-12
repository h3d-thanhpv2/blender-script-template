import os
import sys

import bpy

exporter_dir = os.environ.get('EXPORT_SCRIPT_DIR', None)
if exporter_dir is None:
    raise EnvironmentError()
elif exporter_dir not in sys.path:
    sys.path.append(exporter_dir)

if __name__ == "__main__":
    objects = bpy.data.objects

    for obj in objects:
        if obj.type == "MESH":
            print(obj.name)
