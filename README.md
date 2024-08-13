# IDA Flirt Database

Tool that converts Linux libraries into sig files for IDA

## Usage

```bash
python3 generate-sig
```

```text
usage: generate-sig.py [options]
generate-sig.py: error: the following arguments are required: -a/--arch, -p/--package
```

You need the flair directory to have these 3 commands

```
flair
├── pelf
├── sigmake
└── zipsig
```

### Misc

You may need to adjust the location of `ar` and `tar` to fit your needs
