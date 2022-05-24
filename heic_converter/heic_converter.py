import argparse
import pyheif
from typing import List
from PIL import Image
from pathlib import Path

def convert(imgs: List[str], format:str, out='.'):
    for img in imgs:
            heif_file = pyheif.read(img)
            image = Image.frombytes(
                        heif_file.mode, 
                        heif_file.size,
                        heif_file.data,
                        "raw",
                        heif_file.mode,
                        heif_file.stride,
                    )
            out_name = Path(out)/(Path(img).stem)
            image.save(out_name.with_suffix(f".{format.lower()}"), format.upper())

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Converter for heic images")
    parser.add_argument("input", nargs="+", help="Input files")
    parser.add_argument("-f", "--format", help="Output format", required=True)
    parser.add_argument("-o", "--out", default='.', help="Output directory")
    args = parser.parse_args()
    convert(args.input, args.format, args.out)
