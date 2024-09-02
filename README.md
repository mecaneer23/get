# Get

Simple clone of wget/cURL

## Usage

### Raw mode

Output to stdout (print)

```bash
python3 get.py https://example.com
```

Output to file `file.txt`

```bash
python3 get.py https://example.com file.txt
```

### Assisted mode

```bash
python3 get.py -a
```

![Gif of assisted mode](assistantUsage.gif)

Skipping prompt for save path

```bash
python3 get.py -a path/to/save-file.txt
```
