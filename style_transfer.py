    
import shutil
import subprocess
import os

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--content_path', type=str, help="content file name")
parser.add_argument('--id', type=int, help="style id")

args = parser.parse_args()

content_path = "test_images/" + args.content_path

os.chdir(os.path.dirname(os.path.abspath(__file__)))


command = [
    "python",
    "demo.py",
    "--img_path", content_path,
    "--canvas_color", "white",
    "--max_m_strokes", "500",
    "--m_grid", "3",
    "--renderer", "oilpaintbrush",
    "--renderer_checkpoint_dir", "checkpoints_G_oilpaintbrush_light",
    "--net_G", "zou-fusion-net-light",
    "--output_dir", "./output"
]

print(subprocess.run(command, capture_output=True))

command_transfer = [
    "python",
    "demo_nst.py",
    "--renderer", "oilpaintbrush",
    "--vector_file", "./output/" + args.content_path.split(".")[0] + "_strokes.npz",
    "--style_img_path", "style_images/" + "generated_image_" + str(args.id) + ".jpeg",
    "--content_img_path", content_path,
    "--canvas_color", "white",
    "--net_G", "zou-fusion-net-light",
    "--renderer_checkpoint_dir", "checkpoints_G_oilpaintbrush_light",
    "--transfer_mode", "1"
]

subprocess.run(command_transfer)

#"style_images/" + "generated_image_" + str(args.id) + ".jpeg"

