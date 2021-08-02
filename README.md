# Photo Date Rename

Simple Python 3 script to recursively scan a list of folders and copy the files to a new folder, renamed to with their date. Useful for extracting photos from corrupted macOS Photo Library folders.

Tries to read JPG EXIF data to get the date. If that fails, uses the filesystem's modified date instead.

Works on `*.jpg` files by default, but can be configured to run on any extension with `-x`, e.g. `-x heic` to run on `*.heic`.

## Dependencies

* `pipenv`
* `python3`

## Usage

```console
❯ pipenv install
❯ pipenv run python rename.py -x jpeg ~/images ~/export
```
