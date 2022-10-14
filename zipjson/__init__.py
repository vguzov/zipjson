import json
from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED

__version__ = "0.0.1"


def dump(obj, fp, *args, json_name="data.json", **kwargs):
    json_str = json.dumps(obj, *args, **kwargs)
    with ZipFile(fp, mode="w", compression=ZIP_DEFLATED) as zf:
        zf.writestr(json_name, json_str.encode("utf-8"))


def dumps(obj, *args, **kwargs):
    mem_zip = BytesIO()
    dump(obj, mem_zip, *args, **kwargs)
    return mem_zip.getvalue()


def load(fp, *args, json_name="data.json", **kwargs):
    with ZipFile(fp, mode="r") as zf:
        # for filename in zf.namelist():
        with zf.open(json_name) as cf:
            json_str = cf.read().decode("utf-8")
            obj = json.loads(json_str, *args, **kwargs)
    return obj


def loads(filebytes, *args, **kwargs):
    mem_zip = BytesIO(filebytes)
    return load(mem_zip, *args, **kwargs)
