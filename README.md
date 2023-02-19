# zipjson - a simple tool to create and read compressed JSON files

## Installation
```bash
pip install git+https://github.com/vguzov/zipjson.git
```

## Usage:
The following code creates a .zip archive with `data.json` file inside it, containing the serialized data, then reads it
```python
import zipjson
any_jsonable_data = {"something":42}
file_object = open("test.json.zip", "wb") # Mind the additional 'b' flag
zipjson.dump(any_jsonable_data, file_object)
loaded_data = zipjson.load(open("test.json.zip", "rb"))
print(loaded_data) # {'something': 42}
```

In-memory methods `dumps` and `loads` are supported as well
