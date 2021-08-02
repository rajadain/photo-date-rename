import click
from glob import glob
from shutil import copy2
from datetime import datetime
from exif import Image
from pathlib import Path

exif_date_format = '%Y:%m:%d %H:%M:%S'
file_date_format = '%Y%m%d_%H%M%S'


@click.command()
@click.argument('src_dir', type=click.STRING)
@click.argument('dst_dir', type=click.STRING)
@click.option('--extension', '-x',
              default='jpg',
              help='File extension (default jpg)')
def main(src_dir, dst_dir, extension):
    for file in glob(f'{src_dir}/**/*.{extension}', recursive=True):
        with open(file, 'rb') as img:
            print(f'Processing {file}')
            f = Path(file)
            dt = datetime.fromtimestamp(f.stat().st_mtime)

            try:
                meta = Image(img)
                if meta.has_exif and 'datetime' in meta.list_all():
                    dt = datetime.strptime(meta['datetime'], exif_date_format)
            except Exception:
                # Could not get date from EXIF, default to file date
                pass

            # Check if destination file already exists. If so, add suffix
            dest = f'{dt.strftime(file_date_format)}.{extension}'
            suffix = 1
            while Path(f'{dst_dir}/{dest}').is_file():
                dest = f'{dt.strftime(file_date_format)}_{suffix}.{extension}'
                suffix += 1

            copy2(file, f'{dst_dir}/{dest}')


if __name__ == '__main__':
    main()
