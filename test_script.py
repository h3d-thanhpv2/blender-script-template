import pytest


def test_script():
    import os
    from subprocess import Popen, PIPE
    config = {'import': os.getcwd(),
              'python_script': os.path.join(os.getcwd(), 'script.py'),
              'blend_file': 'khay_tra.blend',
              'blender_path': os.environ.get('BLENDER_PATH', 'blender')}

    subprocess_args = [
        config['blender_path'],  # exec
        config['blend_file'], '--background',
        '--python', config['python_script'],
        '--', '--print-debug', 'true'
    ]

    convert_process = Popen(
        args=subprocess_args,
        shell=False,
        env={
            **os.environ,
            'EXPORT_SCRIPT_DIR': os.path.join(config['import'])
        },
        stdout=PIPE,
        stderr=PIPE
    )

    out, err = convert_process.communicate()
    print("blender output when running script:\n{}",format(out.decode('utf8')))
    assert not err, "These is an error:\n{}".format(err.decode('utf8'))
    assert convert_process.returncode == 0, "non-zero return code from blender converter"
