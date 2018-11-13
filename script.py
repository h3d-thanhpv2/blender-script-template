import os
import sys

import bpy

exporter_dir = os.environ.get('EXPORT_SCRIPT_DIR', None)
if exporter_dir is None:
    raise EnvironmentError()
elif exporter_dir not in sys.path:
    sys.path.append(exporter_dir)


class ExportMesh(object):

    def __init__(self, mesh):
        assert mesh.type == "MESH", 'parameter object is not a mesh'
        self.mesh = mesh

    @property
    def vertices(self):
        return self.mesh.data.vectices

    @property
    def normals(self):
        return self.mesh.data.vectices

    @property
    def polygons(self):
        return self.mesh.data.polygons

    @property
    def tessfaces(self):
        if not self.mesh.data.tessfaces and self.polygons:
            self.mesh.data.calc_tessface()

        return self.mesh.data.tessfaces


if __name__ == "__main__":
    objects = bpy.data.objects

    for obj in objects:
        if obj.type == "MESH":
            ex_mesh = ExportMesh(obj)

            for face in ex_mesh.tessfaces:
                print(str(face))
